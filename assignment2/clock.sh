#!/bin/bash
#clock.sh

	function quit 
{
	exit #function used to exit if wrong imput parameter given
}

if [[ $1 == "no" ]]; then
	export TZ=Europe/Oslo 
	
elif [[ $1 == "sk" ]]; then
	export TZ=Asia/Seul
		
elif [[ $1 == "us" ]]; then
	export TZ=America/New_York

else
	echo "Choose a correct time zone, whether no, sk, us"
	quit

fi
	count=1
	for (( i = 0; i < count; i++ )); do
		sleep 1
		clear
		date +"%T"

		count=$((count+count))
	done

