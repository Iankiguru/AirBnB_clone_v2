#!/usr/bin/python3
"""
State class module.
"""

from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """
    State class that inherits from BaseModel and Base.
    """
    
    __tablename__ = 'states'
    
    name = Column(String(128), nullable=False)
    
    # Add a relationship to City
    cities = relationship("City", back_populates="state", cascade="all, delete-orphan")
