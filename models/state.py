#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', back_populates='state')

    @property
    def cities(self):
        """Gets the cities attribute"""
        from models import storage

        dict_city = storage.all(City)
        output = []

        for key in dict_city:
            city = dict_city[key]
            if self.id == city.state_id:
                output.append(city)
        return output
