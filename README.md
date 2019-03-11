# Krokmou

Ce projet porte sur l'AR Drone 2.0 de Parrot. Le but étant de faire un état des lieux des différentes menaces et vulnérabilités présentes sur ce modèle de drone. Le rendu final est une petite application regroupant les différentes attaques que nous avons étudiées et mises en oeuvre durant ce projet. Nous ne sommes pas responsable de l'utilisation que vous ferez de cette application.

# Prérequis:
  - Cette petite application nécessitent des outils tels que la suite aircrack-ng et de nombreuses librairies python3     
  - Il est donc nécessaire d'installer le paquet npm et le paquet aircrack-ng:
       
        $sudo apt install npm aircrack-ng

# Installation:
Installation rapide via cette ligne de commande à copier dans le terminal.

    git clone https://github.com/ferreolpennel/Krokmou.git && cd Krokmou && 
    git clone https://github.com/functino/drone-browser.git && cd drone-browser && npm install -d &&
    cd ../


# Lancement de Krokmou

Simplement lancer le programme python krokmou.py avec les droits root:

    $ sudo ./krokmou.py

Si certaines dépendances python ne sont pas validées, leurs installation se fait par le fichier requierements.txt
    
    $ pip3 insatall -r requierements.txt
