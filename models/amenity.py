#!/usr/bin/python3
"""
Amenity class module.
"""

from models.base_model import BaseModel
from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from os import environ

class Amenity(BaseModel):
    """
    Amenity class that inherits from BaseModel.
    """

    if "HBNB_TYPE_STORAGE" in environ and environ["HBNB_TYPE_STORAGE"] == "db":
        __tablename__ = 'amenities'

        name = Column(String(128), nullable=False)

        # Define a many-to-many relationship between Place and Amenity through place_amenity
        place_amenities = relationship(
            "Place",
            secondary="place_amenity",
            viewonly=False,
            back_populates="amenities"
        )
