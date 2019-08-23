A image already existed in docker hub


    $ docker run -d -p 3306:3306 --name db -e MYSQL_ROOT_PASSWORD=helloworld01 ericwudocker01/db:latest --default-authentication-plugin=mysql_native_password
    
    $ docker run -d -p 5000:5000 --link db:db ericwudocker01/db:testapp

----------------------------------------------------------------------------------------------------

Build a mysql image   

    $ docker build -t db .
    

Run the image

    $ docker run -d -p 3306:3306 --name db -e MYSQL_ROOT_PASSWORD=helloworld01 db:latest --default-authentication-plugin=mysql_native_password
    

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
