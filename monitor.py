import requests
from dotenv import load_dotenv
import os


load_dotenv()

# Récupération des variables url et key via le fichier .env
url = os.getenv('URL')
key = os.getenv('API_KEY')


# Préparation de l'entête de la clé API
headers = {
    "Authorization": f"Bearer {key}"
}

# Préparation de la réponse du serveur 
response = requests.get(url,headers=headers)

if response.status_code == 200:
    data = response.json()

    print(data)

else:
    print('Erreur de connexion')
