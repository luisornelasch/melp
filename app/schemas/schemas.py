from typing import Optional
from pydantic import BaseModel

from app.database.database import Base


class RestaurantBase(BaseModel):
    id: str
    rating: int
    name: str
    site: str
    email: str
    phone: str
    street: str
    city: str
    state: str
    lat: float
    lng: float


class Restaurant(RestaurantBase):
    class Config:
        orm_mode = True


class Statistics(BaseModel):
    count: int
    avg: Optional[float]
    std: Optional[float]

    class Config:
        orm_mode = True
