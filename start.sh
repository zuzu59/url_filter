#!/bin/bash

echo -e " 
Afin de garder le proxy WEB permanent, il serait bien de le faire tourner dans un 'screen' avec:
screen -S testwwp     pour entrer dans screen
./web_server.sh       pour lancer le serveur WEB dans screen
CTRL+a,d              pour sortir de screen en laissant tourner le serveur
screen -r testwwp     pour revenir dans screen
CTRL+d                pour terminer screen
screen -list          pour lister tous les screen en fonctionement
"

MAX_RAM=600

while [ 1 ];
do 

# Si mitmdump n'est pas lancé
if ! pgrep mitmdump > /dev/null
then
    mitmdump -s ./filter.py & 
    echo Mitmdump launched
else 
    MEM_USED=$(free -h | grep Mem | awk '{print $2}' | awk '{print substr($1, 1, length($1)-1)}')
    MEM_USED=$(($MEM_USED+0))
    if [[ $MEM_USED > $MAX_RAM  ]] 
    then
        pkill $(pgrep mitmdump)
        echo Mitmdump killed
    fi
fi
sleep 1
done



