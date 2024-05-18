#!/usr/bin/python3
""" defines the place class """
from models.base_model import BaseModel


class Place(BaseModel):
    """ represent a place
    attributes
        city_id: the City id
        user_id: the User id
        name: the name of the place
        description: the descrip of the place
        number_rooms: the num of rooms of the place
        number_bathrooms: the num of bathrooms of the place
        max_guest: the max numb of guests of the place
        price_by_night: the price by night of the place
        latitude: the latitude of the place
        longitude: the longitude of the place
        amenity_ids: a list of Amenity ids
    """

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
