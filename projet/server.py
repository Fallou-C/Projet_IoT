from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi.responses import HTMLResponse
import base_de_donnee

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

@app.get("/api/points")
async def api_points():
    # On appelle la fonction qui lit votre liste donnee_gps
    return base_de_donnee.get_coordonnees()

@app.get("/carte", response_class=HTMLResponse)
async def affichage_carte():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Carte Jussieu/Sorbonne</title>
        <meta charset="utf-8">
        <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
        <style>
            #map { height: 100vh; width: 100%; }
            body { margin: 0; }
        </style>
    </head>
    <body>
        <div id="map"></div>

        <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
        <script>
            // 1. Centrer la carte sur le secteur (Paris 5ème/Jussieu)
            // J'ai pris les coord. de "isir" comme centre approximatif
            var map = L.map('map').setView([48.845, 2.356], 16);

            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                attribution: '&copy; OpenStreetMap'
            }).addTo(map);

            // 2. Récupérer les données Python via l'API
            fetch('/api/points')
                .then(response => response.json())
                .then(data => {
                    console.log("Données reçues :", data); // Pour vérifier dans la console du navigateur
                    
                    data.forEach(lieu => {
                        // Création du marqueur
                        var marker = L.marker([lieu.lat, lieu.lng]).addTo(map);
                        
                        // Ajout de la bulle d'info
                        marker.bindPopup(
                            "<b>" + lieu.nom + "</b><br>" +
                            "Nombre d'adresses MAC : " + lieu.nb_mac
                        );
                    });
                })
                .catch(err => console.error("Erreur:", err));
        </script>
    </body>
    </html>
    """
    return html_content