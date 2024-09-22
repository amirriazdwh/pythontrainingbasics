"""
#########################################
python variables and assignments.
########################################

in python all the variable which are created in a program must be assigned a value.
otherwise  # This will raise a NameError: name 'my_variable' is not defined.   means variable are not create.
in python creation of variable requires assignment which determine its class type.  like int() class,  fload, String or None
and a value
---
del my_var will delete object type as well as variable name from dictionary.  so it give error  NameError: name
'my_variable' is not defined.  when you try to print('my_variable')
--
my_var=None just delete object but keeps the variable name in dictionary.  in this case my_var type is None.
previous object type memory reference is released.  its been put to Garbadge collector for cleanup.

to find a variable is None.   we use.
my_var is None.   my_var==None is not prefered.

Avoiding Ambiguity: Using == can be ambiguous if my_var is an object type that defines its own __eq__ method,
potentially leading to unexpected behavior. if __eq__ method is not override.   my_var==None compare None class load memory
address with my_var memory address which should be same.  as None is singlton class and my_var is None.  it ensure the
object override function __eq__ is not evoked.  thats why its safe

global x call in a function access the global variable in that module which is in global area of that module.
nonlocal x access call in inner function access the outter function x variable.

When you assign None to a variable in Python, the variable’s datatype is NoneType, None is a singleton object in python
None is a special constant in Python that represents the absence of a value or a null value.
It is an object of its own datatype, NoneType.


##################################################################################
Underscore in python and how underscore defines variable scope
Note: _ only highlight variable protection by syntax.
##################################################################################
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


Example and Details
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


Identifiers variable rules.
-------------
. Allowed Characters
Identifiers can include letters (a-z, A-Z), digits (0-9), and underscores (_).
Identifiers must begin with a letter or an underscore.

. Case Sensitivity
Names and identifiers are case sensitive. For example, Variable and variable are different identifiers.

.Length of Identifiers
Identifiers can be of unlimited length.

.Special Name Classes
Single Leading Underscore (_variable): Suggests a “private” method or variable name.
These are not imported when you use from module import *.
Single Trailing Underscore (variable_): Used to avoid conflicts with Python keywords (e.g., class_).
Double Leading Underscores (__variable): Used in class definitions to cause name mangling (weak hiding) private variable.
This is not often used.

. Naming Conventions
Modules and Packages: Use all lower case (e.g., mymodule).
Globals and Constants: Use upper case (e.g., CONSTANT_VALUE).
Classes: Use CamelCase with an initial upper case letter (e.g., MyClass).
Methods and Functions: Use all lower case with words separated by underscores (e.g., my_function).
Local Variables: Use lower case with underscores between words (e.g., local_variable) or camelCase with an initial
lower case letter (e.g., localVariable), depending on your preference.
"""
