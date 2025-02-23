""""""
"""
PySys_Init function in CPython (the standard Python implementation) is responsible for initializing the sys module, 
which includes setting up sys.argv.

Here’s a more detailed breakdown of the process:

Command-Line Parsing:
When you run a Python script from the command line, the operating system’s shell parses the command into 
individual arguments. These arguments are passed to the Python interpreter as a list of strings.
When you type a command in the terminal or command prompt, the CLI (such as Bash on Linux or Command Prompt on Windows) 
interprets the input. The CLI splits the input string into individual components (arguments) based on spaces
 and other delimiters
 The CLI parses the command line into a list of strings. For example, the command:
 
python script.py arg1 arg2
splits into 
['python', 'script.py', 'arg1', 'arg2']

Initialization by PySys_Init:
During the startup of the Python interpreter, the PySys_Init function is called.
This function initializes the sys module and sets up various system-related variables, including sys.argv.

Setting sys.argv:
PySys_Init takes the list of command-line arguments and assigns it to sys.argv.
The first element of sys.argv is the name of the script being executed, and the subsequent elements are 
the additional command-line arguments.

Downstream Usage:
Once sys.argv is set up, it can be accessed by any part of the script to retrieve and use the command-line arguments.
This allows the script to behave differently based on the input provided by the user.
"""

"""
sys.exit() Function:
The sys.exit() function raises a SystemExit exception, which can be caught by surrounding code. If uncaught, 
it will terminate the program.
This function is a way to exit the program gracefully, allowing you to specify an exit status code 
(e.g., sys.exit(0) for a successful exit, sys.exit(1) for an error).
----
Process Hierarchy:
When you run a Python script, the operating system creates a new process for the Python interpreter.
This process is the “root” process for your script. If you use sys.exit() within this script, it will terminate 
this root process, effectively ending the program.

Child Processes:
If your script creates additional processes (e.g., using the multiprocessing module), these are child processes of the main 
Python interpreter process.
Calling sys.exit() in the main script will terminate the main process and, by extension, any child processes that depend on it.

this function calls sys.exit(), which raises a SystemExit exception.  if SystemExit exception is not catch by any exception
handling block.  its been finally catch by python interpreter which exits the root program process. 

Note: any exception if not handled by any exception block finally reach to interpreter which print the error message and 
then raise SystemExit exception to terminate the root program process.
Here’s a detailed explanation:

-Raising SystemExit:
When sys.exit() is called, it raises a SystemExit exception.
This exception can be caught and handled like any other exception using a try-except block.
+-
-Uncaught SystemExit:
If the SystemExit exception is not caught by any try-except block in the program, it propagates up the call stack.
Eventually, it reaches the top level of the program, where the Python interpreter catches it.

-Interpreter Handling:
When the interpreter catches the SystemExit exception, it performs cleanup operations and terminates the program.
The exit status code provided to sys.exit() (or the default code 0 if none is provided) is returned to the operating system.

Here’s an example to illustrate:-

"""

import sys
import random


def main():
    """
    This program takes 3 command line arg forms:
    1.-affirm *name*
    2. -hello *name*
    3. -n *number* *name*
    """
    # standard - load "args" list with cmd-line-args
    print(sys.argv)
    #['C:/Users/amirr/PycharmProjects/pythontraining/python/0.2Pass Variable into Main.py', '-affirm', "'name'"]
    args = sys.argv[1:]
    #['-affirm', "'name'"]
    print(args)

    if len(args) == 2 and args[0] == '-affirm':
        affirmation = random.choice(AFFIRMATIONS)
        print(affirmation, args[1])

# Python boilerplate.
if __name__ == '__main__':
    main()


"""
Method 2
another method to pass arugments is as under:
Using argparse Module:
For more complex command-line argument parsing, the argparse module is very useful.

import argparse

parser = argparse.ArgumentParser(description="A simple argument parser")
parser.add_argument("name", type=str, help="Your name")
parser.add_argument("--age", type=int, help="Your age", default=25)

args = parser.parse_args()
print(f"Hello, {args.name}! You are {args.age} years old.")

"""

"""
Method 3.
import getopt
import sys

def main(argv):
    name = ''
    age = 0
    try:
        opts, args = getopt.getopt(argv, "hn:a:", ["name=", "age="])
    except getopt.GetoptError:
        print('script.py -n <name> -a <age>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('script.py -n <name> -a <age>')
            sys.exit()
        elif opt in ("-n", "--name"):
            name = arg
        elif opt in ("-a", "--age"):
            age = int(arg)
    print(f"Name: {name}, Age: {age}")

if __name__ == "__main__":
    main(sys.argv[1:])

"""