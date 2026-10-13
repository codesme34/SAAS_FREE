Commencer un projet !

1. cree un dossier dans un root exemple : mkdir mon_app
2. le connecter a github : "git init -b main" ensuite "git remote add origin https://github.com/votre nom utilisateur/(votre depot).git"
lancer le premier commit:

git add .
git commit -m "Initial commit"
git push -u origin main


3. faire le venv : python3 -m venv .venv
4. activer le venv source .venv/bin/activate
5. cree un dossier app avec le contenu de base : 
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
requirements.txt
run.py


6. installer flask : pip install flask