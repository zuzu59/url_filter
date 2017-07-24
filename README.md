# url_filter

Petit proxy permettant la manipulation du dom d'une page WEB.

Très pratique quand on veut, lors d'une migartion de sites, les 'nettoyer' pour une comparaison visuelle plus facile en attendant d'avoir corrigé tous les bugs de la migration.

# Installation

Ce logiciel necessite l'utilisation de python 3.

Pour installer url_filter, il suffit de runner
`./install.sh`

# Utilisation
`/.start.sh proxy.sh ram_maximale`

Ce script va lancer le proxy. Le paramètre ram_maximale (en mégabyte) permet de stopper le proxy si la ram consommée par toutes la machine dépasse cette valeur. Il faut ensuite mettre l'adresse de la machine et le port 8080 dans les paramètres proxy du navigateur web. 

Pour Firefox, il faut aller dans les paramètres avancés dans l'onglet "Réseau" puis les paramètres de la connexion. Dans la fenêtre qui s'ouvre, il faut choisir la configuration manuelle du proxy puis introduire l'adresse du proxy dans le champ "HTTP Proxy" et le port 8080 et cocher la case pour utiliser ce serveur proxy pour tous les protocoles puis appuyer sur OK.

Ensuite, il faut installer un certificat pour que les connexions en HTTPs marchent. Pour cela, une fois que le proxy est configuré dans le navigateur, il faut aller [ici](http://mitm.it), choisir "Other" puis chosir de confirmer l'AC pour identifier les sites web.

# References:

https://mitmproxy.org/

http://docs.mitmproxy.org/en/stable/

https://github.com/mitmproxy/mitmproxy/tree/2.0.x/examples

https://pypi.python.org/pypi/mitmproxy





