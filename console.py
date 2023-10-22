#!/usr/bin/python3
"""
Console module for the command-line interpreter.
"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program on EOF (Ctrl-D).
        """
        print("")  # Print a newline before exiting
        return True

    def emptyline(self):
        """
        Do nothing on an empty line.
        """
        pass

    def do_create(self, arg):
        """
        Create a new instance of BaseModel, User, State, City, Amenity, Place, or Review.
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]

        try:
            cls = eval(class_name)
        except NameError:
            print("** class doesn't exist **")
            return

        if len(args) > 1 and args[1].startswith("{") and args[1].endswith("}"):
            try:
                attr_dict = eval(args[1])
                if not isinstance(attr_dict, dict):
                    raise SyntaxError
            except (SyntaxError, NameError):
                print("** invalid dictionary format **")
                return
        else:
            attr_dict = {}

        new_instance = cls(**attr_dict)
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Print the string representation of an instance based on class name and id.
        """
        args = arg.split()
        valid_classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
        if not args:
            print("** class name missing **")
            return
        if args[0] not in valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()
        if key in objects:
            print(objects[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Delete an instance based on its ID.
        """
        args = arg.split()
        valid_classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
        if not args:
            print("** class name missing **")
            return
        if args[0] not in valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()
        if key in objects:
            del objects[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Print string representations of all instances or instances of a class.
        """
        args = arg.split()
        valid_classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
        if args and args[0] not in valid_classes:
            print("** class doesn't exist **")
            return
        if args:
            class_name = args[0]
            instances = storage.all().values()
            instances_of_class = [instance for instance in instances if instance.__class__.__name__ == class_name]
            output = [str(instance) for instance in instances_of_class]
            print(output)
        else:
            objects = storage.all()
            output = [str(obj) for obj in objects.values()]
            print(output)

    def do_update(self, arg):
        """
        Update an instance's attributes.
        """
        args = arg.split()
        valid_classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
        if not args:
            print("** class name missing **")
            return
        if args[0] not in valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj = objects[key]
        setattr(obj, args[2], args[3])
        obj.save()

    def do_count(self, arg):
        """
        Count the number of instances of a class.
        """
        args = arg.split()
        valid_classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
        if not args:
            print("** class name missing **")
            return
        if args[0] not in valid_classes:
            print("** class doesn't exist **")
            return
        class_name = args[0]
        instances = storage.all().values()
        instances_of_class = [instance for instance in instances if instance.__class__.__name__ == class_name]
        count = len(instances_of_class)
        print(count)

    def do_destroy(self, arg):
        """
        Delete an instance based on its ID.
        """
        args = arg.split()
        valid_classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
        if not args:
            print("** class name missing **")
            return
        if args[0] not in valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()
        if key in objects:
            del objects[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_update(self, arg):
        """
        Update an instance's attributes.
        """
        args = arg.split()
        valid_classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
        if not args:
            print("** class name missing **")
            return
        if args[0] not in valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj = objects[key]
        setattr(obj, args[2], args[3])
        obj.save()

    def do_update(self, arg):
        """
        Update an instance's attributes.
        """
        args = arg.split()
        valid_classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
        if not args:
            print("** class name missing **")
            return
        if args[0] not in valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj = objects[key]
        setattr(obj, args[2], args[3])
        obj.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
