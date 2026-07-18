from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import sklearn
import numpy as np
from datetime import datetime

app = FastAPI(debug=True,
              title="API de prédiction pluie",
              description="Api simple pour exposer deux modèles : un classifieur pour déterminer si il va pleuvoir, un régresseur pour déterminer la quantité de pluie",
              version="1.0"
              )

#Chargement des modèles au démarrage
try:
    clf = joblib.load('modele_classification.joblib')
    reg = joblib.load('modele_regression.joblib')
    print("Modèles chargés avec succès")
except Exception as e :
    print (f"erreur lors du chargement des modèles : {e}")

class DonneesModele(BaseModel):
    temperature: float
    humidite: int
    pression_mer:int
    variation_pression_3:int
    vitesse_vent:float
    neboliste:float
    month:int
    hour:int

@app.post("/predire/pluie")
def predirePluie(data : DonneesModele):
    if clf is None:
        raise Exception("Modèle de classification indisponible")

    features= np.array([[data.temperature,data.humidite,data.pression_mer,data.variation_pression_3,data.vitesse_vent,data.neboliste,data.month,data.hour]])
    prediction = clf.predict(features)
    if prediction == 1:
        return {"prediction : il va pleuvoir" :  prediction[0].item()}
    else:
        return "prediction : il ne va pas pleuvoir"

@app.post("/predire/quantite")
def predireQuantite(data : DonneesModele):
    if reg is None:
        raise Exception("Modèle de regression indisponible")
    features = np.array(
        [[data.temperature, data.humidite, data.pression_mer, data.variation_pression_3, data.vitesse_vent,
          data.neboliste, data.month, data.hour]])
    prediction = clf.predict(features)
    return f"Il devrait pleuvoir {prediction} mL d'eau"