# THE DOCKER PROCESS
# 1. Write a dockerfile
# 2. Build a docker image
# 3. Run a docker container
 
# starting template for react
FROM node:alpine

# this is where to save your project in docker
WORKDIR /Usr/app 

# to enable caching node modules
COPY package.json .

RUN npm install

COPY ..

# Expose: Tells Docker which port our container is listening to for traffick during port mapping.
# By default some port are automatically mapped e.g 3000 -> React, therefore you need to expose them in order to use them during port mapping.
EXPOSE 3000 
CMD ['npm start']

#* Docker terminal commands
#@ build a docker image in the current dir
# with a latest version
docker build -t <image name> .

# with a specific version
docker build -t <image name:version> .

# check existing docker images
docker images 

#@ removing images
# specific version
docker image rm <image name:version>

# latest version
docker image rm <image name>

#@containers
# run a container i.e create and start
docker run <image name>

# run a detached from the terminal container to allow us to use the terminal; - d is for detach
docker run -d --name <detached container name> <image name>

# keep a container running for some given time using the sleep option which can also be set to infinity
docker run -d debian sleep 300

# check running containers
docker ps

# check all existing containers
docker ps -a

# view latest container created
docker ps -l

# start existing container
docker start <container name / id>

# removing containers; cannot remove running containers
docker rm <container name>

# stopping container - clean up before shutting down hence slower
docker stop <container id>

# kill container - no clean up. shutdown is instantaneous
docker kill <container id>

# port mapping - this enables us to run docker containers in the browser via our local machines
docker run -d --name <container name> -p <brower port>:<container port> <image name>

# port mapping for react
# -it is for interactive mode
docker run -it --name <react container> -p <browser port>:<container port> <image name>

#@ volumes
# enable refresh in react app using -v flag
-v <absolute path to directory to monitor>:<WORKDIR inside our container>

# anonymous volumes i.e leave the folders in this directory alone
-v <WORKDIR/node_modules>

# example
docker run --name react-container-with-volumes -it -p 3000:3000 -v $(pwd):/usr/app -v /usr/app/node_modules react-app

# use commit message to create new docker image as per your liking
docker commit -m "message" -a "Author's Name" container_id repository/new_image_name

#@compose
# start compose file
docker compose file> up

# remove docker containers
docker compose file> down

# docker login. you will get a password prompt after
docker login --username username

# pushing to DockerHub
docker tag my-image username/my-repo
docker push username/my-repo

# pulling an image from DockerHub
docker pull <image name>

# pulling an image from other registry
docker pull <registry.com/image name>

# search for images available in DockerHub
docker search <image name>

