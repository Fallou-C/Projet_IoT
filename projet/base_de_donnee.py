from pydantic import BaseModel
from typing import List

# --- 1. La Classe (INCHANGÉE) ---
class Donnee(BaseModel):
    nom: str
    latitude: float
    longitude: float
    taille: int
    macAddresses: List[List[int]]

# --- 2. Fonction Helper (INCHANGÉE) ---
def str_to_mac(mac_list_str: List[str]) -> List[List[int]]:
    result = []
    for mac in mac_list_str:
        mac = mac.strip()
        if mac:
            try:
                result.append([int(octet, 16) for octet in mac.split(':')])
            except ValueError:
                print(f"Attention, adresse ignorée : {mac}")
    return result

# --- 3. La liste donnee_gps (INCHANGÉE) ---
donnee_gps = [
    Donnee(
        nom="esc 203", latitude=48.8451349, longitude=2.3569465, taille=4,
        macAddresses=str_to_mac(["58:97:BD:D0:96:63", "58:97:BD:D0:96:60", "58:97:BD:D0:96:62", "58:97:BD:D0:96:61"])
    ),
    Donnee(
        nom="isir", latitude=48.845691, longitude=2.356702, taille=28,
        macAddresses=str_to_mac([
            "00:F6:63:E6:2E:D4", "00:F6:63:E6:2E:D2", "00:F6:63:E6:2E:D1",
            "4C:60:DE:3C:2C:FC", "10:27:F5:CD:AD:FC", "E8:65:D4:4E:A6:81",
            "00:F6:63:E6:2F:C4", "E8:65:D4:72:A0:D9", "00:F6:63:E6:2F:C2",
            "00:F6:63:DD:3D:C1", "00:F6:63:DD:3D:C2", "D8:C7:C8:24:D0:50",
            "58:97:BD:A5:E1:74", "58:97:BD:A5:E1:72", "58:97:BD:A5:E1:71",
            "24:1F:BD:E2:55:51", "24:1F:BD:E2:55:50", "E8:65:D4:72:A0:E1",
            "E8:65:D4:72:AC:59", "E8:65:D4:72:AC:69", "E8:65:D4:72:AC:61",
            "D8:C7:C8:A8:B9:02", "00:11:32:A4:37:8B", "D8:C7:C8:A8:B9:01",
            "24:1F:BD:E2:75:10", "B8:27:EB:69:AA:50", "24:1F:BD:E2:75:11",
            "D8:C7:C8:A8:B9:00"
        ])
    ),
    Donnee(
        nom="tour du Z", latitude=48.846852, longitude=2.355515, taille=1,
        macAddresses=str_to_mac(["34:27:92:C2:75:48"])
    ),
    Donnee(
        nom="mve", latitude=48.847903, longitude=2.356386, taille=30,
        macAddresses=str_to_mac([
            "00:FE:C8:F1:23:E4", "00:FE:C8:F1:23:E2", "00:FE:C8:F1:23:E1", "00:F6:63:CE:CA:11", 
            "00:F6:63:CE:CA:12", "00:F2:8B:06:96:E0", "00:F2:8B:06:96:E2", "00:F2:8B:06:96:E3", 
            "00:F2:8B:06:96:A4", "00:F2:8B:06:96:A2", "00:F2:8B:06:96:A1", "00:F6:63:CE:CA:14",
            "00:F6:63:DD:3B:22", "00:F6:63:DD:3B:21", "00:F6:63:AC:D7:21", "00:F6:63:DD:4C:12", 
            "00:F6:63:C7:2B:B1", "00:F6:63:DD:4C:13", "00:F6:63:C7:2B:B2", "00:FE:C8:DD:2D:C2", 
            "00:F6:63:C7:29:72", "00:FE:C8:DD:2D:C1", "00:FE:C8:DD:2D:C3", "00:F6:63:C7:29:71",
            "00:FE:C8:DD:2D:C0", "00:F6:63:B1:D0:82", "E0:46:EE:A3:08:82", "00:F6:63:B1:D0:81", 
            "00:F6:63:B1:D0:84", "00:F6:63:E6:3A:84"
        ])
    ),
    Donnee(
        nom="pyramide", latitude=48.8464464, longitude=2.356551, taille=20,
        macAddresses=str_to_mac([
            "00:F6:63:E6:2E:B2", "00:F6:63:E6:2E:B1", "00:F6:63:E6:2E:B4", "00:F6:63:C7:2D:C4", 
            "00:F6:63:B1:CE:82", "00:F6:63:B1:CE:84", "00:F6:63:B1:CE:81", "00:F6:63:C7:2D:C1", 
            "00:F6:63:E6:3A:A1", "00:F6:63:C7:2D:C2", "00:F6:63:DD:3D:C4", "00:F6:63:E6:3A:A2",
            "00:F6:63:DD:4B:C1", "00:F6:63:E6:3A:A0", "00:F6:63:E6:2E:F1", "00:F6:63:DD:4B:C2", 
            "00:F6:63:DD:4B:C4", "00:F6:63:DD:3D:F4", "00:F6:63:DD:3D:F2", "00:F6:63:DD:3D:F1"
        ])
    )
]

# --- 4. MODIFICATION ICI : On utilise la liste donnee_gps ---
def get_coordonnees():
    """
    Parcourt la liste donnee_gps et extrait les infos pour la carte.
    """
    resultats = []
    for item in donnee_gps:
        # On crée un dictionnaire simple pour l'API
        infos = {
            "nom": item.nom,
            "lat": item.latitude,
            "lng": item.longitude,
            "nb_mac": item.taille
        }
        resultats.append(infos)
    return resultats