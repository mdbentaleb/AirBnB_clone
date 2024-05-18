#!/usr/bin/python3
""" defines the amenity class . """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ represent an Amenity
    attributes
        name : the name of the amenity
    """

    name = ""
