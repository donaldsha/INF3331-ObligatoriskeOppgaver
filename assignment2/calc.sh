#!/bin/bash
#calc.sh

r=$@

num=${r[1]}
multi=1

if [[ "$1" == "S" ]]; then #finds the sum
	for i do
	(( sum+=$i ))
done
echo $sum


elif [[ "$1" == "P" ]]; then #finds multiplication  
	shift;
	for i do
		let multi=$multi*$i
done
echo $multi

elif [[ "$1" == "M" ]]; then #Finds the maximum
	for i do
		if [[ "$i" -gt "$num" ]]; then
			num=$i
		fi
	done
	echo $num

elif [[ "$1" == "m" ]]; then #Finds the minimum
	shift;
	min=$2
		for i do
			if [[ $i -lt $min ]]; then
				min=$i
			fi
		done
	echo $min

else
	echo "No valid command given. Write a valid command"
fi
