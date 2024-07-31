# ASPECT REST Service
The following repository hosts the software belonging to the ASPECT REST service. This API is accessed to retrieve data from the ASPECT server.

## API Runtime Environment
This software runs in a Docker container.
A docker container is a small virtual machine that has the minimal tools and applications needed to execute the API. This docker container comes with it's own operating system, by default the docker container uses the Ubuntu Linux Distribution. The instructions that are given to docker to start a container is within the Dockerfile.


# How to build and run ASPECT REST Service

## Windows
#### Install WSL
Navigate to the Windows command prompt (run as administrator).

//PHOTO

Run the following command: ```wsl --install ```

//PHOTO 

Once WSL has been installed you may need to restart the Windows machine.

//PHOTO


#### Install Docker Desktop
After WSL has been installed, navigate to a web browser and search for Docker Desktop and install the Windows Version.

//PHOTO

Click on the executable and follow the setup wizard.

//PHOTO

Once everything has installed, you will most likely need to restart the machine.

//PHOTO


#### Pull the Docker Container from DockerHub
After the Docker Desktop has installed, then

To build the following docker container run the following command:

``` sudo docker build -t avara2024/aspect-rest-service:latest .```

To run the container:

``` sudo docker run -d --name aspect-rest-service -p 8001:80 avara2024/aspect-rest-service:latest ```



To push to docker hub:

``` sudo docker login docker.io -u avara2024 -p dckr_pat_J-Dfk_dtHfL14WfaRThUgGOzHuI```

``` sudo docker push avara2024/aspect-rest-service:latest```
uvicorn your_fastapi_app:app --host 0.0.0.0 --port 443 --ssl-keyfile=./key.pem --ssl-certfile=./cert.pem
