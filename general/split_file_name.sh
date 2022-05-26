#!/bin/bash

FILE_NAME="some_file.txt.tar"

echo "${FILE_NAME%%.*}"
echo "${FILE_NAME%.*}"

echo "${FILE_NAME#*.}"
echo "${FILE_NAME##*.}"
