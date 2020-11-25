#!/bin/bash

if [ "$#" -ne "2" ]
then
	echo "This script requires two arguments in this exact order"
	echo "1. tcp server address"
	echo "2. port on which server is listening"
	echo "e.g. ./test_tcp.sh 172.17.0.1 9991"
	
	exit 1
fi

server_address=$1
server_port=$2

nc -z -v -w5 $server_address $server_port
