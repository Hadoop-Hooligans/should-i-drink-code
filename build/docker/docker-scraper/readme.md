# readme for docker
This docker file needs access to src to run,

You can pull our local docker using

```
docker pull desertroam/hadoophulligans:latest
```
or you can just run it directly and make sure its output is sent to your terminal to monitor its progress.

```
docker run -it desertroam/hadoophulligans:latest
```

The docker file is hosted on dockerhub so you should have no issues downloading it and all the code to run the container itself and python is stored in the image file.

# ENV file
You will need to consider your own .env file to access this container and send the data to a database.