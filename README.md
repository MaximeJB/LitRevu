# LITRevu - Plateforme de Critiques Littéraires

LITRevu est une application web développée avec Django qui permet à une communauté d'utilisateurs de publier des critiques de livres ou d'articles, de consulter des critiques existantes et de solliciter des critiques à la demande.

## 🚀 Fonctionnalités

L'application permet de :
- **Demander des critiques** de livres ou d'articles, en créant un billet
- **Lire des critiques** de livres ou d'articles 
- **Publier des critiques** de livres ou d'articles

### Les billets
Un billet correspond à une demande de critique de la part d'un utilisateur. Il rédige son billet en demandant une critique pour un livre ou un article de littérature. Les utilisateurs qui suivent l'utilisateur connecté peuvent poster des critiques en réponse à un billet. Il est possible de créer un billet et une critique pour ce billet en même temps.

### Le flux
Le flux affiche les billets et avis de tous les utilisateurs suivis, les billets et avis de l'utilisateur connecté, et les avis en réponse aux billets de l'utilisateur connecté. Le flux est ordonné par ordre antéchronologique (les plus récents en premier).

## 🛠️ Technologies utilisées

- **Framework** : Django
- **Base de données** : SQLite
- **Frontend** : HTML, CSS, JavaScript
- **Accessibilité** : Conforme aux directives WCAG

## 📋 Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)
- Git

## 🔧 Installation et configuration

### 1. Cloner le repository

```bash
git clone https://github.com/votre-username/litrevu.git
cd litrevu
```

### 2. Créer un environnement virtuel

```bash
# Sur Windows
python -m venv venv
venv\Scripts\activate

# Sur macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Configurer la base de données

```bash
# Appliquer les migrations
python manage.py migrate

# Créer un superutilisateur (optionnel)
python manage.py createsuperuser
```

### 5. Charger les données de test

```bash
# Charger les fixtures avec des données de démonstration
python manage.py loaddata fixtures/sample_data.json
```

### 6. Lancer le serveur de développement

```bash
python manage.py runserver
```

L'application sera accessible à l'adresse : `http://127.0.0.1:8000/`

## 📱 Structure de l'application

```
litrevu/
├── litrevu/          # Configuration principale du projet
├── Comment/          # App de gestion des utilisateurs
├── Review /          # App principale (billets et critiques)
├── UserCustom /      # Modèle utilisateur personnalisé 
├── UserFollows /     # Logique du following
├── Tickets /         # Modèle des demandes de critique
├── static/           # Fichiers statiques (CSS, JS, images)
├── templates/        # Templates HTML
├── db.sqlite3        # Base de données SQLite
├── requirements.txt  # Dépendances Python
└── README.md         # Documentation
```

## 🎨 Interface utilisateur

L'interface respecte les wireframes fournis avec :
- Navigation intuitive
- Respect des standards WCAG pour l'accessibilité
- Interface épurée et moderne

## 📝 Développement

### Standards de code
- Respect de la PEP 8
- Documentation des fonctions complexes
- Noms de variables explicites
- Séparation des préoccupations

## 📄 License

Ce projet est développé dans le cadre d'un exercice de formation et n'est pas destiné à un usage commercial.

---
