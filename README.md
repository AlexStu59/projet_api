


```markdown
# API Data Monitor

## 📝 Description

Ce projet Python interroge une API REST, enregistre les données reçues dans un fichier JSON, puis les insère dans une base de données MySQL. Il est conçu pour surveiller l'état d'une application ou d'un service via une API exposant des informations telles que le nom de l'application, son statut, le temps de réponse et un horodatage.

## ⚙️ Fonctionnalités

- Requête GET vers une API sécurisée par clé.
- Enregistrement des réponses dans un fichier `repports/data_repport.json`.
- Insertion des données dans une base MySQL (`app_status`).
- Journalisation des événements dans `logs/app.log`.

## 📦 Prérequis

- Python 3.8+
- MySQL Server
- Un environnement virtuel (optionnel mais recommandé)

## 📁 Installation

```bash
git clone https://github.com/votre-utilisateur/api-data-monitor.git
cd api-data-monitor
python -m venv venv
source venv/bin/activate  # ou venv\\Scripts\\activate sous Windows
pip install -r requirements.txt
```

## 🔐 Configuration

Créez un fichier `.env` à la racine du projet avec les variables suivantes :

```env
URL=http://127.0.0.1:8000/status
API_KEY=your_api_key_here

DB_HOST=localhost
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_NAME=your_db_name
```

## 🧪 Utilisation

Lancez le script principal :

```bash
python monitor.py
```

Le script :
- interroge l'API,
- enregistre la réponse dans un fichier JSON,
- insère les données dans la base de données MySQL.

## 🗃️ Structure de la base de données

```sql
CREATE TABLE app_status (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME,
    app_name VARCHAR(255) NOT NULL,
    status VARCHAR(100)
);
```

## 🪵 Logs

Tous les événements sont enregistrés dans `logs/app.log`. Cela inclut :
- les connexions réussies ou échouées à la base de données,
- les erreurs HTTP,
- les insertions SQL.

## 🤝 Contribuer

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou une pull request.

## 📄 Licence

Ce projet est sous licence MIT.
```