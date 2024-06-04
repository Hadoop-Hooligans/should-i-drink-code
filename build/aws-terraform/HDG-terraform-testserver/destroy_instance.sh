#!/bin/bash

# ensure terraform has been initialised
bash init_terraform.sh

log_file="../../logs/$(date +'%Y-%d-%m')-hdg-destroy.log"

mc_details=("$(uname)" "$(lsb_release -c | awk '{print $2}')")
cat << EOF >> "$log_file"
$(printf "%0.s-" {1..32})
INFORMATION

$(printf "%0.s-" {1..32})

You are currently on $HOSTNAME
Running as user      $(whoami)
you appear to be running on ${mc_details[0]}\\${mc_details[1]}
$(printf "%0.s-" {1..32})

EOF

# Define log file path for Terraform destroy operation

args=("destroy" "--auto-approve") 

echo "running destroy_instance.sh" >> "$log_file"

# Terraform destroy operation logging
{
    time (
        terraform ${args[0]} ${args[1]} 2>&1 | while IFS= read -r line; do
            printf '%s %s\n' "$(date)" "$line"
        done
    )
} 2>&1 | tee -a "$log_file"

# Logging related to Python scraper
echo "Please check $log_file to view any activities"

# Finish logging for Python scraper
cat << EOF >> "$log_file"
$(printf "%0.s-" {1..32})
FINISHED LOGGING
$(printf "%0.s-" {1..32})
EOF
