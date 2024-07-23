#!/bin/bash 

Executable="$1"
ExecutableBase="$(basename "$Executable")"
Usage="\
Usage: $(basename $0) command
E.g.:  $(basename $0) google-chrome\
"

############## USGCHECKS #################

if [[ $# -ne 1 || "$1" =~ ^(-h|--help)$ ]]; then
  echo "$Usage"
  exit 1
fi

################ MAIN ####################

# the most recently accessed window on this desktop/session
current_desktop="$(xdotool get_desktop)"
MostRecentWID="$(xdotool search --class --desktop "$current_desktop" --name "$ExecutableBase" | tail -1 2> /dev/null)"

if [[ -z "$MostRecentWID" ]]; then
	echo "$ExecutableBase not found in this session, will search in all."
	MostRecentWID="$(xdotool search --class --name "$ExecutableBase" | tail -1 2> /dev/null)"
fi 

if [[ -z "$MostRecentWID" ]]; then
	echo "$ExecutableBase not found. Launching new window."
  	"$Executable" > /dev/null 2>&1 &
  	disown
else
  echo "Focusing existing instance of $ExecutableBase."
  # use brute-force approach if activating most recent WID doesn't work
  xdotool windowactivate "$MostRecentWID" 2>&1 | grep failed \
  && xdotool search --class --name "$ExecutableBase" windowactivate 
fi