#!/bin/bash

# NOTE
# address have to have 'application' and 'content' name at the end
# eg. rtmp://localhost:9991/live/test01
# iy you see 'INFO: connected' that means rtmp server is working

if [ "$#" -ne "1" ]
then
	echo "You have to specify rtmp server address as the only argument."

	exit 1
fi

rtmpdump -r $1
