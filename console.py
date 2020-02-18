#!/usr/bin/python3
""" Program that contains the entry point of the command interpreter """
import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """ init Command Prompt """
    prompt = "(hbnb) "
    lavel =  {"BaseModel", "City", "State"
              "User", "Place", "Review", "Ameity"}

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
        """Create a instance of BaseModel"""
        if len(line) == 0:
            print("** class name missing **")
            return None
        elif line not in HBNBCommand.lavel:
            print("** class name missing **")
            return None
        else:
            my_inst = eval(line + "()")
            my_inst.save()
            print my_inst.id

    def do_show(self, line):
        """Prints the string representation of
        an instance based on the class name and id"""
        if len(line) == 0:
            print("** class name missing **")
            return None
        n = parse(line)
        if ar[0] not in HBNBCommand.lavel:
            print("** class doesn't exist **")
            return None
        try:
            if n[1]:
                ite = "{},{}".format(n[0], n[1])
                if ite not in storage.all().keys():
                    print("** no instance found **")
                else:
                    print(storage.all()[ite])
        except IndexError:
            print("** instance id missing **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        if len(line) == 0:
            print("** class name missing **")
            return None
        n = parse(line)
        if ar[0] not in HBNBCommand.lavel:
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
        n = parse(line)
        my_obj = []
        if len(line) == 0:
            for ite in storage.all().value():
                my_obj.append(ite)
            print my_obj
        elif n[0] in HBNBCommand.lavel:
            if n [0] in key:
                my_obj.append(ite)
            else:
                print("** class doesn't exist **")


    def do_update(self, line)
    """Updates an instance based on the class name and id"""


if __name__ == '__main__':
    HBNBCommand().cmdloop()
