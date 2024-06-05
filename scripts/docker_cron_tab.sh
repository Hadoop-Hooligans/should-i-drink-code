IMAGE_NAME="desertroam/hadoophulligans:latest"
REPO="/home/ubuntu/should-i-drink-code/build/docker/docker-scraper"
RUN_COMMAND_SCRIPT="start_scraper.sh"

container_age() {
    local container_id=$(sudo docker ps -q -f ancestor=$IMAGE_NAME)
    if [ -z "$container_id" ]; then
        echo 9999
        return
    fi
    local start_time=$(sudo docker inspect -f '{{.State.StartedAt}}' $container_id)
    local start_timestamp=$(date -d "$start_time" +%s)
    local current_timestamp=$(date +%s)
    local age=$((current_timestamp - start_timestamp))
    echo $age
}
    age=$(container_age)
    if [ $age -lt 3000 ]; then
        echo "$(date): Container is less than 5 minutes old. Skipping restart."
        exit 0
    fi

      running_container=$(sudo docker ps -q -f ancestor=$IMAGE_NAME)
    if [ -z "$running_container" ]; then
        echo "$(date): No running container found for image $IMAGE_NAME. Starting the Docker container using $RUN_COMMAND_SCRIPT."
        cd $REPO
        bash $RUN_COMMAND_SCRIPT
    else
        cd $REPO
        sudo docker compose pull
        bash $RUN_COMMAND_SCRIPT
    fi
fi