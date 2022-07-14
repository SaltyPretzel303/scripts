#!/usr/bin/python3.8

import argparse
import os
from os.path import exists
import youtube_dl
import sys

# NOTE 
# after all this script is actyally useless
# instead of youtube_dl you should use yt_dlp (the main reason is that max download
# speed is gonna be aroung 17Kb/s or somehing very slow)
# to download video just use 
# yt-dlp --no-playlist https://youtube...videhash
# or just follow the docs for more options 

LINKS_LIST = "./link_list"
DOWNLOAD_DIR = "./new"

# setup cli arguments parser

parser = argparse.ArgumentParser(
    f"Downloads songs from youtube links specified as lines of file. \n\
    Default links list is {LINKS_LIST} file.\n\
    Defualt destination dir of downloaded content is {DOWNLOAD_DIR} .\n")

parser.add_argument("--links",
                    dest="links_list",
                    required=False,
                    help="Specifies file in which youtube links are stored. ")

cli_input = parser.parse_args()

# check are any arguments passed 

if(hasattr(cli_input, "links_list") and 
        (cli_input.links_list is not None) and (cli_input.links_list != "")):

    links_list = cli_input.links_list
    
else:
    links_list = LINKS_LIST


print(f"Using links from the path: {links_list} ... ")

# download specified links

if not exists(links_list):
    print("File: " + links_list + " does not exists. ")
    sys.exit(1)

links_file = open(links_list)
links = links_file.readlines()

options = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'noplaylist': 'True',
    'rmcachedir':'True'
}


with youtube_dl.YoutubeDL(options) as ydl:
    ydl.download(links)

os.system('find ./ -maxdepth 1 -iname "*.mp3" -exec mv -t ./old {} +')
