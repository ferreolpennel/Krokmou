# Krokmou

Ce projet porte sur l'AR Drone 2.0 de Parrot. Le but étant de faire un état des lieux des différentes menaces et vulnérabilités présentes sur ce modèle de drone.

# Prérequis:
  - Cette petite application nécessitent des outils tels que la suite aircrack-ng et de nombreuses librairies python3
  - Afin de controller le drone via votre ordinateur, veuillez récupérer le dépot suivant et le cloner dans la racine du répertoire de Krokmou:
  
       https://github.com/functino/drone-browser.git
       
# Installation:
    $ git clone https://github.com/ferreolpennel/Krokmou.git
    $ cd Krokmou
    $ git clone https://github.com/functino/drone-browser.git
    $ cd drone-browser
    $ npm install -d
    $ cd ../
    $ pip3 install -r requirements.txt
    $ chmod+x swiss_knife
  
  
# Lancement de Krokmou

Simplement lancer le programme python swiss_knife avec les droits root:

    $ sudo ./swiss_knife 
   
 
