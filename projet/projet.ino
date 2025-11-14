/*
 *  WiFi scan avec filtrage : afficher seulement les réseaux NON-téléphones
 */
#include <HardwareSerial.h>
#include "WiFi.h"

HardwareSerial loraSerial(2);
#define LORA_RX 16
#define LORA_TX 17

bool loraJoined = false;

void sendAT(String cmd) {
  Serial.print(">> "); Serial.println(cmd);
  loraSerial.println(cmd);

  unsigned long start = millis();
  while (millis() - start < 3000) { // max 3 sec d'attente
    while (loraSerial.available()) {
      String resp = loraSerial.readStringUntil('\n');
      if (resp.length() > 0) {
        Serial.print("<< ");
        Serial.println(resp);
      }
    }
  }
}

// ---------------------------------------------------------
// Détection fiable d'un point d'accès venant d'un téléphone
// ---------------------------------------------------------
bool isPhoneAP(int i) {

  String ssid = WiFi.SSID(i);
  uint8_t* b = WiFi.BSSID(i);
  wifi_auth_mode_t auth = WiFi.encryptionType(i);

  // Convertir BSSID → string
  char mac[18];
  sprintf(mac, "%02X:%02X:%02X:%02X:%02X:%02X",
          b[0], b[1], b[2], b[3], b[4], b[5]);
  String bssidStr = String(mac);

  // 1) MAC randomisée → très souvent un smartphone
  // (premier octet B2 = local administered + unicast)
  if ((b[0] & 0x02) == 0x02) return true;

  // 2) OUI de fabricants de téléphones
  const char* phoneOUI[] = {
    // Apple
    "28:F0:76","A4:5E:60","88:E9:FE","D0:03:4B",
    // Samsung
    "1C:99:4C","D4:3A:2A","44:27:8D","08:3B:2C",
    // Huawei
    "50:1A:A5","00:9A:CD","78:11:DC",
    // Xiaomi
    "4C:49:E3","30:FC:68",
    // OnePlus
    "94:65:2D","3C:2C:30"
  };

  String oui = bssidStr.substring(0, 8);
  for (int k = 0; k < sizeof(phoneOUI)/sizeof(phoneOUI[0]); k++) {
    if (oui.equalsIgnoreCase(phoneOUI[k])) return true;
  }

  // 3) SSID typiques des hotspots téléphones
  if (ssid.indexOf("iPhone") >= 0 ||
      ssid.indexOf("Android") >= 0 ||
      ssid.indexOf("Galaxy") >= 0 ||
      ssid.indexOf("OnePlus") >= 0 ||
      ssid.indexOf("HUAWEI") >= 0 ||
      ssid.indexOf("Xiaomi") >= 0 ||
      ssid.indexOf("Hotspot") >= 0)
      return true;

  // 4) Enterprise = jamais un téléphone → pas téléphone
  if (auth == WIFI_AUTH_WPA2_ENTERPRISE ||
      auth == WIFI_AUTH_WPA3_ENTERPRISE)
      return false;

  // sinon → pas un téléphone
  return false;
}

// ---------------------------------------------------------
void setup() {
  Serial.begin(115200);
  WiFi.STA.begin(); // mode station
  delay(1000);
  loraSerial.begin(9600, SERIAL_8N1, LORA_RX, LORA_TX);

  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, 0);

  delay(1000); // Laisser au module le temps de démarrer
  sendAT("AT+VER");
  sendAT("AT+ID=DevEUI,70B3D57ED0073264");   // DevEUI 
  delay(300);

  sendAT("AT+ID=AppEUI,0000000000000000");   // AppEUI 
  delay(300);

  sendAT("AT+KEY=APPKEY,A5559C4C4943F7EDBE1795FE30505AA0"); // AppKey 
  delay(300);

  sendAT("AT+DR=5");  // Data Rate (ex: 5 pour EU868)
  delay(300);

  sendAT("AT+JOIN");  // Tentative de rejoindre le réseau
  // Lire les réponses pendant 10 secondes
  delay(10000);

  bool joined = false;
  unsigned long start = millis();
  while (millis() - start < 10000) {
    while (loraSerial.available()) {
      String resp = loraSerial.readStringUntil('\n');
      resp.trim();
      Serial.print("<< ");
      Serial.println(resp);
      if (resp.indexOf("+JOIN: Done") != -1) {
        joined = true;
      }
      if (resp.indexOf("+JOIN: Fail") != -1) {
        Serial.println("❌ JOIN échoué !");
      }
    }
  }

