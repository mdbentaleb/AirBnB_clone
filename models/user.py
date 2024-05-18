#!/usr/bin/python3
""" defines the user class """
from models.base_model import BaseModel


class User(BaseModel):
    """ represent a user
    attributes
        email: the email of the user
        password: the passwd of the user
        first_name: the first name of the user
        last_name: the last name of the user
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
