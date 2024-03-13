#!/usr/bin/python3
"""
Import files
"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.place import Place
from models.review import Review
import json
import shlex
from models.city import City
from models.amenity import Amenity


class HBNBCommand(cmd.Cmd):
    """ prompt fo air bnb app """
    prompt = '(hbnb)'
    my_dict = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
            }

    def do_nothing(self, arg):
        """ nothing """
        pass

    def do_quit(self, arg):
        """ Close save data """
        return True

    def do_EOF(self, arg):
        """ Close program     """
        print("")
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        """ Creates a new instance of the basemodel class
        Structure: create [class name]
        """
        if not arg:
            print("** class name missing **")
            return
        my_data = shlex.split(arg)
        if my_data[0] not in HBNBCommand.my_dict.keys():
            print("** doesn't exist **")
            return
        entry = HBNBCommand.my_dict[my_data[0]]()
        entry.save()
        print(entry.id)

    def do_show(self, arg):
        """
        Shows an entry
        """
        token = shlex.split(arg)
        if len(token) == 0:
            print("** class name missing **")
            return
        if token[0] not in HBNBCommand.my_dict.keys():
            print("**class doesn't exist **")
            return
        if len(token) <= 1:
            print("** instance id missing **")
            return
        storage.reload()
        objs_dict = storage.all()
        safoa = token[0] + "." + token[1]
        if safoa in objs_dict:
            obj_instance = str(objs_dict[safoa])
            print(obj_instance)
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name
        and id (save the change into the JSON file)
        """
        tokens = shlex.split(arg)
        if not tokens:
                print("** class name missing **")
                return

        class_name = tokens[0]
        if class_name not in HBNBCommand.my_dict:
            print("** class doesn't exist **")
            return

        if len(tokens) <= 1:
            print("** instance id missing **")
            return

        storage.reload()
        objs_dict = storage.all()
        key = f"{class_name}.{tokens[1]}"
        if key in objs_dict:
            del objs_dict[key]
            storage.save()
        else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        #show everthtinh
        storage.reload()
        my_json = []
        objects_dict = storage.all()
        if not arg:
            for i in objects_dict:
                my_json.append(str(objects_dict[i]))
            print(json.dumps(my_json))
            return
        token = shlex.split(arg)
        if token[0] in HBNBCommand.my_dict.keys():
            for key in objects_dict:
                if token[0] in i:
                    my_json.append(str(objects_dict[i]))
            print(json.dumps(my_json))
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Updates an instance based on the class name and
        id 
        """
        if not arg:
            print("** class name missing **")
            return
        inputs = shlex.split(arg)
        storage.reload()
        objs_dict = storage.all()
        if inputs[0] not in HBNBCommand.my_dict.keys():
            print("** class doesn't exist **")
            return
        if (len(inputs) == 1):
            print("** instance id missing **")
            return
        try:
            i = inputs[0] + "." + inputs[1]
            objs_dict[i]
        except KeyError:
            print("** no instance found **")
            return
        if (len(inputs) == 2):
            print("** attribute name missing **")
            return
        if (len(inputs) == 3):
            print("** value missing **")
            return
        event = objs_dict[i]
        if hasattr(event, inputs[2]):
            data_type = type(getattr(event, inputs[2]))
            setattr(event, inputs[2], data_type(inputs[3]))
        else:
            setattr(event, inputs[2], inputs[3])
        storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
