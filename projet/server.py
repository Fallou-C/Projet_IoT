from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi.responses import HTMLResponse
import base_de_donnee
from base_de_donnee import prevision_emplacement

app = FastAPI()

# 1. Création du modèle de données (Pydantic)
# Cela valide que l'entrée correspond exactement à ton JSON
class MacInput(BaseModel):
    macAddresses: List[List[int]] # Liste de listes d'entiers
    taille: int
    

# stocker en memoire les points calculés
coordonnee_liste = []

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

    #On compare les adresses reçues avec celles de la base de donnéees et on calcule les coordonnées moyennes

    # 3. Stockage des données
    # On ajoute les nouvelles adresses à notre liste globale
    coordonnee_liste.extend(prevision_emplacement(data.macAddresses))
    
	#on supprime les premières si y'en a trop
    while(len(coordonnee_liste) > 50):
        coordonnee_liste.pop(0)

    return {
        "message": "Calcul terminé",
        "points_ajoutés": coordonnee_liste[len(coordonnee_liste)],
        "total_en_mémoire": len(coordonnee_liste)
    }

@app.get("/voir-points")
async def get_stored():
    """Endpoint pour vérifier ce qui a été stocké"""
    return {"database": coordonnee_liste}

@app.get("/api/points")
async def api_points():
    # On appelle la fonction qui lit votre liste donnee_gps
    data = base_de_donnee.get_coordonnees()
    return data

@app.get("/api/coordonnee")
async def get_coordonne():
    resultats = []
    i = 0
    for i in range(len(coordonnee_liste)//2):
        # On crée un dictionnaire simple pour l'API
        infos = {
            "nom": i,
            "lat": coordonnee_liste[i*2],
            "lng": coordonnee_liste[i*2+1],
        }
        resultats.append(infos)
    return {"database": resultats}

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
            // 1. Initialisation de la carte
            var map = L.map('map').setView([48.845, 2.356], 16);

            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                attribution: '&copy; OpenStreetMap'
            }).addTo(map);

            // ---------------------------------------------------------
            // 2. Chargement des POINTS DE LA BASE DE DONNÉES (Bleus)
            // ---------------------------------------------------------
            fetch('/api/points')
                .then(response => response.json())
                .then(data => {
                    data.forEach(lieu => {
                        // Marqueur standard (BLEU par défaut)
                        var marker = L.marker([lieu.lat, lieu.lng]).addTo(map);
                        marker.bindPopup(
                            "<b>BASE DE DONNÉE: " + lieu.nom + "</b><br>" +
                            "Nombre MAC: " + lieu.nb_mac
                        );
                    });
                })
                .catch(err => console.error("Erreur BDD:", err));

            // ---------------------------------------------------------
            // 3. Chargement des POINTS CALCULÉS / DYNAMIQUES (Rouges)
            // ---------------------------------------------------------
            fetch('/api/coordonnee')
                .then(response => response.json())
                .then(data => {
                    // data.database contient votre liste coordonnee_liste
                    var points = data.database;

                    // On utilise 'index' pour récupérer le numéro dans la liste (0, 1, 2...)
                    points.forEach((point, index) => {
                        
                        // Création d'un point ROUGE (CircleMarker)
                        var redDot = L.circleMarker([point.lat, point.lng], {
                            color: 'red',       // Contour rouge
                            fillColor: '#f03',  // Remplissage rouge vif
                            fillOpacity: 0.8,
                            radius: 10          // Taille du point
                        }).addTo(map);

                        // Popup avec l'indice du point
                        redDot.bindPopup(
                            "<b> Coordonée </b><br>" +
                            "Point numéro : " + (index + 1)
                        );
                    });
                })
                .catch(err => console.error("Erreur Points Calculés:", err));

        </script>
    </body>
    </html>
    """
    return html_content