#!/bin/bash

# Teste si les arguments sont bien passés 
if (( $# < 2 ))
then
    echo "Erreur: pas assez d'arguments
    usage: ./start.sh fichier_du_script quantité_de_RAM_maximale"
    exit
fi

# Teste si fichier existe
if [ -e "$1" ]
then
    CMD=$(sed -n 2p $1)
    echo $CMD
    CMD_NAME=$(echo $CMD | awk '{print $1}')
    echo $CMD_NAME
else
    echo Pas de fichier $1 
    exit
fi

MAX_RAM=$2

echo -e " 
Afin de garder le proxy WEB permanent, il serait bien de le faire tourner dans un 'screen' avec:
screen -S testwwp     pour entrer dans screen
./web_server.sh       pour lancer le serveur WEB dans screen
CTRL+a,d              pour sortir de screen en laissant tourner le serveur
screen -r testwwp     pour revenir dans screen
CTRL+d                pour terminer screen
screen -list          pour lister tous les screen en fonctionement
"

function finish () {
    kill -9 $(pgrep $CMD_NAME) > /dev/null
    echo "Arrêt"
    exit
}

trap finish INT

while [ 1 ];
do 

# Si mitmdump n'est pas lancé
if ! pgrep $CMD_NAME > /dev/null
then
    $CMD &
    echo "Mitmdump allumé"
fi 

sleep 1
if ! pgrep $CMD_NAME > /dev/null
then
    echo "Erreur: Mitmdump n'a pas pu être lancé"
    break
fi 
MEM_USED=$(free -h | grep Mem | awk '{print $3}' | awk '{print substr($1, 1, length($1)-1)}')
MEM_USED=$(($MEM_USED+0))
# Si la mémoire max est dépassée
if (( $MEM_USED > $MAX_RAM ))
then
    kill -9 $(pgrep $CMD_NAME) > /dev/null
    echo "Mitmdump arrêté"
fi
sleep 1
done
done

