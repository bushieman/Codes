# Linux Docker setup
sudo groupadd <groupname> # adding new group 
sudo adduser <username> # adding new user
sudo usermod -aG <groupname> <username> # create simlink between user and group
sudo login # login to your account
exit # logs out all existing configs
sudo systemctl list-units # show all processes
sudo systemctl list-units --type=service # show all services
sudo systemctl start <name of your service>
sudo setfacl -m user:$<user>: rw /var/run/docker.sock # ??
grep <groupname> /etc/group # check existing groups
newgrp <groupname> # change your users group ID 

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

CMD ['npm start']

#* terminal commands
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

# run a detached from the terminal container to allow us to use the terminal - d is for detach
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

# removing containers
docker rm <container name>

# stopping container - clean up before shutting down hence slower
docker stop <container id>

# kill container - no clean up. shutdown is instantaneous
docker kill <container id>

# port mapping - this enables us to run docker containers in the browser via our local machines
docker run -d --name <container name> -p <brower port>:<container port> <image name>

# port mapping for react
# it is for interactive mode
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

# pushing to dockerhub
docker tag my-image username/my-repo
docker push username/my-repo
# docker commands
# docker build -t docker-tutorial . - to build a docker image in the current folder
# docker image ls - show current images in local docker
# docker images - show current images in local docker
# docker run <name of the image>
# docker run ubuntu - start a docker container 
# docker search <image name> - search for images available in DockerHub
# docker pull <image name> - download the image from DockerHub to your local computer
# docker pull <registry.com/image name> - download the image from other registry
# docker run -it -d <container id> - to create and run a docker file
# docker exec -it <container id> - to run an existing docker file
# docker ps - check running processes
# docker ps -a - check all processes
# docker run -it ubuntu - start ubuntu container
# apt update
# apt install <name of package>
# apt remove <name of package>
# pwd - print working directory - to check where we are in the root directory
# ls - lists
# ls -1 - vertically arranged lists
# ls -l - more details on the lists
# mkdir <folder> - create a new folder
# touch <files> - create a new file
# mv <old file> <new file> - rename files
# mv <file> /new path - move the file to a new directory 
# rm <files> - remove files
# rm <file*> - remove files that start with file
# rm -r <directory> - remove an entire directory
# <package> - to open a package
# <package> <file> - to create a file inside a package and open it
# cat <file> or <absolute path to file> - open entire content of small files
# cat <file1> <file2> > <combined file> - combine multiple files into a single file
# echo <text> > <file> - write the text to the file
# more <file> or <absolute path to file> - open page by page of a file by scrolling down only using spacebar
# more <file> or <absolute path to file> - open page by page of a file with options for up and down navigation using arrow keys
# head -n 5 <file> or <absolute path to file> - show the first 5 lines of the file
# tail -n 5 <file> or <absolute path to file> - show the last 5 lines of the file

# CTRL w - remove an entire word from the terminal
# CTRL l - clear the terminal
# q - to exit
