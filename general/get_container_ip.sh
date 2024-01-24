#!/bin/bash

with_name='{{.Name}}:  '

name_arg=''
all_flag='-a'

all_names=

function chec_all_flag {
	for arg in $@
	do 
		if [[ "$arg" == "$all_flag" ]]
		then 
			name_arg=$with_name
			return
		fi 
	done 
}

chec_all_flag $@

# -t check if current input is terminal.
# if ! -t there is input piped from other command. 
if [ ! -t 0 ]
then 

	while read line
	do
		all_names+=" $line"
	done 

	# This should replace the above alg but not sure how it (dosn't) works.
	# readarray -t read_names
fi

all_names+=" $@"

for c_name in $all_names
do
	if [[ "$c_name" == "$all_flag" ]]
	then 
		continue
	fi

	docker inspect "$c_name" --format "$name_arg{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}"
done