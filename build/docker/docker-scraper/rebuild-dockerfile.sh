#!/bin/bash

username="desertroam"
repository="hadoophulligans"
tag="latest"

# Check if the script is being run inside the docker-scraper directory
expected_dir="docker-scraper"
current_dir=${PWD##*/}

if [ "$current_dir" != "$expected_dir" ]; then
  echo "Error: This script must be run from inside the $expected_dir directory."
  exit 1
fi

# Remove the Docker image
docker image rmi "$username/$repository:$tag"

# docker needs the src files
rm -rf src
cp -r ../../../src ./src

# Build the Docker image
docker build . -t "$username/$repository:$tag" --no-cache

# Clean up the src directory
rm -rf src

# Log in to Docker and push the image
docker login
docker push "$username/$repository:$tag"
