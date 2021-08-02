#!/bin/bash

apt update && apt install  openssh-server sudo -y

useradd -r -s /bin/bash -g root -G sudo new_user

echo 'new_user:new_user_passwd' | chpasswd

service ssh start

