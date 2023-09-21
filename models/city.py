#!/usr/bin/python3
"""
City class module.
"""

from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    """
    City class that inherits from BaseModel and Base.
    """
    
    __tablename__ = 'cities'
    
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    
    # Add a relationship to State
    state = relationship("State", back_populates="cities")
