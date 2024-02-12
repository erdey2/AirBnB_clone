#!/usr/bin/python3
"""AirBnB command line module."""
from cmd import Cmd
import sys
import re
from shlex import split
import json
import os
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(Cmd):
    """Command line imp class."""
    prompt = '(hbnb) '
    classes = {'BaseModel': BaseModel, 'User': User, 'City': City,
            'Place': Place, 'Amenity': Amenity, 'Review': Review,
               'State': State}

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

    def do_create(self, arg):
        """create a new object."""
        if len(arg) == 0:
            print('** class name missing **')
            return
        new = None
        if arg:
            arg_list = arg.split()
            if len(arg_list) == 1:
                if arg in self.classes.keys():
                    new = self.classes[arg]()
                    new.save()
                    print(new.id)
                else:
                    print("** class doesn't exist **")

    def do_show(self, arg):
        """prints instance."""
        if len(arg) == 0:
            print("** class name missing **")
            return
        elif arg.split()[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(arg.split()) > 1:
            key = arg.split()[0] + '.' + arg.split()[1]
            if key in storage.all():
                i = storage.all()
                print(i[key])
            else:
                print("** no instance found **")
        else:
            print("** instance id missing **")

    def do_destroy(self, arg):
        """delete instance with class and id """
        if len(arg) == 0:
            print("** class name missing **")
            return
        arg_list = arg.split()
        try:
            obj = eval(arg_list[0])
        except Exception:
            print("** class doesn't exist **")
            return
        if len(arg_list) == 1:
            print('** instance id missing **')
            return
        if len(arg_list) > 1:
            key = arg_list[0] + '.' + arg_list[1]
            if key in storage.all():
                storage.all().pop(key)
                storage.save()
            else:
                print('** no instance found **')
                return

    def do_all(self, arg):
        """print all instances."""
        if len(arg) == 0:
            print([str(a) for a in storage.all().values()])
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            print([str(a) for b, a in storage.all().items() if arg in b])

    def do_all(self, arg):
        """Usage: <class>.all()
        Display string representations of all instances of a given class."""
        larg = parse(arg)
        if len(larg) > 0 and larg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            lobj = []
            for obj in storage.all().values():
                if len(larg) > 0 and larg[0] == obj.__class__.__name__:
                    lobj.append(obj.__str__())
                elif len(larg) == 0:
                    lobj.append(obj.__str__())
            print(lobj)

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        count the total number of instances."""
        larg = parse(arg)
        count = 0
        for i in storage.all().values():
            if larg[1] == i.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        """update JSON file."""
        arg = arg.split()
        if len(arg) == 0:
            print('** class name missing **')
            return
        elif arg[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(arg) == 1:
            print('** instance id missing **')
            return
        else:
            key = arg[0] + '.' + arg[1]
            if key in storage.all():
                if len(arg) > 2:
                    if len(arg) == 3:
                        print('** value missing **')
                    else:
                        setattr(
                            storage.all()[key],
                            arg[2],
                            arg[3][1:-1])
                        storage.all()[key].save()
                else:
                    print('** attribute name missing **')
            else:
                print('** no instance found **')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
