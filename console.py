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

    def do_create(self, arg):
        """Creates new instance of the class
        """
        if not arg:
            print("** class name missing **")
            return
        my_data = shlex.split(arg)
        if my_data[0] not in HBNBCommand.index.keys():
            print("** class doesn't exist **")
            return
        new_instance = HBNBCommand.index[my_data[0]]()
        new_instance.save()
        print(new_instance.id)

    def do_destroy(self, arg):
        """
        removes and destroys an entry
        """
        tokens = shlex.split(arg)
        if len(tokens) == 0:
            print("** class name missing **")
            return
        if tokens[0] not in HBNBCommand.my_dict.keys():
            print("** class doesn't exist **")
            return
        if len(tokens) <= 1:
            print("** instance id missing **")
            return
        storage.reload()
        objs_dict = storage.all()
        key = tokens[0] + "." + tokens[1]
        if key in objs_dict:
            del objs_dict[key]
            storage.save()
        else:
            print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()



