#!/usr/bin/python3
"""
Contains the FileStorage class
"""
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class FileStorage:
    """serialises instances"""

    # string - path to the JSON file
    __file_path = "file.json"
    # dictionary - empty but will store all objects by <class name>.id
    __objects = {}

    def all(self):
        """Shows objs"""
        return self.__objects

    def new(self, obj):
        """Does new"""
        if obj is not None:
            i = obj.__class__.__name__ + "." + obj.id
            self.__objects[i] = obj

    def save(self):
        """Does new  save"""
        json_objects = {}
        for i in self.__objects:
            json_objects[i] = self.__objects[i].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """Undoes it"""
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for i in jo:
                self.__objects[i] = classes[jo[i]["__class__"]](**jo[i])
        except:
            pass


