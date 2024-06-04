#!/bin/bash
log_file="../../logs/$(date +'%Y-%d-%m-%H:%M')-pythonscraper.log"

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

# runs docker selenium scraper

#Test purpose go back to previous directory.
# repo=desertroam/hadoophulligans
# tag=latest
# pythonscraper should change to something that briefly explains what the script does
# --Copy

scriptfile='start_scraper.sh' # should be script name 

echo "Please check $log_file to view any activities"


echo "running $scriptfile" >> $log_file
# -- leave these lines below
#dont move these over to new scripts if you move the stuff above check names ie script names
{ 
    time ( 
        sudo docker compose down -v | while IFS= read -r line; do 
            printf '%s %s %s %s %s\n' "$HOSTNAME:" "$(whoami)" - "$(date)" "$line"
            done 
        )} 2>&1 | tee -a "$log_file"

{ 
    time ( 
        sudo docker compose up | while IFS= read -r line; do 
            printf '%s %s %s %s %s\n' "$HOSTNAME:" "$(whoami)" - "$(date)" "$line"
            done 
        )} 2>&1 | tee -a "$log_file"
        
# --copy below here this can be appended to end of script
#sudo docker run -it --name python-scraper $repo:$tag
cat << EOF >> "$log_file"
$(printf "%0.s-" {1..32})
FINISHED LOGGING
$(printf "%0.s-" {1..32})
EOF