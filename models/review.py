#!/usr/bin/python3
""" Review module for the HBNB project """
import models
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel):
    """ Review classto store review information """
    if model.storage_type = "db":
        __tablename__ = 'reviews'
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), nullable=False, ForeignKey('places_id'))
        user_id = Column(String(60), nullable=False, ForeignKey('users.id'))
    else:
        place_id = ""
        user_id = ""
        text = ""