if (joined) {
  Serial.println("LoRaWAN JOIN réussi !");
} else {
  Serial.println("LoRaWAN JOIN non confirmé !");
}

  delay(2000);
}

// ---------------------------------------------------------
void ScanWiFi() {
  Serial.println("Scan start");
  int n = WiFi.scanNetworks();
  Serial.println("Scan done");

  if (n == 0) {
    Serial.println("no networks found");
  } else {

    Serial.print(n);
    Serial.println(" networks found");
    Serial.println("Nr | SSID                             | RSSI | CH | Encryption | BSSID");

    String atCommand = "AT+MSGHEX=";

    for (int i = 0; i < n; ++i) {

      // ----------- NOUVEAU FILTRE : ignorer téléphones -----------
      if (isPhoneAP(i)) continue;

      // ----------- Affichage original -----------
      Serial.printf("%2d", i + 1);
      Serial.print(" | ");
      Serial.printf("%-32.32s", WiFi.SSID(i).c_str());
      Serial.print(" | ");
      Serial.printf("%4ld", WiFi.RSSI(i));
      Serial.print(" | ");
      Serial.printf("%2ld", WiFi.channel(i));
      Serial.print(" | ");

      switch (WiFi.encryptionType(i)) {
        case WIFI_AUTH_OPEN:            Serial.print("open"); break;
        case WIFI_AUTH_WEP:             Serial.print("WEP"); break;
        case WIFI_AUTH_WPA_PSK:         Serial.print("WPA"); break;
        case WIFI_AUTH_WPA2_PSK:        Serial.print("WPA2"); break;
        case WIFI_AUTH_WPA_WPA2_PSK:    Serial.print("WPA+WPA2"); break;
        case WIFI_AUTH_WPA2_ENTERPRISE: Serial.print("WPA2-EAP"); break;
        case WIFI_AUTH_WPA3_PSK:        Serial.print("WPA3"); break;
        case WIFI_AUTH_WPA2_WPA3_PSK:   Serial.print("WPA2+WPA3"); break;
        case WIFI_AUTH_WAPI_PSK:        Serial.print("WAPI"); break;
        default:                        Serial.print("unknown");
      }

      Serial.print(" | ");

      uint8_t *bssid = WiFi.BSSID(i);
      for (int j = 0; j < 6; j++) {
        if (j > 0) Serial.print(":");
        Serial.printf("%02X", bssid[j]);
      }

      String bssidHex = "";
      for (int j = 0; j < 6; j++) {
      if (bssid[j] < 16) bssidHex += "0";
        bssidHex += String(bssid[j], HEX);
      }
      bssidHex.toUpperCase();
      atCommand = atCommand + bssidHex;
      
      Serial.println();
      delay(10);
    }
    loraSerial.println(atCommand);
  }

  WiFi.scanDelete();
  Serial.println("-------------------------------------");
}

// ---------------------------------------------------------
void loop() {

  Serial.println("-------------------------------------");
  Serial.println("Default wifi band mode scan:");
  Serial.println("-------------------------------------");

#if ESP_IDF_VERSION >= ESP_IDF_VERSION_VAL(5, 4, 2)
  WiFi.setBandMode(WIFI_BAND_MODE_AUTO);
#endif

  ScanWiFi();

#if CONFIG_SOC_WIFI_SUPPORT_5G
  delay(1000);
  Serial.println("-------------------------------------");
  Serial.println("2.4 GHz wifi band mode scan:");
  Serial.println("-------------------------------------");

  WiFi.setBandMode(WIFI_BAND_MODE_2G_ONLY);
  ScanWiFi();

  delay(1000);
  Serial.println("-------------------------------------");
  Serial.println("5 GHz wifi band mode scan:");
  Serial.println("-------------------------------------");

  WiFi.setBandMode(WIFI_BAND_MODE_5G_ONLY);
  ScanWiFi();
#endif

  delay(10000);
}
