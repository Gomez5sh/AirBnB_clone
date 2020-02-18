#!/usr/bin/python3
""" Program that contains the entry point of the command interpreter """
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place
from models import storage


class HBNBCommand(cmd.Cmd):
    """ init Command Prompt """
    prompt = "(hbnb) "
    level = {"BaseModel", "City", "State"
             "User", "Place", "Review", "Amenity"}

    def do_EOF(self, args):
        """CTRl-D to exit\n"""
        print()
        return True

    def do_quit(self, args):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """ENTER shouldn’t execute anything"""
        pass

    def do_create(self, line):
        """Create a new instance of BaseModel"""
        if not line:
            print("** class name missing **")
            return None
        elif (line not in self.level):
            print("** class doesn't exist **")
            return None
        else:
            my_inst = eval(line + "()")
            my_inst.save()
            print(my_inst.id)

    def do_show(self, line):
        """Prints the string representation of
        an instance based on the class name and id"""
        # First, separate in a list the commands by white space
        n = line.split()
        if not line:
            print("** class name missing **")
            return None
        elif (n[0] not in self.level):
            print("** class doesn't exist **")
            return None
        elif len(n) == 1:
            print("** instance id missing **")
            return None
        else:
            # concatenate class_name and id with a dot
            key = "{}.{}".format(n[0], n[1])
            # search in file json the key saved in key
            if key not in storage.all().keys():
                print("** no instance found **")
            else:
                obj = storage.all()
                # string representation of the instance with class name and id
                print(obj[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        if len(line) == 0:
            print("** class name missing **")
            return None
        n = line.split()
        if ar[0] not in HBNBCommand.level:
            print("** class doesn't exist **")
            return None
        try:
            if n[1]:
                ite = "{},{}".format(n[0], n[1])
                if ite not in storage.all().keys():
                    print("** no instance found **")
                else:
                    del storage.all()[ite]
                    storage.save()
        except IndexError:
            print("** instance id missing **")

    def do_all(self, line):
        """Prints all string representation of
        all instances based or not on the class name."""
        n = line.split()
        my_obj = []
        if len(line) == 0:
            for ite in storage.all().value():
                my_obj.append(ite)
            print(my_obj)
        elif n[0] in HBNBCommand.lavel:
            if n[0] in key:
                my_obj.append(ite)
            else:
                print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
