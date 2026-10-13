Commencer un projet !

1. cree un dossier dans un root exemple : mkdir mon_app
2. Connecter le projet a github.(si besoin)
3. Cree le fichier .gitignore

4. Cree un dossier app avec le contenu de base : 
app/
├── __init__.py        # create_app() (factory)
├── config.py
├── extensions.py      # db, migrate, login_manager...
├── models/
├── routes/            # Blueprints (= tes controllers)
├── services/
├── schemas/           # Marshmallow / Pydantic
├── utils/
└── middlewares.py     # ou before_request / after_request
tests/
.env
.gitignore
requirements.txt
run.py

5. faire le venv : python3 -m venv .venv
6. activer le venv source .venv/bin/activate
7. installer flask : pip install flask