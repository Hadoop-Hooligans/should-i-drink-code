#!/bin/bash

# Define log file path for Terraform init operation
init_log_file="../../logs/$(date +'%Y-%d-%m')-hdg-terraform-init.log"


mc_details=("$(uname)" "$(lsb_release -c | awk '{print $2}')")
cat << EOF >> "$init_log_file"
$(printf "%0.s-" {1..32})
INFORMATION

$(printf "%0.s-" {1..32})

You are currently on $HOSTNAME
Running as user      $(whoami)
you appear to be running on ${mc_details[0]}\\${mc_details[1]}
$(printf "%0.s-" {1..32})

EOF

cat << EOF >> "$init_log_file"
$(printf "%0.s-" {1..32})
Terraform needs to initialise

$(printf "%0.s-" {1..32})
EOF




# Logging related to Python scraper
echo "Please check $init_log_file to view any activities"

echo "running init_instance.sh" >> "$init_log_file"



{
    time (
        terraform init 2>&1 | while IFS= read -r line; do
            printf '%s %s\n' "$(date)" "$line" 
        done
    )
} 2>&1 | tee -a "$init_log_file"

cat << EOF >> "$init_log_file"
$(printf "%0.s-" {1..32})
FINISHED LOGGING
$(printf "%0.s-" {1..32})
EOF
