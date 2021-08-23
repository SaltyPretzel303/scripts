#!/bin/bash

# to find out bus and port number (format: {bus}-{port}[.{subport}])
# use lsusb to list attached devices, get device number
# ue lsusb -t to find that device under bus tree

# output should look like this
# /:  Bus 01.Port 1: Dev 1, Class=root_hub, Driver=xhci_hcd/10p, 480M
#    |__ Port 5: Dev 26, If 1, Class=Human Interface Device, Driver=, 1.5M

# in this case bus=1 port=5, value to pass 1-5


port='usb1' # this bill restart while usb hub I think
#port='1-7' # this should restart single port (far right usb2.0)

echo "Working with port: $port ..."

# first argument should be port (in this case "$port")
bind_usb(){
	echo "$1" > /sys/bus/usb/drivers/usb/bind
}

unbind_usb(){
	echo "$1" > /sys/bus/usb/drivers/usb/unbind
}

echo "Unbinding usb on port $port"
unbind_usb "$port"

sleep 1

echo "Binding usb on port $port"
bind_usb "$port"
