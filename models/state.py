#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage
from datetime import datetime
from sqlalchemy import Column, Integer, String, MetaData, DateTime
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """
    This class is used to manage the State class
    instances.
    """
    name = ""
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    state = relationship("Place", backref="cities")

    def __init__(self, *args, **kwagrs):
        """
        This method is called wherever this class gets
        instanciated.
        """
        if ("id" not in kwagrs.keys()):
            super().__init__()
        if 'name' not in kwagrs:
            kwagrs['name'] = self.name
        for key, value in kwagrs.items():
            if key != "__class__":
                if (key == "created_at"):
                    self.created_at = datetime.fromisoformat(value)
                elif (key == "updated_at"):
                    self.updated_at = datetime.fromisoformat(value)
                else:
                    setattr(self, key, value)
        if ("id" not in kwagrs.keys()):
            storage.new(self)
