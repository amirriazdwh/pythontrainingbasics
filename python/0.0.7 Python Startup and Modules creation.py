"""
When you start a Python program using a command like python calc.py, the Python runtime environment creates a process (called the interpreter).
The Python interpreter finds the specified file, creates a module object from it, registered it to sys.module and loads it into memory.
This loading of module create a global namespace.  at the time of loading python provides each module a name.  which is represented by
__name__ variable.   since this module is passed to interpreter through python.exe,  pythin name this module __main__
thats why we code if __name__=="__main__":  in python main module.  all the other modules were name by their file name
for example math module is name as __name__=="__math__"

before loading main module, Python automatically imports built-in modules and makes them available under the __builtins__ key.
builtin moduels are loaded into builtin namespace.  they are first module to be laoded after the interpreter process starts.
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