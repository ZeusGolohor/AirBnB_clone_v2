#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage
from datetime import datetime
from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    name = ""

    # defining a relationship btn place and amenities
    place_amenity = Table("place_amenity",
                          Base.metadata,
                          Column(
                              "place_id",
                              String(60),
                              ForeignKey("places.id"),
                              primary_key=True,
                              nullable=False),
                          Column(
                              "amenity_id",
                              String(60),
                              ForeignKey("amenities.id"),
                              primary_key=True,
                              nullable=False)
                          )

    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship(
        "Place", secondary=place_amenity, viewonly=False, backref="amenities")

    def __init__(self, *args, **kwagrs):
        """
        This method is called wherever this class gets
        instanciated.
        """
        if ("id" not in kwagrs.keys()):
            super().__init__()
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
