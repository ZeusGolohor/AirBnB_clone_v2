#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage
from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, Float


class Place(BaseModel, Base):
    """ A place to stay """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    # cities = relationship("City", backref="cities")

    def __init__(self, *args, **kwagrs):
        """
        This method is called wherever this class gets
        instanciated.
        """
        if ("id" not in kwagrs.keys()):
            super().__init__()
        # check if default values should be used
        if 'city_id' not in kwagrs:
            kwagrs['city_id'] = self.city_id
        if 'user_id' not in kwagrs:
            kwagrs['user_id'] = self.user_id
        if 'name' not in kwagrs:
            kwagrs['name'] = self.name
        if 'description' not in kwagrs:
            kwagrs['description'] = self.description
        if 'number_rooms' not in kwagrs:
            kwagrs['number_rooms'] = self.number_rooms
        if 'number_bathrooms' not in kwagrs:
            kwagrs['number_bathrooms'] = self.number_bathrooms
        if 'max_guest' not in kwagrs:
            kwagrs['max_guest'] = self.max_guest
        if 'price_by_night' not in kwagrs:
            kwagrs['price_by_night'] = self.price_by_night
        if 'latitude' not in kwagrs:
            kwagrs['latitude'] = self.latitude
        if 'longitude' not in kwagrs:
            kwagrs['longitude'] = self.longitude
        if 'amenity_ids' not in kwagrs:
            kwagrs['amenity_ids'] = self.amenity_ids
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
