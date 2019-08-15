# gRPC_demo
easy micro services with gRPC communication
--------------------------------------------

This prject contains 2 micro services, communicating with gRPC.
  1. frontend -- a http server to forward a httpRequest to corresponding backend service
  2. register -- the backend service to handle Register
  
Set up the project
------------------------

  1. Clone this repo to your local
  ------------------------------------------------------------------------------
     
      Command: $ git clone https://github.com/i333463/gRPC_demo.git
      
      Result:
      Cloning into 'gRPC_demo'...
      remote: Enumerating objects: 74, done.
      remote: Counting objects: 100% (74/74), done.
      remote: Compressing objects: 100% (50/50), done.
      remote: Total 74 (delta 30), reused 65 (delta 23), pack-reused 0
      Unpacking objects: 100% (74/74), done.
      
      The repo has been cloned into the local.
      
  
  2. Build the image for service 'frontend'
  ------------------------------------------------------------------------------
     
      Command:  $ cd gRPC_demo/src/app_frontend 
      
      Command:  $ ls
      
      Result:
      Dockerfile        frontend.py       requirements.txt  templates
      app_frontend.py   genproto          static
     

      Command:  $ docker build -f Dockerfile .
      
      Result:   Successfully built c39028007fc7
      
      Now a image 'c39028007fc7' was built successfully.
      
  3. Run this image as the container.
  ------------------------------------------------------------------------------
  
      Command:  $ docker run -d -p 8080:5000 c39028007fc7
      
      -p 8080:5000:
      The Frontend service will listen the port 5000, and forward the request to backend service.
      And in the Docker file, expose the 5000 port as well.
      Mapping the port 8080 of host ---> port 5000 of container
      
      -d background
      
      Command:  $ docker ps
      
      Result:
      CONTAINER ID    IMAGE        COMMAND              CREATED        STATUS    PORTS          NAMES
      cc3d4df9f7af  c39028007fc7   "python /app_fronten…"   47 seconds ago   Up 45 seconds   0.0.0.0:8080->5000/tcp   nifty_darwin
      
  4. Build the image for service 'register'
  ------------------------------------------------------------------------------
   
      Command:  $ cd gRPC_demo/src/register
      Command:  $ docker build -f Dockerfile .
      
      Result:   Successfully built d8c201353144
      
  5. Run this image as the container.
  ------------------------------------------------------------------------------
   
      Command:  $ docker run -d -p 50051:50051 d8c201353144
      
      Mapping the port 50051 of host ---> port 50051 of container
      
  6. Organize the containers and network
  ------------------------------------------------------------------------------
  
  How to handle the communication between 2 containers, this step is to link this two containers via an network. We can use docker network command to achieve this.
  
  Use command:   $ docker ps 
  List all of containers, then replace below container1 & container2 with your real container id.
  
      Command:  $ docker network create testnet
                $ docker network connect testnet container1 --alias frontend
                $ docker network connect testnet container2 --alias register
                
     
     In the frontend service, when a register request was recieved, it will be forward to backend service "register" that runing in the container2, this communication was done by a channel provided by gRPC client API, the channel should contains a available <hostname:port> format address.
     The contaniners that running in the same docker network, it's possible to use alias instead of <hostname>.
     
   7.Test
  ------------------------------------------------------------------------------
 
   Goto <Your-hostname:8080>, and click register. 
 
     
   
   
      
  
     
      
  
