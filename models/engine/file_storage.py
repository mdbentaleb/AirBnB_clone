#!usr/bin/python3

""" defines the file storage class """
from models.base_model import BaseModel
from models.user import User
from models.state import State
import json
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ serializes an instance to JSON """

    # Stores all objects by <class name>.id
    __objects = {}
    # Path to the JSON file.
    __file_path = "file.json"

    def all(self, cls=None):
        """ returns a dictionary of __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __ojbects the obj with key <obj class name >.id """
        if obj is not None:
            # Concatenate class object name with id.
            key = obj.__class__.__name__+"."+obj.id
            # update the __object dictionary with values.
            self.__objects[key] = obj

    def save(self):
        """" serializes __objects to the JSON File(path:__file_path)  """
        j_objects = {}
        # For serialization of the data stored inside the __objec
        # variable as objects must be converted to a dictionary so that python
        # for json to understand using to_dict method of the basemodel class
        # The result is a unique dictionary as the value.
        for key in self.__objects:
            j_objects[key] = self.__objects[key].to_dict()
        # Convert the dictionary into json and save in __filepath.
        with open(self.__file_path, 'w') as f:
            json.dump(j_objects, f)

    def reload(self):
        """
        deserializes the JSON file to __objs(only if the JSON file(__file_path)
        """

        try:
            with open(self.__file_path, 'r', encoding="utf8") as f:
                # The load method deserializes a json string into a python dict
                obj_dict = json.load(f)
            for obj_item in obj_dict.values():
                # Extract the class from which to instantiate an object.
                # Remember we loaded the values not the keys.
                class_name = obj_item["__class__"]
                # creation of object instances the attribute __class__\
                # should not be supplied as part of the arguments to the init
                # function of the class(identified by class_name) all the other
                # arguments are valid.
                del obj_item["__class__"]
                # Use the defined new function to create a new __obj.
                # The double asterics expands the dictionary to allow every key
                # value pair from object_item to be passed to the __init__()
                # method of the class identified by class_name
                self.new(eval(class_name)(**obj_item))
        except FileNotFoundError:
            pass
