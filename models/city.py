#!/usr/bin/python3
""" City Module for HBNB project """
import models
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey


class City(BaseModel):
    """ The city class, contains state ID and name """
    if models.storage_type =="db":
        __tablename__ = "cities"
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        name = Column(String(128), ForeignKey("states.id"), nullable=False)
        places = relationship("Place", cascade="all, delete-orphan", backref="city")
    else:
        state_id = ""
        name = ""
