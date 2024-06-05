#!/bin/bash

# this command is only for Docker
#apt update && apt install -y sudo
# set up timezone to not prompt
sudo ln -fs /usr/share/zoneinfo/Pacific/Auckland /etc/localtime
export TZ=Pacific/Auckland

# rest installs ansible to be used.
sudo apt-get clean all
sudo apt-get update
sudo apt-get dist-upgrade -y
sudo apt-get install python3 -y
sudo apt-get install python3-pip -y
sudo apt-get install software-properties-common -y
sudo apt-get install -y ansible

# some of these tools are not on some debian sites so installs them.
sudo apt-get install -y curl git wget tmux vim