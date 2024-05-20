#!/usr/bin/python3
import cmd
import re
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage

class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""
    prompt = '(hbnb) '

    def default(self, line):
        """Override the default method to handle custom commands"""
        match = re.fullmatch(r"(\w+)\.(\w+)\((.*)\)", line)
        if match:
            class_name, method_name, params = match.groups()
            params = params.strip("\"'")
            if method_name == "all":
                self.do_all(class_name)
            elif method_name == "count":
                self.do_count(class_name)
            elif method_name == "show":
                self.do_show(f"{class_name} {params}")
            elif method_name == "destroy":
                self.do_destroy(f"{class_name} {params}")
            elif method_name == "update":
                attr_match = re.fullmatch(r'(\S+),\s*(\{.*\})', params)
                if attr_match:
                    obj_id, attr_dict = attr_match.groups()
                    attr_dict = json.loads(attr_dict.replace("'", '"'))
                    self.do_update(f"{class_name} {obj_id}", attr_dict)
                else:
                    self.do_update(f"{class_name} {params}")
            else:
                print(f"*** Unknown syntax: {line}")
        else:
            print(f"*** Unknown syntax: {line}")

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id"""
        if not arg:
            print("** class name missing **")
            return
        try:
            cls = globals()[arg]
            new_instance = cls()
            new_instance.save()
            print(new_instance.id)
        except KeyError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        cls_name, cls_id = args
        try:
            cls = globals()[cls_name]
        except KeyError:
            print("** class doesn't exist **")
            return
        key = f"{cls_name}.{cls_id}"
        obj = storage.all().get(key)
        if obj:
            print(obj)
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        cls_name, cls_id = args
        try:
            cls = globals()[cls_name]
        except KeyError:
            print("** class doesn't exist **")
            return
        key = f"{cls_name}.{cls_id}"
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name"""
        if arg:
            try:
                cls = globals()[arg]
                objs = [str(obj) for key, obj in storage.all().items() if key.startswith(arg)]
            except KeyError:
                print("** class doesn't exist **")
                return
        else:
            objs = [str(obj) for obj in storage.all().values()]
        print(objs)

    def do_count(self, arg):
        """Retrieves the number of instances of a class"""
        try:
            cls = globals()[arg]
            count = sum(1 for key in storage.all() if key.startswith(arg))
            print(count)
        except KeyError:
            print("** class doesn't exist **")

    def do_update(self, arg, attr_dict=None):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        if attr_dict is None:
            args = arg.split()
            if len(args) < 1:
                print("** class name missing **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return

            cls_name, cls_id, attr_name, attr_value = args
            try:
                cls = globals()[cls_name]
            except KeyError:
                print("** class doesn't exist **")
                return

            key = f"{cls_name}.{cls_id}"
            obj = storage.all().get(key)
            if not obj:
                print("** no instance found **")
                return

            # Convert the attribute value to its correct type
            if hasattr(obj, attr_name):
                attr_type = type(getattr(obj, attr_name))
                try:
                    attr_value = attr_type(attr_value)
                except ValueError:
                    print("** value type error **")
                    return

            setattr(obj, attr_name, attr_value)
            obj.save()
        else:
            args = arg.split()
            cls_name, cls_id = args
            try:
                cls = globals()[cls_name]
            except KeyError:
                print("** class doesn't exist **")
                return

            key = f"{cls_name}.{cls_id}"
            obj = storage.all().get(key)
            if not obj:
                print("** no instance found **")
                return

            for attr_name, attr_value in attr_dict.items():
                if hasattr(obj, attr_name):
                    attr_type = type(getattr(obj, attr_name))
                    try:
                        attr_value = attr_type(attr_value)
                    except ValueError:
                        print(f"** value type error for attribute {attr_name} **")
                        continue
                setattr(obj, attr_name, attr_value)
            obj.save()

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
