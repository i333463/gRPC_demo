Register Service
-----------------
Register service is built with Python.

the Dockerfile already was provided in this repo. After clone this repo,go to path /register, and build the image with Dockerfile.

Build image & share it in docker hub
$ docker build -f Dockerfile .  # Build a image with Dockerfile

$ docker tag <image-built> <dockerhub_username>/<repo>:<tagname>  # Tag the image built just now
---Please replace <Variant> with the real value
---You need to have a user in dockerhub and create a repo

$ docker images  # List the images, then we can see the tag name

$ docker login  # Login docker hub with your username & password

$ docker push <dockerhub_username>/<repo>:<tagname>  # push it into your repo
---Please replace <Variant> with the real value

You will recieve below message:
<tagname>: digest: sha256:a4831e656ba9ad098425628ecdcd3c1addea9b2bdf70708b64fa20bba93c4f9e size: 3052

Now image was pushed in your repo.
Run the image
Run it anywhere after it was pushed into a repo.

$ docker run -d -p <your-port>:50051 <dockerhub_username>/<repo>:<tagname> # run the image
-- -d background run
-- -p mapping a port of your host to 50051, 50051 is the port that is listening by register service
