# Melp - Intelimétrica

 Test for Backend Developer at Intelimétrica

 Links to the API documentation:

- Swagger UI: [https://melp-testing.herokuapp.com/docs](https://melp-testing.herokuapp.com/docs)
- ReDoc Documentation: [https://melp-testing.herokuapp.com/redoc](https://melp-testing.herokuapp.com/redoc)
- Postman: [https://www.postman.com/luisornelasch/workspace/melp-intelimtrica/collection/18472659-7f17a436-5ad2-4177-bffa-849f0475c46d](https://www.postman.com/luisornelasch/workspace/melp-intelimtrica/collection/18472659-7f17a436-5ad2-4177-bffa-849f0475c46d)


## Local

NOTE: To be able to run the API locally, you need to have Docker installed.

The following command will allow us to raise the Docker containers to run the API:

```sh
$ docker-compose up -d
```

To run the API, the command used is:

```sh
$ docker-compose logs -f app
```

These commands will raise the API locally at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

Locally we can consult the ReDoc documentation of the API in the path: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc).

To test the functionality of the API in the path: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).


### Migration

For migration to the database, it is only necessary to run the command:

```sh
$ docker-compose exec app python migration.py
```
