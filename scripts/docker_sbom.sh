#!/bin/bash
file='../search/above2star/uniqueSearchFrom1to3.csv'
file='uniqueSearchFrom1to3.csv'
rows=1
error="errors.csv"
while IFS="," read -r  name x y z 
do
	output='./data/'$rows'_'$name
	echo $name
	echo $output
	(((docker sbom $name)>>$output)&&(docker image rm $name))||($rows>>$error)
	rows=$(($rows + 1))
done < $file