#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from models import storage
from datetime import datetime


class City(BaseModel):
    """ The city class, contains state ID and name """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwagrs):
        """
        This method is called wherever this class gets
        instanciated.
        """
        if ("id" not in kwagrs.keys()):
            super().__init__()
        # check if default values should be used
        if 'state_id' not in kwagrs:
            kwagrs['state_id'] = self.state_id
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
