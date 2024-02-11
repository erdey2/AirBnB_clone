#!/usr/bin/python3
"""AirBnB command line module."""
from cmd import Cmd


class HBNBCommand(Cmd):
    """Command line imp class."""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True
    
    def do_EOF(self, arg):
        """implement EOF."""
        print('')
        return True
    
    def emptyline(self):
        """privent execution."""
        pass
if __name__ == '__main__':
    HBNBCommand().cmdloop()
