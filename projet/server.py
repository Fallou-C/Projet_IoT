import asyncio
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# 1. Création du modèle de données (Pydantic)
# Cela valide que l'entrée correspond exactement à ton JSON
class MacInput(BaseModel):
    macAddresses: List[List[int]] # Liste de listes d'entiers
    taille: int

# Simulation d'une base de données pour stocker les résultats
mac_storage = []

@app.get("/")
async def root():
    return {"message": "Hello World"}

# 2. Endpoint POST mis à jour
@app.post("/items/save-mac")
async def save_mac_addresses(data: MacInput):
    """
    Reçoit un objet JSON contenant une liste d'adresses MAC et une taille.
    Stocke les adresses dans une liste globale.
    """
    
    # Validation simple (optionnelle) : vérifier que la taille correspond
    if len(data.macAddresses) != data.taille:
        return {"error": "La taille déclarée ne correspond pas au nombre d'adresses"}

    # 3. Stockage des données
    # On ajoute les nouvelles adresses à notre liste globale
    mac_storage.extend(data.macAddresses)
    
	#on supprime les premières si y'en a trop
    while(len(mac_storage) > 50):
        mac_storage.pop(0)

    return {
        "message": "Adresses sauvegardées avec succès",
        "adresses_recues": data.macAddresses,
        "total_adresses_stockees": len(mac_storage)
    }

@app.get("/view-macs")
async def get_stored_macs():
    """Endpoint pour vérifier ce qui a été stocké"""
    return {"database": mac_storage}

