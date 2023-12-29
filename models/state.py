#!/usr/bin/python3
"""This is the state class"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
from models.city import City
import shlex


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")
    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """
            Getter method to return the list of City objects linked to the current State.
            """
            city_list = []
            for city_id, city in models.storage.all(City).items():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
