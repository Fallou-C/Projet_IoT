from pydantic import BaseModel
from typing import List


class Donnee(BaseModel):
    nom: str
    latitude: float
    longitude: float
    taille: int
    macAddresses: List[List[int]]


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

# base de donnée fixe
# Assurez-vous d'avoir vos imports et la fonction str_to_mac définis au dessus

donnee_gps = [
    # 1. ESC 203
    Donnee(
        nom="esc 203", latitude=48.8451349, longitude=2.3569465, taille=4,
        macAddresses=str_to_mac([
            "58:97:BD:D0:96:63", "58:97:BD:D0:96:60", "58:97:BD:D0:96:62", "58:97:BD:D0:96:61"
        ])
    ),
    # 2. ISIR
    Donnee(
        nom="isir", latitude=48.845694, longitude=2.356735, taille=27,
        macAddresses=str_to_mac([
            "00:F6:63:E6:2E:D4", "00:F6:63:E6:2E:D2", "00:F6:63:E6:2E:D1", "4C:60:DE:3C:2C:FC",
            "10:27:F5:CD:AD:FC", "E8:65:D4:4E:A6:81", "00:F6:63:E6:2F:C4", "E8:65:D4:72:A0:D9",
            "00:F6:63:E6:2F:C2", "00:F6:63:DD:3D:C1", "00:F6:63:DD:3D:C2", "D8:C7:C8:24:D0:50",
            "58:97:BD:A5:E1:74", "58:97:BD:A5:E1:72", "58:97:BD:A5:E1:71", "24:1F:BD:E2:55:51",
            "24:1F:BD:E2:55:50", "E8:65:D4:72:A0:E1", "E8:65:D4:72:AC:59", "E8:65:D4:72:AC:69",
            "E8:65:D4:72:AC:61", "D8:C7:C8:A8:B9:02", "00:11:32:A4:37:8B", "D8:C7:C8:A8:B9:01",
            "24:1F:BD:E2:75:10", "B8:27:EB:69:AA:50", "24:1F:BD:E2:75:11", "D8:C7:C8:A8:B9:00"
        ])
    ),
    # 3. Tour à l'entrée
    Donnee(
        nom="tour à l’entrée", latitude=48.846852, longitude=2.355515, taille=1,
        macAddresses=str_to_mac(["34:27:92:C2:75:48"])
    ),
    # 4. MVE
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
    # 5. Pyramide
    Donnee(
        nom="pyramide", latitude=48.8464464, longitude=2.356551, taille=20,
        macAddresses=str_to_mac([
            "00:F6:63:E6:2E:B2", "00:F6:63:E6:2E:B1", "00:F6:63:E6:2E:B4", "00:F6:63:C7:2D:C4",
            "00:F6:63:B1:CE:82", "00:F6:63:B1:CE:84", "00:F6:63:B1:CE:81", "00:F6:63:C7:2D:C1",
            "00:F6:63:E6:3A:A1", "00:F6:63:C7:2D:C2", "00:F6:63:DD:3D:C4", "00:F6:63:E6:3A:A2",
            "00:F6:63:DD:4B:C1", "00:F6:63:E6:3A:A0", "00:F6:63:E6:2E:F1", "00:F6:63:DD:4B:C2",
            "00:F6:63:DD:4B:C4", "00:F6:63:DD:3D:F4", "00:F6:63:DD:3D:F2", "00:F6:63:DD:3D:F1"
        ])
    ),
    # 6. Tour 66
    Donnee(
        nom="Tour 66", latitude=48.845367, longitude=2.356772, taille=14,
        macAddresses=str_to_mac([
            "E8:65:D4:4E:A6:81", "80:EA:96:EE:36:2C", "00:F6:63:C7:2A:74", "00:F6:63:C7:2A:72",
            "00:F6:63:C7:2A:71", "E8:65:D4:72:AC:59", "00:F6:63:DD:3C:F4", "00:F6:63:DD:3C:F2",
            "00:F6:63:DD:3C:F1", "24:1F:BD:E1:D0:90", "24:1F:BD:E1:D0:91", "00:F6:63:AC:D6:32",
            "00:F6:63:E6:2E:D2", "00:F6:63:AC:D6:34"
        ])
    ),
    # 7. Tour 65
    Donnee(
        nom="Tour 65", latitude=48.845663, longitude=2.357287, taille=7,
        macAddresses=str_to_mac([
            "00:F6:63:AC:D6:34", "00:F6:63:AC:D6:32", "00:F6:63:AC:D6:31", "E8:65:D4:72:AC:59",
            "58:D9:D5:41:50:32", "00:F6:63:C7:2A:71", "00:F6:63:DD:3C:F4"
        ])
    ),
    # 8. Tour 55
    Donnee(
        nom="Tour 55", latitude=48.846080, longitude=2.356654, taille=15,
        macAddresses=str_to_mac([
            "00:F6:63:E6:2F:C1", "00:F6:63:E6:2F:C4", "00:F6:63:E6:2F:C2", "00:F6:63:E6:2E:D4",
            "00:F6:63:E6:2E:D2", "00:F6:63:E6:2E:D1", "10:27:F5:CD:AD:FC", "DC:00:B0:F7:5F:80",
            "14:91:82:8D:BC:3C", "00:F6:63:DD:3D:C4", "00:F6:63:C7:2D:C4", "00:F6:63:DD:3D:C1",
            "00:F6:63:DD:3D:C2", "00:F6:63:E6:2E:B4", "D0:6E:DE:C9:92:90"
        ])
    ),
    # 9. Tour 56
    Donnee(
        nom="Tour 56", latitude=48.845755, longitude=2.356172, taille=31,
        macAddresses=str_to_mac([
            "00:F6:63:E6:2E:D1", "00:F6:63:E6:2E:D4", "E8:65:D4:4E:A6:81", "00:F6:63:E6:2E:D2",
            "00:F6:63:E6:2E:B4", "00:F6:63:E6:2E:B2", "00:F6:63:C7:2A:74", "00:F6:63:C7:2A:71",
            "00:F6:63:E6:2E:B1", "00:F6:63:E6:2F:C1", "00:F6:63:E6:2F:C4", "00:F6:63:E6:2F:C2",
            "00:F6:63:DD:3C:F2", "00:F6:63:C7:2A:72", "04:D4:C4:0A:AC:F0", "00:F6:63:DD:3C:F4",
            "00:F6:63:DD:3C:F1", "24:1F:BD:E2:55:50", "24:1F:BD:E2:55:51", "00:F6:63:DD:3D:C1",
            "00:F6:63:DD:3D:C4", "00:F6:63:DD:3D:C2", "00:F6:63:C7:2D:C2", "4C:60:DE:3C:2C:FC",
            "58:D9:D5:41:50:32", "D8:C7:C8:24:D0:51", "00:F6:63:C7:2D:C4", "D8:C7:C8:24:D1:32",
            "80:EA:96:EE:36:2C", "D8:C7:C8:24:D0:53"
        ])
    ),
    # 10. Tour 46
    Donnee(
        nom="Tour 46", latitude=48.846158, longitude=2.355572, taille=24,
        macAddresses=str_to_mac([
            "F0:A7:31:14:32:75", "00:F6:63:DD:36:C4", "00:F6:63:DD:36:C2", "00:F6:63:DD:36:C1",
            "D8:47:32:5C:69:1E", "00:F6:63:DD:3D:C4", "00:F6:63:DD:3D:C1", "00:F6:63:DD:3D:C2",
            "00:F6:63:AC:D8:32", "00:F6:63:AC:D8:31", "00:F6:63:DD:3C:F1", "84:B2:61:75:82:01",
            "84:B2:61:75:82:02", "84:B2:61:75:82:03", "84:B2:61:75:82:00", "00:F6:63:DD:3C:F4",
            "D8:C7:C8:24:D0:53", "6C:61:F4:3A:8F:BE", "00:F6:63:E6:2E:D4", "00:F6:63:E6:2F:C4",
            "D8:C7:C8:24:D0:51", "00:F6:63:C7:2D:C4", "00:F6:63:C7:2D:C2", "D8:C7:C8:A8:B9:71",
            "D8:C7:C8:A8:B9:72"
        ])
    ),
    # 11. Tour 45
    Donnee(
        nom="Tour 45", latitude=48.846497, longitude=2.356043, taille=9,
        macAddresses=str_to_mac([
            "00:F6:63:B1:CD:91", "00:F6:63:B1:CD:94", "00:F6:63:B1:CD:92", "00:F6:63:C7:2A:F2",
            "00:F6:63:C7:2A:F1", "00:F6:63:C7:2A:F4", "00:FE:C8:F1:44:72", "00:FE:C8:F1:44:71",
            "00:FE:C8:F1:44:74"
        ])
    ),
    # 12. Tour 44
    Donnee(
        nom="Tour 44", latitude=48.846792, longitude=2.356590, taille=22,
        macAddresses=str_to_mac([
            "00:F6:63:C7:2D:C2", "00:F6:63:E6:3A:A1", "00:F6:63:C7:2D:C4", "00:F6:63:C7:2D:C1",
            "00:F6:63:E6:3A:A3", "00:F6:63:E6:3A:A2", "00:F6:63:DD:4B:C2", "00:F6:63:DD:4B:C1",
            "00:F6:63:C7:2A:F1", "00:F6:63:DD:4B:22", "00:F6:63:DD:4B:21", "00:F6:63:DD:4B:24",
            "00:F6:63:E6:3A:A0", "00:F6:63:DD:4B:C4", "58:97:BD:5D:5F:31", "58:97:BD:5D:5F:33",
            "00:F6:63:DD:3D:F4", "00:F6:63:E6:2E:B1", "00:F6:63:DD:3D:F1", "00:F6:63:C7:2A:F4",
            "58:97:BD:5D:5F:32", "58:97:BD:5D:5F:30"
        ])
    ),
    # 13. Tour 54
    Donnee(
        nom="Tour 54", latitude=48.846401, longitude=2.357179, taille=23,
        macAddresses=str_to_mac([
            "00:F6:63:E6:2E:F2", "00:F6:63:E6:2E:F1", "00:F6:63:E6:2E:F4", "00:F6:63:AC:D9:E2",
            "00:F6:63:E6:2E:B2", "00:F6:63:AC:D9:E4", "00:F6:63:AC:D9:E1", "00:F6:63:E6:2E:B4",
            "00:F6:63:E6:2E:B1", "00:F6:63:DD:3D:F4", "00:F6:63:DD:3D:F2", "00:F6:63:DD:3D:F1",
            "00:F6:63:C7:2D:C4", "00:F6:63:C7:2D:C2", "00:F6:63:C7:2D:C1", "00:F6:63:B1:CE:84",
            "00:F6:63:B1:CE:81", "00:F6:63:DD:4B:C4", "00:F6:63:DD:4B:C1", "58:97:BD:BC:01:A4",
            "00:F6:63:B1:CE:82", "00:F6:63:DD:4B:C2", "58:97:BD:BC:01:A2", "58:97:BD:BC:01:A1"
        ])
    ),
    # 14. Tour 53
    Donnee(
        nom="Tour 53", latitude=48.846722, longitude=2.357672, taille=6,
        macAddresses=str_to_mac([
            "00:F6:63:AC:D9:E2", "00:F6:63:AC:D9:E4", "00:F6:63:AC:D9:E1", "00:F6:63:B1:CE:82",
            "00:F6:63:B1:CE:81", "00:F6:63:B1:CE:84"
        ])
    ),
    # 15. Atrium
    Donnee(
        nom="Atrium", latitude=48.846323, longitude=2.357728, taille=13,
        macAddresses=str_to_mac([
            "00:F6:63:B1:CE:82", "00:F6:63:B1:CE:81", "00:F6:63:B1:CE:84", "00:F6:63:AC:D9:E1",
            "00:F6:63:AC:D9:E2", "E4:38:83:5E:C0:F2", "00:F6:63:AC:D9:E4", "34:64:A9:67:C6:53",
            "00:F2:8B:06:8B:52", "60:22:32:AC:6F:BA", "18:8B:9D:92:23:72", "00:F2:8B:06:8B:51",
            "18:8B:9D:92:23:71"
        ])
    ),
    # 16. Tour 43
    Donnee(
        nom="Tour 43", latitude=48.847128, longitude=2.357074, taille=14,
        macAddresses=str_to_mac([
            "00:F6:63:C7:36:64", "00:F6:63:C7:36:62", "00:F6:63:C7:36:61", "00:F6:63:DD:4B:24",
            "00:F6:63:DD:4B:21", "00:F6:63:DD:4B:22", "00:F6:63:DD:4A:A4", "00:F6:63:C7:36:51",
            "00:F6:63:DD:4A:A2", "00:F6:63:C7:36:54", "00:F6:63:DD:4B:C2", "08:5A:11:28:8A:63",
            "00:F6:63:C7:36:52", "00:F6:63:DD:4B:C4"
        ])
    ),
    # 17. Tour 33
    Donnee(
        nom="Tour 33", latitude=48.847520, longitude=2.356478, taille=9,
        macAddresses=str_to_mac([
            "00:F6:63:DD:4A:A2", "00:F6:63:DD:4A:A1", "00:F6:63:DD:4A:A4", "00:F6:63:CE:D3:04",
            "00:F6:63:CE:D3:02", "00:F6:63:CE:D3:01", "00:F6:63:B1:CC:F4", "00:F6:63:C7:36:52",
            "00:F6:63:C7:36:51"
        ])
    ),
    # 18. Tour 34
    Donnee(
        nom="Tour 34", latitude=48.847195, longitude=2.356006, taille=19,
        macAddresses=str_to_mac([
            "00:F6:63:CE:D3:02", "00:F6:63:CE:D3:01", "00:F6:63:CE:D3:04", "00:F6:63:DD:4B:64",
            "00:F6:63:DD:4B:62", "00:F6:63:DD:4B:61", "00:F6:63:DD:4A:A1", "00:F6:63:DD:4A:A4",
            "00:F6:63:B1:CC:F3", "00:F6:63:DD:4A:A2", "00:F6:63:B1:CC:F0", "00:F6:63:B1:CC:F4",
            "00:F6:63:B1:CC:F2", "00:F6:63:C7:2A:F2", "00:F6:63:C7:2A:F4", "00:F6:63:C7:2A:F1",
            "00:F6:63:E6:3B:04", "00:F6:63:E6:3B:01", "9C:3D:CF:B5:EF:32", "00:F6:63:C7:34:F2"
        ])
    ),
    # 19. Tour 24
    Donnee(
        nom="Tour 24", latitude=48.847601, longitude=2.355379, taille=37,
        macAddresses=str_to_mac([
            "00:F6:63:CE:CA:14", "00:F6:63:CE:CA:12", "00:F6:63:CE:CA:11", "00:F6:63:DD:4C:10",
            "00:F6:63:DD:4C:11", "00:F6:63:DD:4C:12", "00:F6:63:DD:4C:13", "00:F6:63:B1:CF:24",
            "00:F6:63:B1:CF:22", "00:F6:63:B1:CF:21", "00:F6:63:CA:D8:84", "00:F6:63:CA:D8:81",
            "00:F6:63:DD:3D:52", "00:F6:63:CA:D8:82", "00:F6:63:CA:E4:B2", "00:F6:63:DD:3B:21",
            "00:F6:63:DD:3D:51", "00:F6:63:C7:2B:B1", "00:F6:63:E6:3B:81", "00:F6:63:CE:C3:51",
            "00:F6:63:C7:2B:B4", "00:F6:63:CA:E4:B4", "00:F6:63:DD:3D:54", "00:F6:63:CA:E4:B1",
            "00:F6:63:B1:D0:82", "00:F6:63:DD:3B:24", "00:F6:63:DD:3B:22", "00:F6:63:CE:C3:54",
            "00:F6:63:CE:C3:52", "00:F6:63:E6:3B:84", "00:F6:63:B1:D0:84", "00:F2:8B:06:96:E3",
            "00:F2:8B:06:96:E0", "00:F6:63:E6:3B:82", "00:F6:63:B1:D0:81", "00:F2:8B:06:96:E1",
            "00:F2:8B:06:96:E2", "00:F6:63:CE:C0:94", "00:F6:63:AC:D7:24"
        ])
    ),
    # 20. Tour 23
    Donnee(
        nom="Tour 23", latitude=48.847929, longitude=2.355890, taille=36,
        macAddresses=str_to_mac([
            "00:F6:63:CE:CA:14", "00:F6:63:CE:CA:12", "00:F6:63:CE:CA:11", "00:F6:63:C7:2B:B1",
            "00:F6:63:CA:E4:B4", "00:F6:63:CA:E4:B2", "00:F6:63:CA:E4:B1", "00:F6:63:C7:2B:B2",
            "00:F6:63:C7:2B:B4", "00:F6:63:AC:D7:24", "00:F6:63:AC:D7:22", "00:F6:63:AC:D7:21",
            "00:F6:63:E6:3B:84", "00:F6:63:E6:3B:82", "00:F6:63:E6:3B:81", "00:F6:63:DD:4A:A1",
            "00:F6:63:DD:4C:10", "00:F6:63:B1:CC:F4", "00:F6:63:B1:CC:F3", "00:F6:63:DD:4C:11",
            "00:F6:63:B1:CC:F0", "00:F6:63:B1:CC:F2", "00:F6:63:DD:4C:13", "00:F6:63:CE:C0:91",
            "00:F6:63:CE:C3:54", "00:F6:63:CE:C0:92", "00:F6:63:DD:3D:54", "00:F2:8B:06:96:E2",
            "00:F6:63:DD:3B:21", "00:F6:63:DD:4A:A4", "00:F6:63:B1:D0:84", "00:F6:63:B1:CF:22",
            "00:F6:63:CE:C3:52", "00:F6:63:CE:C0:94", "00:F6:63:DD:4C:12", "00:F2:8B:06:96:E1",
            "00:F6:63:DD:3D:52"
        ])
    ),
    # 21. Tour 13
    Donnee(
        nom="Tour 13", latitude=48.848332, longitude=2.355292, taille=37,
        macAddresses=str_to_mac([
            "00:F6:63:CE:C3:54", "00:F6:63:CE:CA:11", "00:F6:63:CE:CA:12", "00:F6:63:C7:29:72",
            "00:F6:63:C7:29:71", "00:F6:63:E6:3A:81", "00:F6:63:C7:29:74", "04:70:56:CF:94:4D",
            "00:F6:63:DD:4C:13", "00:F6:63:E6:3A:82", "00:F6:63:CE:C0:91", "00:F6:63:AC:D7:24",
            "00:24:D4:56:68:20", "00:FE:C8:F1:35:43", "00:F6:63:B1:CF:22", "00:FE:C8:F1:35:40",
            "00:F6:63:CA:D8:82", "00:F6:63:E6:3A:84", "00:FE:C8:F1:35:42", "00:F6:63:CE:C0:92",
            "00:F6:63:CE:C0:94", "00:F6:63:DD:4C:12", "00:F6:63:AC:D7:21", "00:F6:63:AC:D7:22",
            "00:F6:63:B1:CF:24", "00:FE:C8:F1:35:41", "00:F6:63:DD:4C:10", "00:F6:63:CA:D8:84",
            "00:F6:63:B1:CF:21", "00:F6:63:DD:4A:A4", "00:F6:63:DD:4C:11", "00:F6:63:CA:D8:81",
            "00:FE:C8:DD:33:F2", "00:F6:63:E6:2C:21", "00:F6:63:DD:4A:A1", "34:27:92:34:E2:27",
            "20:66:CF:FC:E5:18", "8C:97:EA:8E:00:70", "00:FE:C8:DD:33:F4", "40:65:A3:00:2F:A6",
            "00:F6:63:CA:E4:B4", "00:F6:63:CA:E4:B1", "60:35:C0:25:93:C6", "18:86:37:1A:FB:B0",
            "00:1B:93:01:16:55"
        ])
    ),
    # 22. Tour 14
    Donnee(
        nom="Tour 14", latitude=48.848039, longitude=2.354767, taille=34,
        macAddresses=str_to_mac([
            "00:F6:63:CE:C3:51", "00:F6:63:CE:C3:54", "00:F6:63:CE:C3:52", "00:F6:63:C7:2B:B1",
            "00:F6:63:C7:2B:B4", "00:F6:63:C7:2B:B2", "00:F6:63:B1:CF:22", "00:F6:63:B1:CF:21",
            "00:F6:63:B1:D0:81", "00:F6:63:B1:D0:84", "00:F6:63:B1:D0:82", "00:F6:63:B1:CF:24",
            "00:F6:63:DD:3B:22", "00:F6:63:DD:3D:54", "00:F6:63:DD:3D:52", "00:F6:63:DD:4C:12",
            "00:F6:63:DD:4C:13", "00:F6:63:DD:4C:10", "00:F6:63:DD:3D:51", "00:F6:63:CA:D8:84",
            "00:F6:63:DD:4C:11", "00:F6:63:DD:3B:21", "00:F6:63:DD:3B:24", "00:F6:63:CA:D8:81",
            "00:F6:63:CA:D8:82", "00:F6:63:E6:3B:84", "00:F6:63:E6:3B:81", "00:F6:63:CE:CA:12",
            "00:F6:63:C7:29:71", "00:F6:63:AC:D7:21", "00:F6:63:E6:2C:21", "00:F6:63:E6:2C:24",
            "00:F6:63:E6:2C:22", "00:F6:63:CE:CA:14", "00:F6:63:E6:3A:81", "00:F6:63:CE:CA:11",
            "00:F6:63:C7:29:72", "00:F6:63:C7:29:74"
        ])
    ),
    # 23. Tour 25
    Donnee(
        nom="Tour 25", latitude=48.847283, longitude=2.354885, taille=35,
        macAddresses=str_to_mac([
            "00:F6:63:B1:CF:24", "00:F6:63:B1:CF:22", "00:F6:63:B1:CF:21", "00:F6:63:B1:D0:31",
            "00:F6:63:E6:3B:81", "00:F6:63:B1:D0:32", "00:F6:63:B1:D0:34", "00:F6:63:E6:3B:84",
            "00:F6:63:E6:3B:82", "00:F6:63:DD:4C:13", "0C:D5:D3:AC:28:02", "00:F6:63:DD:4C:10",
            "00:F6:63:DD:4C:12", "00:F6:63:DD:4C:11", "00:F6:63:DD:3B:24", "0C:D5:D3:AC:28:00",
            "00:F6:63:DD:3B:22", "0C:D5:D3:AC:28:01", "00:F6:63:DD:3B:21", "00:FE:C8:FD:B3:C4",
            "00:F6:63:DD:3D:51", "00:F6:63:E6:3A:22", "00:FE:C8:FD:B3:C1", "00:F6:63:E6:3A:21",
            "0C:D5:D3:AC:75:02", "68:D7:9A:D4:28:40", "00:F6:63:CE:C3:51", "00:F6:63:DD:3D:54",
            "00:F6:63:E6:3A:24", "00:FE:C8:FD:B3:C2", "00:F6:63:AC:D7:22", "0C:D5:D3:AC:75:00",
            "00:F6:63:E6:3D:14", "00:F6:63:E6:3D:12", "0C:D5:D3:AC:75:01", "00:1B:93:01:13:C7"
        ])
    ),
    # 24. Tour 26
    Donnee(
        nom="Tour 26", latitude=48.846965, longitude=2.354381, taille=34,
        macAddresses=str_to_mac([
            "0C:D5:D3:AC:75:00", "00:FE:C8:FD:B3:C4", "0C:D5:D3:AC:75:02", "0C:D5:D3:AC:2F:A0",
            "0C:D5:D3:AC:2F:A1", "0C:D5:D3:AC:2F:A2", "00:FE:C8:FD:B3:C2", "00:FE:C8:FD:B3:C1",
            "0C:D5:D3:AC:75:01", "0C:D5:D3:AC:63:80", "0C:D5:D3:AC:63:81", "0C:D5:D3:AC:63:82",
            "00:F6:63:E6:3A:22", "00:F6:63:E6:3A:21", "68:D7:9A:D4:28:40", "00:F6:63:E6:3A:24",
            "00:F6:63:E6:3D:11", "00:FE:C8:EF:9B:92", "00:F6:63:C7:29:54", "70:BC:48:54:6D:21",
            "70:BC:48:54:6D:22", "00:FE:C8:EF:9B:91", "00:F6:63:CA:D5:B2", "14:0C:76:7B:BF:D6",
            "00:F6:63:CA:D5:B1", "0C:D5:D3:AC:28:00", "0C:D5:D3:AC:28:02", "00:F6:63:C7:29:52",
            "00:F6:63:C7:29:51", "00:FE:C8:EF:9B:94", "00:F6:63:CE:C9:54", "B4:E2:65:F3:15:E4",
            "74:08:DE:0B:F7:F9", "00:F6:63:CE:C9:52", "B4:E2:65:CA:C7:35"
        ])
    ),
    # 25. Tour 16
    Donnee(
        nom="Tour 16", latitude=48.847375, longitude=2.353780, taille=27,
        macAddresses=str_to_mac([
            "00:F6:63:CA:D5:B4", "00:F6:63:CA:D5:B2", "00:F6:63:CA:D5:B1", "00:F6:63:CE:C9:54",
            "00:F6:63:CE:C9:52", "00:F6:63:CE:C9:51", "00:F6:63:CE:C0:F4", "00:F6:63:CE:C0:F1",
            "00:F6:63:CE:C0:F2", "00:F6:63:E6:3D:12", "DC:15:C8:05:E7:72", "00:F6:63:E6:3D:11",
            "00:F6:63:E6:3D:14", "68:D7:9A:D4:28:40", "00:F6:63:CE:C3:51", "EC:75:0C:9D:D0:96",
            "00:F6:63:CA:D8:84", "00:F6:63:CA:D8:81", "14:0C:76:7B:BF:D6", "74:08:DE:0B:F7:F9",
            "00:F6:63:DD:3D:51", "F0:81:75:1A:C7:70", "A8:6A:BB:5D:C3:64", "00:1B:93:01:16:55",
            "00:F6:63:DD:3D:52", "CC:19:A8:14:69:50"
        ])
    )
]

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

def prevision_emplacement(mac_addresses: List[List[int]]):
    coordonnes = [0,0]
    nb_points = 0
    for donnee in donnee_gps:
        for mac in mac_addresses:
            if mac in donnee.macAddresses:
                coordonnes[0] += donnee.latitude
                coordonnes[1] += donnee.longitude
                nb_points += 1
    coordonnes[0] = coordonnes[0] / nb_points if nb_points > 0 else 0
    coordonnes[1] = coordonnes[1] / nb_points if nb_points > 0 else 0
    return coordonnes
