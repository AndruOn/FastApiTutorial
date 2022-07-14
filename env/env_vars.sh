#!/bin/sh

filename="env_variables.txt"

while read line; do
# reading each line
conda env config vars set $line
echo $line
done < $filename