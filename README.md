# How to build docker container
To build the following docker container run the following command:

``` sudo docker build -t avara2024/aspect-rest-service:latest .```

To run the container:

``` sudo docker run -d --name aspect-rest-service -p 8001:80 avara2024/aspect-rest-service:latest ```



To push to docker hub:

``` sudo docker login docker.io -u avara2024 -p dckr_pat_J-Dfk_dtHfL14WfaRThUgGOzHuI```

``` sudo docker push avara2024/aspect-rest-service:latest```
uvicorn your_fastapi_app:app --host 0.0.0.0 --port 443 --ssl-keyfile=./key.pem --ssl-certfile=./cert.pem
