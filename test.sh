#!/bin/bash

# Set version
VERSION=$1
shift

if [ -d "/home/students/tirissou/trainedModel/v$VERSION" ]; then
	echo "Version $VERSION already exists. Please choose another version"
	exit 1
else 
	mkdir /home/students/tirissou/trainedModel/v$VERSION
fi  

# Iterate through all games
while test $# -gt 0
do 
	GAME=$1
	# Make necessary directories
	P=/home/students/tirissou/trainedModel/v$VERSION/$GAME
	mkdir $P
	for NETWORK in $(find ./ -maxdepth 1 -name "*trainer.py")
	do
		NETNAME=$(basename $NETWORK .py)
		nP=$P/$NETNAME
		mkdir $nP
		np=$nP/
		# Make the scripts
		cp ./template.pbs ./v$VERSION-$GAME.pbs
		echo "python3 $(pwd)/$(basename $NETWORK) --myversion $VERSION --env-name $GAME --path $nP > $nP/stdout.txt" >> ./v$VERSION-$GAME-$NETNAME.pbs
		qsub ./v$VERSION-$GAME-$NETNAME.pbs -o $nP/log.txt -e $nP/err.txt
		# rm ./v$VERSION-$GAME.pbs
	done
	shift 
done
