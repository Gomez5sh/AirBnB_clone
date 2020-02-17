#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    """init Command Prompt"""
    prompt = "(hbnb)"

    def do_EOF(self, args):
        """CTRl-D to exit"""
        print()
        return True

    def do_quit(self, args):
        """exit the program"""
        return True

    def empty_line(self):
        """ENTER shouldn’t execute anything"""
        pass
