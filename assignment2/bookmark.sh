#!/bin/bash

args=("$@")

if [[ "$1" == "-a" ]]; then
	$bmark="$2"
	echo "$bmark|$PWD" >> $HOME/.bookmarks

elif [[ "$1" == "-r" ]]; then
	echo $(grep -v "$bmark|" $HOME/.bookmarks) > $HOME/.bookmarks

else 
	echo "Wrong input. Write -a or -r"
fi

while IFS="|" read var1 value; do

	export var1=value

done < $HOME/.bookmarks