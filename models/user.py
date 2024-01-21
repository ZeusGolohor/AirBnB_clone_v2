#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from models.review import Review
from datetime import datetime
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship("Place", backref="users",
                          cascade='all, delete-orphan')
    reviews = relationship(Review, backref="user",
                           cascade='all, delete-orphan')

    def __init__(self, *args, **kwagrs):
        """
        This method is called wherever this class gets
        instanciated.
        """
        from models import storage

        if ("id" not in kwagrs.keys()):
            super().__init__()
        for key, value in kwagrs.items():
            if key != "__class__":
                if (key == "created_at"):
                    self.created_at = datetime.fromisoformat(value)
                elif (key == "updated_at"):
                    self.updated_at = datetime.fromisoformat(value)
                elif (key == "_sa_instance_state"):
                    del kwagrs["_sa_instance_state"]
                else:
                    setattr(self, key, value)
        if ("id" not in kwagrs.keys()):
            storage.new(self)
