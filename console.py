#!/usr/bin/python3
"""
interactive console for my airbnb 
"""
import cmd
from models.base_model import BaseModel
from models import storage
import shlex
import json
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.city import City

class HBNBCommand(cmd.Cmd):
    """ prompt to access Airbnb """
    prompt = '(hbnb)'
    index = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
            }
    def do_nothing(self, arg):
        """nothing"""
        pass

    def do_emptyline(self):
    """skips the empty line function"""
    pass 

    def do_quit(self, arg):
        return True

    def do_EOF(self,arg):
        print("")
        return True
   




