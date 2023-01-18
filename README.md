# Test for Backend Developer at Intelimétrica
 
 ### Assignment Description
 
 - Import the raw data (from the CSV file) into a relational database and exposing a REST API that implements CRUD (Create, Read, Update, Delete) operations.
   
   Create the Restaurants table with the following schema:
      ```
     Restaurants (
         id TEXT PRIMARY KEY, -- Unique Identifier of Restaurant
         rating INTEGER, -- Number between 0 and 4
         name TEXT, -- Name of the restaurant
         site TEXT, -- Url of the restaurant
         email TEXT,
         phone TEXT,
         street TEXT,
         city TEXT,
         state TEXT,
         lat FLOAT, -- Latitude
         lng FLOAT) -- Longitude
     ```
 - Implement the following endpoint: ```/restaurants/statistics?latitude=x&longitude=y&radius=z ``` it receives a latitude and a longitude as parameters, which correspond to the center of a circle, and a third parameter that corresponds to a radius in meters.

     This endpoint needs to return a JSON with the following data:
     ```
     {
       count: Count of restaurants that are inside the circle with center [x,y] and radius z,
       avg: Average rating of restaurant inside the circle,
       std: Standard deviation of rating of restaurants inside the circle
     }
     ```

Once deployed, please send us the following:
- Link to the heroku app.
- A Postman collection to test your API.


## Links to Heroku app and Postman collection:

- Swagger UI: [https://melp-testing.herokuapp.com/docs](https://melp-testing.herokuapp.com/docs)
- ReDoc Documentation: [https://melp-testing.herokuapp.com/redoc](https://melp-testing.herokuapp.com/redoc)
- Postman: [https://www.postman.com/luisornelasch/workspace/melp-intelimtrica/collection/18472659-7f17a436-5ad2-4177-bffa-849f0475c46d](https://www.postman.com/luisornelasch/workspace/melp-intelimtrica/collection/18472659-7f17a436-5ad2-4177-bffa-849f0475c46d)


## Local

NOTE: To be able to run the API locally, you need to have Docker installed.

The following command will allow you to create the Docker containers to run the API:

```sh
$ docker-compose up -d
```

To run the API, the command used is:

```sh
$ docker-compose logs -f app
```

These commands will deploy the API locally at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

Locally you can consult the ReDoc documentation of the API in the path: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc).

To test the functionality of the API in the path: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).


### Migration

For migration to the database, it is only necessary to run the command:

```sh
$ docker-compose exec app python migration.py
```
