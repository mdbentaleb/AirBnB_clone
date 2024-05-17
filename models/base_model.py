#!/usr/bin/python3
""" BaseModel class """
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ represents the BaseModel """

    def __init__(self, *args, **kwargs):
        """ new BaseModel
        Args:
            *args: Unused.
            **kwargs: pairs of attributes.
        """
        d_form = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, d_form)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """ update """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """ return the dictionary of the BaseModel instance """
        c_dict = self.__dict__.copy()
        c_dict["created_at"] = self.created_at.isoformat()
        c_dict["updated_at"] = self.updated_at.isoformat()
        c_dict["__class__"] = self.__class__.__name__
        return c_dict

    def __str__(self):
        """ return the print/str representation of the BaseModel instance """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
