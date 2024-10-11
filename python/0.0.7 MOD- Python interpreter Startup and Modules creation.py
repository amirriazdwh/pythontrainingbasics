"""
Note:  Python support the following import statement types.
1.  import module   e.g    import math.    math is an object so you can access math object funcitons as math.sqrt.
2.  from module import funciton.
3.  from module import *
4   import module as m
5.  python __

for further understand see Python module advance.

When you start a Python program using a command like python calc.py, the Python runtime environment creates a process (called the interpreter).
The Python interpreter finds the specified file, creates a module object from it, registered it to sys.module and loads it into memory.
This loading of module create a global namespace.  at the time of loading python provides each module a name.  which is represented by
__name__ variable.   since this module is passed to interpreter through python.exe,  pythin name this module __main__
thats why we code if __name__=="__main__":  in python main module.  all the other modules were name by their file name
for example math module is name as __name__=="__math__".  in python all modules have a global namespace.  here for example main has
a global namespace as well as math.  when we specify import math.   we link main global namespace with math global namespace.  therefore the
more imports we have in main module the more global namespace are attached with it.   this can be verified by running global()
which show the main module namespace.  it will look like this if math is imported.

dict_keys(['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__annotations__', '__builtins__', 'math'])

in case of multiple imports.
Names in the global namespace:
dict_keys(['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__annotations__', '__builtins__', 'math', 'os', 'sys'])

Note: that import keyword takes the module create a object type reference and register it in main global namespace with a name.
it does the same thing when we only import function.  from module it takes the function,  creates function object refrence and
store it in main module directory with function name.
so
form math import sqrt

only registers the function object reference with main global namespace.   therefore it can be accessed without any prefix in main.
while

from math import sqrt

# Now you can use sqrt directly
result = sqrt(16)
print(result)  # Output: 4.0

{
    '__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7f8b8c0>,
     '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'sqrt': <built-in function sqrt>,
      'number': 16, 'result': 4.0, 'print': <built-in function print>
}


import math.   registers math module object in main global namespace.  so sqrt function has to be accessed as main.sqrt()
----------------------------------------------------------------------------------------------------------------------------------------
before loading main module, Python automatically imports built-in modules and makes them available under the __builtins__ key.
builtin moduels are loaded into builtin namespace.  they are first module to be laoded after the interpreter process starts.
All the types, classes, and functions from the built-in modules are loaded into memory.
----------------------------------------------------------------------------------------------------------------------------------------

so python program structure is as under:
main module namespace -> imported module namespace-> imported classes and function    this is in case of import math statement.

in case of
from math import sqrt
main module -> sqrt

dir(math) provides function, classes of math module from module specification.  it does not provide this information from
module namespace or main module namespace.

''

"""

"""
The __init__.py file in a Python package serves several important purposes:

Package Initialization: It indicates to Python that the directory should be treated as a package. This is essential for the 
package to be importable.

Initialization Code: You can include code in __init__.py that runs when the package is imported. This can be useful for 
setting up package-level variables or performing other initialization tasks.

Namespace Definition: It helps define the package’s namespace. You can use it to import specific modules or functions into 
the package’s namespace, making them easier to access.

Subpackage Inclusion: If your package contains subpackages, each subpackage should also have its own __init__.py file 
to be recognized as a package.

Control Imports: By setting the __all__ variable, you can control what is imported when someone uses from package import *.
In Python versions 3.3 and later, the __init__.py file is not strictly required to define a package, but it is still 
commonly used for the reasons mentioned above
"""