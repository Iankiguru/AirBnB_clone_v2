#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
from os import environ
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class Review(BaseModel):
    """ Review class to store review information """
    if "HBNB_TYPE_STORAGE" in environ and environ["HBNB_TYPE_STORAGE"] == "db":
        __tablename__ = 'reviews'

        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)

    # Define a relationship from Review to User
    user = relationship('User', back_populates='reviews')

    # Define a relationship from Review to Place
    place = relationship('Place', back_populates='reviews', cascade='all, delete-orphan')
