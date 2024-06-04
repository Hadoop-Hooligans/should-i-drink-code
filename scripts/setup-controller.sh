#!/bin/bash

# set up env script
touch .env
# build the required packages
sh setup_ansible_mini.sh
sh init_ansible.sh