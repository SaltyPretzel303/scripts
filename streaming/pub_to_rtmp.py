#!/usr/bin/python3

import subprocess
import argparse

parser = argparse.ArgumentParser("Publish specified video file to specified rtmp server.")

parser.add_argument("--src_file",
                    dest="src_file",
                    required=True,
                    help="Video file to stream. ")

parser.add_argument("--server_addr",
                    dest="server_addr",
                    required=True,
                    help="Rtmp server address. ")

parser.add_argument("--loop",
                    dest="loop_flag",
                    default="0",
                    action="store_const",
                    const="-1",
                    required=False,
                    help="If specified ffmpeg will loop this video after its end. ")

cli_input = parser.parse_args()

# loop_flag: 0     -> don't loop (exit after whole file is streamed/sent)
# loop_flag: n     -> loop src_file n-times (not used by this script)
# lopp_flag: -1    -> loop src_file forever

print ("Loop flag value: " + cli_input.loop_flag)

subprocess.call(['sh', 
                './pub_to_rtmp.sh',
                cli_input.src_file,
                cli_input.server_addr,
                cli_input.loop_flag])
