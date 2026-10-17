# Portfolio d'Abdou Salifou

Portfolio responsive réalisé avec Python, Flask, Jinja2, HTML, CSS et JavaScript.
Les coordonnées sont centralisées dans `portfolio_data.py`. Les projets et les
technologies non confirmés sont explicitement présentés comme tels.

## Prérequis

- Windows 11 et Python 3.10 ou plus récent (`py --version`)
- Une connexion Internet pour installer les dépendances et charger les polices

## Installation et lancement sous PowerShell

Depuis le dossier `portofolio` :

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

Ouvrir ensuite <http://127.0.0.1:5000>.

Si PowerShell bloque l'activation, autoriser uniquement les scripts pour le
terminal courant avec la commande suivante, puis relancer la commande
d'activation :

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Cette modification ne persiste pas après la fermeture du terminal. Autre
possibilité : utiliser l'invite de commandes Windows avec
`.venv\Scripts\activate.bat`.

## Tests

```powershell
python -m pytest
```

Les tests couvrent la page d'accueil, les sections et coordonnées, les pages de
détail et d'erreur, les fichiers statiques et l'absence ou la présence du CV.
Les tests serveur ne remplacent pas une vérification visuelle sur différents
appareils. Pour vérifier manuellement le rendu mobile, réduire la largeur de la
fenêtre ou utiliser le mode appareil des outils de développement du navigateur.

## Personnalisation

- Modifiez les coordonnées, la formation, les pistes de compétences et les
  informations projets dans `portfolio_data.py`.
- Une compétence ou une technologie reste une « piste à confirmer » tant que
  son niveau ou son utilisation n'a pas été confirmé.
- Ajoutez votre photo dans `static/images/`, puis remplacez l'emplacement
  réservé dans `templates/index.html` par la photo et un texte alternatif exact.
- Ajoutez votre CV sous `static/files/cv-abdou-salifou.pdf` pour faire apparaître
  automatiquement les liens de téléchargement. Vérifiez son contenu avant de
  l'ajouter au dépôt : le PDF sera accessible publiquement avec le site.
- Pour modifier le statut d'un projet, réglez son champ `status` dans
  `portfolio_data.py` sur `En conception`, `En développement` ou `Terminé`
  uniquement lorsque cette information est confirmée.
- Aucun formulaire ne simule l'envoi d'un message : le lien e-mail ouvre le
  logiciel de messagerie du visiteur.

## Déploiement

L'application est compatible avec un hébergeur Python/WSGI et inclut Waitress.
Pour la publier avec Render (après création et connexion d'un dépôt GitHub) :

1. Créez un nouveau **Web Service** depuis votre dépôt GitHub.
2. Choisissez Python comme environnement.
3. Commande de construction : `pip install -r requirements.txt`.
4. Commande de démarrage : `waitress-serve --listen=0.0.0.0:$PORT app:app`.
5. Ne choisissez un plan payant qu'après avoir vérifié et accepté son tarif.
   La disponibilité et les limites des offres gratuites peuvent changer selon
   l'hébergeur.
6. Une fois la publication terminée, vérifiez la page d'accueil, les pages
   projets et les liens de contact sur l'URL fournie par l'hébergeur.

Ne publiez pas de fichier `.env`, de secret ou de CV sans avoir vérifié le
contenu. Le lancement local et les tests ne publient pas le site.
