#!/usr/bin/python3
"""This module for the DBStorage"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from os import getenv

class DBStorage:
    """
    DBStorage class for managing database storage.
    """

    __engine = None
    __session = None

    def __init__(self):
        """
        Initialize DBStorage instance.
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Query and return all objects of a specific class or all classes.
        """
        objects = {}
        classes = [cls] if cls else [User, State, City, Amenity, Place, Review]

        for cls in classes:
            objects.update({obj.id: obj for obj in self.__session.query(cls).all()})

        return objects

    def new(self, obj):
        """
        Add a new object to the current database session.
        """
        self.__session.add(obj)

    def save(self):
        """
        Commit all changes of the current database session.
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete an object from the current database session.
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Create all tables in the database and create a new database session.
        """
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                      expire_on_commit=False))

    def close(self):
        """
        Close the session.
        """
        self.__session.remove()
