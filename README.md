# Steps to run this application

###### Prerequsite: 
* need docker CE
---
* #####  clone this repo on your PC
* #####  select application folder inside this repo
* #####  build docker container using this command sudo docker build -t flask_app .
* #####  After Successful build to run docker container - sudo docker run -e "MESSAGE=port 500x" -p 500x:5000 -d flask_app
* #####  run this above command for 3 times with different port (500x) where x is variable x=1,x=2,x=3.
* #####  for nginx deployment move back to root folder of this repo and select nginx-docker
* #####  build docker conatiner using this command sudo docker build -t nginx-docker .
* #####  After Successful build to run docker container - sudo docker run -p 5000:80 -d nginx-docker
* ###### check dockercontainer status using command sudo docker ps
***
open browser and use localhost:5000/user?user="xxx"   x-->refers to value of user 
values in dictionary {"abc":123,"man":"mankey","dog":"dogkey","cat":"catkey"}.
***
#### Expected output: response from port 500x key for user: key-value 
***

# A package of flask app

 ###### function: get api for user->key  
 ###### application framework:Flask  
 ###### Backend TCP load balancer:Nginx reverse proxy  
 ###### Deployed on multiple docker container.  
***
## Flask App 
##### Created flask app ```[app.py](./application/app.py)``` with using dictionary to check whether user present or not. If not then key error 400.
##### Created requirement file Created [requirements.txt](./application/requirements.txt)for packages needed by python to execute.
##### Created Dockerfile [Dockerfile](../application/Dockerfile)
***
## Nginx configuration
##### Created Dockerfile [Dockerfile](./nginx-docker/Dockerfile)
##### Created configuration file for nginx [nginx.conf](./nginx-docker/nginx.conf)
