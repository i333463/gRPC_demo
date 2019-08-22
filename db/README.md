Build a mysql image   

    $ docker build -t db .
    

Run the image

    $ docker run -d -p 3306:3306 --name db -e MYSQL_ROOT_PASSWORD=helloworld01 db:latest
    

Start up a Admin tool

    $ docker run -d -p 8080:8080 --link db:db adminer:latest
    
Build the test app

    $ cd src/db_mysql
    $ docker build -t app .
    
Start up the app

    $ docker run -d -p 5000:5000 --link db:db app:latest
    
Test the app

   Open host:5000, see result: 
   
    {"a user inserted": "Eric Wu"}
