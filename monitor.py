import requests
from dotenv import load_dotenv
import os
import logging
import json
import mysql.connector
from mysql.connector import Error

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,  # Niveau de log (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='logs/app.log',  # Fichier de log
    filemode='a'         # 'a' pour ajouter, 'w' pour écraser à chaque exécution
)




# Connexion à la base de données MySQL
try:
    connection = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
    )

    if connection.is_connected():
        logging.info("Connexion à la base de données MySQL réussie.")
        cursor = connection.cursor()
        print('Connexion à la base de données MySQL réussie.')

except Error as e:
    logging.error(f"Erreur lors de la connexion à MySQL : {e}")
    print(f"Erreur lors de la connexion à MySQL : {e}")
    exit(1)





# Récupperation des variables d'environnement
load_dotenv()

url = os.getenv('URL')
key = os.getenv('API_KEY')




# Vérification des variables d'environnement
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

    if response.status_code == 200:
        data = response.json()
        logging.info("Succès de la réponse du serveur API")
        print('Succès de la réponse du serveur API')




    
# Création du dossier pour l'enregistrement des données au format json (s'il n'existe pas)
    os.makedirs("repports", exist_ok=True)




    # Enregistrement des données dans un fichier JSON
    with open("repports/data_repport.json", "a", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    logging.info("Données enregistrées dans repports/data_repport.json")
    print("Données enregistrées avec succès.")



except requests.exceptions.HTTPError as http_err: # Erreur de type http
    logging.error(f"Erreur http : {http_err}")
    print(f"Erreur http : {http_err}")

except requests.exceptions.RequestException as err:
    logging.error(f'Erreur de connexion : {err}')
    print(f'Erreur de connexion : {err}')

except Exception as e:
    logging.critical(f'Erreur inconnue : {e}')
    print(f'Erreur inconnue : {e}')



