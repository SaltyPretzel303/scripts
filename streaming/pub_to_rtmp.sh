#!/bin/bash

src_file=$1
rtmp_server=$2
loop_option=$3

ffmpeg -re -stream_loop $loop_option -i $src_file -c copy -f flv $rtmp_server
