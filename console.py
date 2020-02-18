#!/usr/bin/python3


""" Program that contains the entry point of the command interpreter """
import cmd


class HBNBCommand(cmd.Cmd):
    """ init Command Prompt """
    prompt = "(hbnb) "

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
        """Create a instance by the user"""
        if len(line) == 0:
            print("** class name missing **")
        elif line not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            inst = eval(line)()
            inst.save()
            print(inst.id)

    def do_show(self, line):
        """Prints the string representation of
        an instance based on the class name and id"""
        if len(line) == 0:
            print("** class name missing **")
            return
        ar = parse(line)

        if ar[0] is not HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        try:
            if ar[1]:
                n = "{}.{}".format(ar[0], ar[1])
                if n is not in storage.all().key():
                    print("** no instance found **")
                else:
                    print storage.all()[n]
        except IndexError:
            print("** instance id missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
