#!/usr/bin/python3

import cmd

class MyConsole(cmd.Cmd):
    prompt = "(hbnb) "
    pass

if __name__ == "__main__":
    MyConsole().cmdloop()