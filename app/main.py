from typing import List
from fastapi import (FastAPI, Response, status,
                     HTTPException, Depends, APIRouter)
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from app.models import models
from app.database.database import engine, get_db
from app.schemas import schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Melp")

router = APIRouter(
    prefix="/restaurants", tags=["Restaurantes"])


@router.get("/statistics", response_model=schemas.Statistics,
            description="Muestra los restaurantes en un radio en metros específico tomando como centro de referencia una latitud y una longitud determinadas")
def statistics(latitude: float, longitude: float,
               radius: float, db: Session = Depends(get_db)):

    return db.query(func.count(models.Post.id).label('count'), func.avg(models.Post.rating).label('avg'), func.stddev(models.Post.rating).label('std')).filter(func.ST_DistanceSphere(func.ST_MakePoint(models.Post.lng, models.Post.lat), func.ST_MakePoint(longitude, latitude)) <= radius).first()


# Get all the restaurants


@router.get("", response_model=List[schemas.Restaurant],
            description="Muestra todos los restaurantes registrados")
def list_restaurants(db: Session = Depends(get_db)):
    return db.query(models.Post).all()


# Get a specific restaurant
@router.get("/{id}", response_model=schemas.Restaurant,
            description="Muestra los datos de un restaurante en específico")
def get_restaurant(id: str, db: Session = Depends(get_db)):

    restaurant = db.query(models.Post).filter(models.Post.id == id).first()

    if not restaurant:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Restaurant with id: {id} was not found")

    return restaurant


# Create a restaurant
@router.post("", status_code=status.HTTP_201_CREATED,
             response_model=schemas.Restaurant, description="Registra nuevo restaurante")
def create_restaurant(post: schemas.RestaurantBase, db: Session = Depends(get_db)):

    restaurant = models.Post(**post.dict())
    db.add(restaurant)
    db.commit()
    db.refresh(restaurant)

    return restaurant


# Delete a restaurant
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, description="Elimina un restaurante en específico")
def delete_restaurant(id: str, db: Session = Depends(get_db)):

    restaurant = db.query(models.Post).filter(models.Post.id == id)

    if restaurant.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Restaurant with id: {id} was not found")

    restaurant.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


# Update a restaurant
@router.put("/{id}", response_model=schemas.Restaurant,
            description="Actualiza los datos de un restaurante en específico")
def update_restaurant(id: str, post: schemas.RestaurantBase,
                      db: Session = Depends(get_db)):

    query = db.query(models.Post).filter(models.Post.id == id)
    post_first = query.first()

    if post_first is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Restaurant with id: {id} does not exist")

    query.update(post.dict(), synchronize_session=False)
    db.commit()
    return query.first()


app.include_router(router)
