"""
Underscores in Python- Single Leading Underscore (_var):
    - Purpose: Indicates a name is meant for internal use.
    - Usage: Treated as a non-public part of the API. It’s a hint for programmers and not enforced by Python.
    - Example: _internal_function()
    - Import Behavior: Not imported with from module import *.
- Double Leading Underscore (__var):
    - Purpose: Triggers name mangling to avoid name conflicts in subclasses.
    - Usage: Makes a variable or method private within a class.
    - Example: __private_method()
    - Name Mangling: __var in class Test becomes _Test__var.
- Single Trailing Underscore (var_):
    - Purpose: Used to avoid naming conflicts with Python keywords.
    - Example: class_ = 'MyClass'
- Double Leading and Trailing Underscore (var):
    - Purpose: Indicates special methods defined by Python (dunder methods).
    - Usage: Used for object initialization, operator overloading, etc.
    - Example: __init__, __add__, __iter__
- Single Underscore (_) as a Variable:
    - Purpose: Used for temporary or insignificant variables.
    - Example: for _ in range(10):
- Single Underscore (_) in the Interactive Shell:
    - Purpose: Contains the result of the last evaluated expression.
- non underscore means:  variable or method is public 

- Example:
>>> 1 + 2
3
>>> _ + 4
7

ExamplesUsing Underscores in Variables and Methods
class Person:
    def __init__(self):      #dunder methods
        self.name = 'Sarah'  # Public variable
        self._age = 26       # Protected variable
        self.__id = 30       # Private variable

p = Person()
print("Public variable:", p.name)
print("Protected variable:", p._age)
print("Private variable (accessed via name mangling):", p._Person__id)

Using Underscores in Loops and Assignments
x = (11, 12, 1, 3)
_, _, _, c = x
(*b, _) = x
print(b, c)

for _ in range(len(x)):
    print("looping")

    
############################################################################ 
Key Points to Remember-
python has 4 types of namespace.

1. Built-in Namespace: Initialized when the Python interpreter starts. it loads the buildin module of python builtin.py and other moduel to
   provide acess to print functions etc
2. Global Namespace: Initialized when a module or python file is loaded.  all modules are first registered in sys.modules  then a global name space
   for that module is created which contains its variable, class and functions.  each module has its own namespace.
   When mymodule is imported, it creates its own global namespace containing global_var and greet. when you create a variable in function with
   keyword global var.  it gets created in mobule global_var area.
   Using del mymodule deletes the reference to the module, effectively removing its global namespace and so is the global variable in module
   Accessing After Deletion: Attempting to access mymodule after deletion raises a NameError because the module is no longer defined.


3. Enclosing Namespace: Created dynamically when a nested function is called.
4. Local Namespace: Created dynamically when a function is called

 _var: Protected (internal use in class, module or in any object).   it can be accessed as object._varS.

 __var: Private (name in class, module or in any object). it can object._mymodule_var
 in a function, there can be private variable and global variables.  if a function has inner function
 which wants to access the outter function variable it uses nonlocal keyword which appends the outter function
 name and make it accessable in inner funciton.  any variable you want to declare as global are created by global keyword.
 global variables are
var_: Avoids naming conflicts with reserved words.
_var_: Special methods (dunder methods).
- _: Temporary variable or last result in the shell.
#############################################################################
"""
