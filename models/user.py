#!/usr/bin/python3
"""This module defines a class User"""
"""This module defines a class User"""
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class User(BaseModel):
    """
    User class that inherits from BaseModel.
    """

    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))

    # Define a one-to-many relationship from User to Place
    places = relationship('Place', back_populates='user', cascade='all, delete-orphan')

    # Define a one-to-many relationship from User to Review
    reviews = relationship('Review', back_populates='user', cascade='all, delete-orphan')
