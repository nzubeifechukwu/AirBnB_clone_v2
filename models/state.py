#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import storage


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', back_populates='state')

    @property
    def cities(self):
        """Gets the cities attribute"""
        dict_city = storage.all(City)
        ouput = []
        for city in dict_city:
            if self.id == city.state_id:
                output.append(city)
        return output
