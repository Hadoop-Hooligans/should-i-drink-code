#!/bin/bash
# ensure terraform has been initialised
bash init_terraform.sh
log_file="../../logs/$(date +'%Y-%d-%m')-hdg-create.log"

mc_details=("$(uname)" "$(lsb_release -c | awk '{print $2}')")
cat <<EOF >>"$log_file"
$(printf "%0.s-" {1..32})
INFORMATION

$(printf "%0.s-" {1..32})

You are currently on $HOSTNAME
Running as user      $(whoami)
you appear to be running on ${mc_details[0]}\\${mc_details[1]}
$(printf "%0.s-" {1..32})

EOF

args=("apply" "--auto-approve")

{
  time (
    terraform "${args[0]}" "${args[1]}" 2>&1 | while IFS= read -r line; do
      printf '%s %s\n' "$(date)" "$line"
    done
  )
} 2>&1 | tee -a "$log_file"

# I copied these over
log_file="../../logs/$(date +'%Y-%d-%m-%H:%M')-pythonscraper.log"
scriptfile='create_instance.sh' # should be script name

echo "Please check $log_file to view any activities"

echo "running $scriptfile" >>"$log_file"

# Copied this over
#sudo docker run -it --name python-scraper $repo:$tag
cat <<EOF >>"$log_file"
$(printf "%0.s-" {1..32})
FINISHED LOGGING
$(printf "%0.s-" {1..32})
EOF
