#!/usr/bin/python3
""" defines the city class """
from models.base_model import BaseModel


class City(BaseModel):
    """ represent a city
    attributes
        state_id: The state id
        name: The name of the city
    """

    state_id = ""
    name = ""
