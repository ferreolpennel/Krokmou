# Krokmou

Ce projet porte sur l'AR Drone 2.0 de Parrot. Le but étant de faire un état des lieux des différentes menaces et vulnérabilités présentes sur ce modèle de drone.

# Prérequis:
  - Cette petite application nécessitent des outils tels que la suite aircrack-ng et de nombreuses librairies python3
  - Afin de contrôler le drone via votre ordinateur, veuillez récupérer le dépot suivant et le cloner dans la racine du répertoire de Krokmou:

       https://github.com/functino/drone-browser.git

# Installation:
Installation rapide via cette ligne d ecommande à copier dans le terminal.

    git clone https://github.com/ferreolpennel/Krokmou.git && cd Krokmou &&
    git clone https://github.com/functino/drone-browser.git && cd drone-browser && npm install -d &&
    cd ../ && chmod +x krokmou.py


# Lancement de Krokmou

Simplement lancer le programme python krokmou.py avec les droits root:

    $ sudo ./krokmou.py
