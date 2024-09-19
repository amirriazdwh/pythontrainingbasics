"""
Note:  Python support the following import statement types.
1.  import module   e.g    import math.    math is an object so you can access math object funcitons as math.sqrt.
2.  from module import funciton.
3.  from module import *
4   import module as m

for further understand see Python module advance.

When you start a Python program using a command like python calc.py, the Python runtime environment creates a process (called the interpreter).
The Python interpreter finds the specified file, creates a module object from it, registered it to sys.module and loads it into memory.
This loading of module create a global namespace.  at the time of loading python provides each module a name.  which is represented by
__name__ variable.   since this module is passed to interpreter through python.exe,  pythin name this module __main__
thats why we code if __name__=="__main__":  in python main module.  all the other modules were name by their file name
for example math module is name as __name__=="__math__".  in python all modules have a global namespace.  here for example main has
as global namespace as well as math.  when we specify import math.   we link main global namespace with math.  therefore the
more imports we have in main module the more global namespace are attached with it.   this can be verified by running global()
which show the main module namespace.  it will look like this if math is imported.

dict_keys(['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__annotations__', '__builtins__', 'math'])

in case of multiple imports.
Names in the global namespace:
dict_keys(['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__annotations__', '__builtins__', 'math', 'os', 'sys'])

note that import keyword takes the object type refrence and register it in main global namespace.
so
form math import sqrt

only registers the function reference with its name in global namespace.   therefore it can be accessed without any prefix in main.
while

import math.   registers math module object in main global namespace.  so sqrt function has to be accessed as main.sqrt()
----------------------------------------------------------------------------------------------------------------------------------------
before loading main module, Python automatically imports built-in modules and makes them available under the __builtins__ key.
builtin moduels are loaded into builtin namespace.  they are first module to be laoded after the interpreter process starts.
All the types, classes, and functions from the built-in modules are loaded into memory.
----------------------------------------------------------------------------------------------------------------------------------------

so python program structure is as under:
main module -> imported class module -> imported classes and function    this is in case of import math statement.
in case of
from math import sqrt
main module -> sqrt

dir(math) provides function, classes of math module not the math module global namespace.

__main__ module
Imported modules
Classes and variables Functions

"""