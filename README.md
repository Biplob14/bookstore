# bookstore

>Django based Ecommerce site for books. 

## Run project with
- `docker-compose up` command and everything will be set.
- register the database server with pg admin to show data. Enter hostname same as the name of database service name set on docker-compose
- create a superadmin to access as admin and modify data. 
- use command `python manage.py loaddata data_collection.json` to load existing json data into database. 