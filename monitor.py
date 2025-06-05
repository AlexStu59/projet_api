import requests
from dotenv import load_dotenv
import os
import logging



# Configuration du logging
logging.basicConfig(
    level=logging.INFO,  # Niveau de log (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='logs/app.log',  # Fichier de log
    filemode='a'         # 'a' pour ajouter, 'w' pour écraser à chaque exécution
)



# Récupperation des variables d'environnement
load_dotenv()

url = os.getenv('URL')
key = os.getenv('API_KEY')




# Vérification des variables
if not url or not key:
    logging.error("URL ou API_KEY manquante dans le fichier .env")
    exit(1)




# Préparation de l'entête de la clé API
headers = {
    "Authorization": f"Bearer {key}"
}




# Envoi de la requête au serveur API
try:
    logging.info(f"Envoi de la requête GET au serveur {url}")
    response = requests.get(url,headers=headers)
    response.raise_for_status()  # Lève une exception pour les codes d'erreur HTTP

    response.status_code == 200
    data = response.json()
    logging.info("Réponse reçue avec succès")

    print(data)

except requests.exceptions.HTTPError as http_err: # Erreur de type http
    logging.error(f"Erreur http : {http_err}")
    print(f"Erreur http : {http_err}")

except requests.exceptions.RequestException as err:
    logging.error(f'Erreur de connexion : {err}')
    print(f'Erreur de connexion : {err}')

except Exception as e:
    logging.critical(f'Erreur inconnue : {e}')
    print(f'Erreur inconnue : {e}')