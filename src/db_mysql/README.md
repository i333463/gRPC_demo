# This is a composed db service for testing purpose.
contains:
  1. mysql db
  2. adminer
  3. app.py
 
these services were composed by a docker-compose file.

Dockerfile is for building the app.

init.sql is for initializing the db, create a DB and a Table.


# How to test in PWD

1. Clone the repo: git clone ~
2. goto the db_mysql path:  cd gRPC_demo/src/db_mysql
3. run the service:  docker-compose up




 
