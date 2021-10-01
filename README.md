# LITReview
#### LITReview est site qui permet a leurs utilisateur de poster ou de demander des critiques pour des livres.

## Activer l'environnement virtuel

Sous Windows, ouvrez votre shell, placez vous dans le dossier LITReview et tapez : 
`venv/scripts/activate`  

Sous Linux, ouvrez votre shell, placez vous dans le dossier LITReview et tapez : 
`source venv/bin/activate`  

### Installer les librairies nécessaire au projet

Une fois l'environnement virtuel activé, tapez :
`pip install -r requirements.txt`  

### Création d'un compte admin 
Pour créer un utilisateur admin tapez :
`python3 manage.py createsuperuser`  

Suivez les instructions, gardez en tête que lors de la saisie du mot de passe le champ reste vide mais les inputs sont bien saisis.

### Démarrer le serveur

Pour démarrer le serveur tapez :             
`python3 manage.py runserver`  

### Se rendre sur le site

Pour vous rendre sur le site, ouvrez un navigateur et dans l'url saisissez :
`127.0.0.1:8000`  

###  Création d'un utilisateur 
Pour créer un simple utilisateur suivez les instructions sur la page de connexion.
