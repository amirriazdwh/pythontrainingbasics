"""
When you start a Python program using a command like python calc.py, the Python runtime environment creates a process (called the interpreter).
The Python interpreter finds the specified file, creates a module object from it, and loads it into memory. This module object represents the global
scope of the program.

Python automatically imports built-in modules and makes them available under the __builtins__ key. This is known as the built-in scope.
 All the types, classes, and functions from the built-in modules are loaded into memory.

Similarly, Python creates namespaces for classes and functions. In Python, the __main__ module is the top-level module, while imported modules fall
below it. All modules contain dictionary objects. For example, when a module is loaded, its dictionary is created, linking variables, classes,
and functions within that module.

A class in Python contains a dictionary that holds its static variables and methods. When a function is loaded, its methods can be inherited by subclasses.
 The hierarchy is as follows:

__main__ module
Imported modules
Classes and variables
Functions

"""