# gRPC_demo
easy micro services with gRPC communication

This prject contains 2 micro services, communicating with gRPC.
  1. frontend -- a http server to forward a httpRequest to corresponding backend service
  2. register -- the backend service to handle Register
  
Set up the project

  1. Clone this repo to your local
     
      Command: $ git clone https://github.com/i333463/gRPC_demo.git
      
      Result
      -------------------------------------------------------------------------
      Cloning into 'gRPC_demo'...
      remote: Enumerating objects: 74, done.
      remote: Counting objects: 100% (74/74), done.
      remote: Compressing objects: 100% (50/50), done.
      remote: Total 74 (delta 30), reused 65 (delta 23), pack-reused 0
      Unpacking objects: 100% (74/74), done.
      -------------------------------------------------------------------------
      
      The repo has been cloned into the local.
  
  2. Build the image for service 'frontend'
     
      Command:  $ cd gRPC_demo/src/app_frontend 
      
      Command:  $ ls
      
      Result
      -------------------------------------------------------------------------
      Dockerfile        frontend.py       requirements.txt  templates
      app_frontend.py   genproto          static
      -------------------------------------------------------------------------

      Command:  $ docker build -f Dockerfile .
      
      Result
      -------------------------------------------------------------------------
      Successfully built c39028007fc7
      -------------------------------------------------------------------------
      
      Now a image 'c39028007fc7' was built successfully.
      
  3. Run this image as the container.
  
      Command:  $ docker run -d -p 8080:5000 c39028007fc7
      
      Result
      -------------------------------------------------------------------------
      Successfully built c39028007fc7
      -------------------------------------------------------------------------
      
      The Frontend service will listen the port 5000, and forward the request to backend service.
      And in the Docker file, expose the 5000 port as well.
      Mapping the port 8080 of host ---> port 5000 of container
      
      
      
  
     
      
  
