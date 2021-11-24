# Melp - Intelimétrica

 Prueba para Backend Developer en Intelimétrica

 Los enlaces a la documentación de la API:

- Swagger UI: [https://melp-testing.herokuapp.com/docs](https://melp-testing.herokuapp.com/docs)
- ReDoc Documentation: [https://melp-testing.herokuapp.com/redoc](https://melp-testing.herokuapp.com/redoc)
- Postman: [https://www.postman.com/luisornelasch/workspace/melp-intelimtrica/collection/18472659-7f17a436-5ad2-4177-bffa-849f0475c46d](https://www.postman.com/luisornelasch/workspace/melp-intelimtrica/collection/18472659-7f17a436-5ad2-4177-bffa-849f0475c46d)


## Local

NOTA: Para poder correr la API de forma local es necesario contar con Docker.

El siguiente comando nos permitirá levantar los contenedores de Docker para correr la API:

```sh
$ docker-compose up -d
```

Para correr la API se usa el comando:

```sh
$ docker-compose logs -f app
```

Estos comandos van a levantar la API de forma local en [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

De forma local podemos consultar la documentación de ReDoc de la API en la ruta: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc).

Para pobrar la funcionalidad de la API en la ruta: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).


### Migración

Para la migración a la base de datos únicamente es necesario ejecutar el comando:

```sh
$ docker-compose exec app python migration.py
```