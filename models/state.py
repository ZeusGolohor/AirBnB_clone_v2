#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from datetime import datetime
from sqlalchemy import Column, Integer, String, MetaData, DateTime
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """
    This class is used to manage the State class
    instances.
    """
    name = ""
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade='all, delete-orphan')

    def __init__(self, *args, **kwagrs):
        """
        This method is called wherever this class gets
        instanciated.
        """
        from models import storage

        if ("id" not in kwagrs.keys()):
            super().__init__()
        if ("_sa_instance_state" in kwagrs):
            del kwagrs["_sa_instance_state"]
        for key, value in kwagrs.items():
            if key != "__class__":
                if (key == "created_at"):
                    self.created_at = datetime.fromisoformat(value)
                elif (key == "updated_at"):
                    self.updated_at = datetime.fromisoformat(value)
                else:
                    setattr(self, key, value)
        if ("id" not in kwagrs.keys()):
            # check for the database in use
            # if (os.getenv("HBNB_TYPE_STORAGE", "FileStorage") != "db"):
            # if ("name" not in kwagrs.keys()):
            #     kwagrs["name"] = ""
            storage.new(self)

    @property
    def cities(self):
        """
        Method to return the list of City objects from
        storage linked to the current State.
        """
        from models.__init__ import storage
        from models.city import City
        cities = []
        # Get all states.cities in the file storage.
        for id, value in storage._FileStorage__objects.items():
            if (value.__class__ == City):
                if (value.state_id == self.id):
                    del value._sa_instance_state
                    try:
                        del self._sa_instance_state
                    except Exception:
                        pass
                    cities.append(value)
            # exit(1)
        return (cities)
