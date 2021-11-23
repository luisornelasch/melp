from os import name
from typing import Optional
import pandas
from pydantic import BaseModel, Field, validator
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float, engine
from sqlalchemy import orm
from sqlalchemy.orm import relationship, session
from sqlalchemy.sql.expression import null, text
from sqlalchemy.sql.functions import count
from sqlalchemy.sql.sqltypes import TIMESTAMP
from app.database.database import Base, engine
from numpy import genfromtxt


class Post(Base):
    __tablename__ = "restaurants"

    id = Column(String, primary_key=True, nullable=False)
    rating = Column(Integer, nullable=False)
    name = Column(String, nullable=False)
    site = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    street = Column(String, nullable=False)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    lat = Column(Float)
    lng = Column(Float)


# file_name = "restaurantes.csv"
# data_frame = pandas.read_csv(file_name)
# data_frame.to_sql(con=engine, name=Post.__tablename__,
#                   if_exists='append', index=False)
