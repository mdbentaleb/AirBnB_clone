#!/usr/bin/python3
""" defines the review class """
from models.base_model import BaseModel


class Review(BaseModel):
    """ represent a review
    attributes
        place_id : the Place id
        user_id : the User id
        text : the text of the review
    """

    place_id = ""
    user_id = ""
    text = ""
