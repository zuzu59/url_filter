# url_filter
Petit proxy qui permet d'enlever ou d'ajouter des 'choses' sur des pages WEB !

Très pratique quand on veut, lors d'une migartion de sites, les 'nettoyer' pour une comparaison visuelle plus facile en attendant d'avoir corrigé tous les bugs de la migration.

# Installation
`./install.sh`

# Utilisation
`/.start.sh`

Ce script va lancer le proxy. Il faut ensuite mettre l'addresse de la machine et le port 8080 dans les paramètres proxy du navigateur web. 

Pour Firefox, il faut aller dans les paramètres avancés dans l'onglet "Réseau" puis les paramètres de la connexion. Dans la fenêtre qui s'ouvre, il faut choisir la configuration manuelle du proxy puis introduire l'adresse du proxy dans le champ "HTTP Proxy" et le port 8080 et cocher la case pour utiliser ce serveur proxy pour tous les protocoles puis appuyer sur OK.

# Sources:

https://mitmproxy.org/

http://docs.mitmproxy.org/en/stable/

https://github.com/mitmproxy/mitmproxy/tree/2.0.x/examples

https://pypi.python.org/pypi/mitmproxy





