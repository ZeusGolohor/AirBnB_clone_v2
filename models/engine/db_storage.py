#!/usr/bin/python3
""" DB_Storage model for HBNB project"""
import sqlalchemy
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
import os
from sqlalchemy import create_engine


class DBStorage():
    __engine = None
    __session = None

    def __init__(self):
        """
        This method is used to instanciate this class.
        """
        self.HBNB_MYSQL_USER = os.getenv("HBNB_MYSQL_USER")
        self.HBNB_MYSQL_PWD = os.getenv("HBNB_MYSQL_PWD")
        self.HBNB_MYSQL_HOST = os.getenv("HBNB_MYSQL_HOST", "localhost")
        self.HBNB_MYSQL_DB = os.getenv("HBNB_MYSQL_DB")
        self.HBNB_ENV = os.getenv("HBNB_ENV")
        self.HBNB_TYPE_STORAGE = os.getenv("HBNB_TYPE_STORAGE")
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format
            ("hbnb_dev", "hbnb_dev_pwd", "hbnb_dev_db"), pool_pre_ping=True)
        if (self.HBNB_ENV == 'test'):
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        results = {}
        self.reload()
        # check if we should print all or just one class
        if (cls is not None):
            for key, value in classes.items():
                if value is cls:
                    try:
                        query1 = self.__session.query(value).all()
                        for query in query1:
                            results["{}.{}".format(
                                key, query.id)] = query.to_dict()
                    except sqlalchemy.exc.InvalidRequestError:
                        pass
        else:
            for key, value in classes.items():
                try:
                    query1 = self.__session.query(value).all()
                    for query in query1:
                        results["{}.{}".format(
                                key, query.id)] = query.to_dict()
                except sqlalchemy.exc.InvalidRequestError:
                    pass
        return (results)

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if (obj is not None):
            self.__session.delete(obj)
            self.__session.commit()

    def reload(self):
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)
