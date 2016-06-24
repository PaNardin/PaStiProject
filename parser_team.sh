#!/bin/sh
#
# This script runs all Gnuplot scripts in the current directory.
#

files=`ls |grep '.csv'`

for file in $files ; do
	echo "Parsing " $file
	sed -i 's/Gardiens: //g' $file # Supprimer les chaines de caractères
	sed -i 's/Défenseurs: //g' $file
	sed -i 's/Milieux: //g' $file
	sed -i 's/Attaquants: //g' $file
	sed -i 's/([^)]*)//g' $file # Effacer le texte entre parenthèses
	sed -i -e "s/, /\n/g" $file # Remplacer virgules par retour à la ligne
	sed -i '/^$/d' $file # Suppression lignes vides
done

exit 0