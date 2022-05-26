#!/bin/bash

FULL_PATH="./some/path/some_file.txt.tar"
echo "Full path: $FULL_PATH"

FILE_NAME=$(basename ${FULL_PATH})

echo "Just a name: $FILE_NAME"

echo "Just some parts of it ... "

echo "${FILE_NAME%%.*}"
echo "${FILE_NAME%.*}"

echo "${FILE_NAME#*.}"
echo "${FILE_NAME##*.}"

