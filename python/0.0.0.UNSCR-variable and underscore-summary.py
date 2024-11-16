"""
#########################################
python variables and assignments.
########################################

in python all the variable which are created in a program must be assigned a value.
otherwise  # This will raise a NameError: name 'my_variable' is not defined.  error  means variable are not create but why?.
in python creation of variable requires assignment which determine its class type.  like int() class,  fload, String or None
and a value.  at runtime python find the variable class type.  create the variable name "my_variable" in namespace of module
then create an object of that class type.  registers object's memory refrence to my_varable in dictionary and then the variable
is created.  without assigning the variable value all this process cannot occur

#####################
Deletion of variable
#####################
del my_var will delete object type as well as variable name from dictionary.  so if the variable is printed again after deletion
 it will give error  NameError: name 'my_variable' is not defined.  when you try to print('my_variable')
--
my_var=None just delete object but keeps the variable name in dictionary.  in this case my_var type is None.
previous object type memory reference is released.  its been put to Garbadge collector for cleanup.

if you just only want to delete the object memory refrence without deleting the variable defined in dictionary.  you simply
assign None to variable

x=None.

this decrement the variable reference count in variable x's object and assign it static object NoneType memory reference.
the python virtual machine memory manager will clear old object as its reerence count is 0

##################################
Find weather a variable is None
##################################
to find a variable is None.   we use.
my_var is None.   my_var==None is not prefered.

The use of == for comparisons can be ambiguous, especially if my_var is an instance of a custom object that has its own __eq__ method
defined. When you use ==, Python will call the __eq__ method of that object, which could lead to unexpected behavior if it’s not
implemented properly. However, when checking if a variable is None, it’s much safer to use the is operator (e.g., if my_var is None:).
This is because None is a singleton in Python, meaning there’s only one instance of None in memory. The is operator checks whether
my_var and None refer to the exact same object in memory, bypassing any custom __eq__ methods that might be defined. This ensures
that the comparison is reliable and not affected by any overridden behavior. Therefore, for clarity and correctness, it’s best to
use is rather than == when checking for None.:

When you assign None to a variable in Python, the variable’s datatype is NoneType, None is a singleton object in python
None is a special constant in Python that represents the absence of a value or a null value.
It is an object of its own datatype, NoneType.

################
Global X calls
################
in python a global variable in module is accessable to all the functions and classes in that module. however,  function
and classes cannot reassign the value of global variable.  this does not mean what global variable is immutable.  global
variable can be immutable or mutable based on variable types.  however, it cannot be resigned a value without a global call.


x = 10  # Global variable, let's say it's at memory address 0x1000

def modify_variable():
    global x       # Tell Python to use the global 'x' (memory address 0x1000)
    print(f"Before modification, x = {x}, address = {id(x)}")
    x = 20         # This modifies the value at the same address (0x1000)
    print(f"After modification, x = {x}, address = {id(x)}")

print(f"Initially, x = {x}, address = {id(x)}")
modify_variable()
print(f"After function call, x = {x}, address = {id(x)}")

output with immutable variable
----------------------------------------------------------------
Initially, x = 10, address = 140179207636544
Before modification, x = 10, address = 140179207636544
After modification, x = 20, address = 140179207636864
After function call, x = 20, address = 140179207636864
-------------------------------------------------------------------
my_list = [1, 2, 3]  # Global variable (a list)

def modify_list():
    global my_list  # Required to reassign a new list to the global variable
    print(f"Before reassignment, my_list = {my_list}, address = {id(my_list)}")
    # Assigning a new list to 'my_list'
    my_list = [4, 5, 6]  # This creates a new list and reassigns 'my_list'
    print(f"After reassignment, my_list = {my_list}, address = {id(my_list)}")

print(f"Initially, my_list = {my_list}, address = {id(my_list)}")
modify_list()
print(f"After function call, my_list = {my_list}, address = {id(my_list)}")

output with mutable variable -------------------------------------------
Initially, my_list = [1, 2, 3], address = 140517279715072
Before reassignment, my_list = [1, 2, 3], address = 140517279715072
After reassignment, my_list = [4, 5, 6], address = 140517279717184
After function call, my_list = [4, 5, 6], address = 140517279717184
-------------------------------------------------------------------------
so when a new assigned is conducted through global x declaring in that funciton.  a new object refrence is assigned
to that the variable. however,  the variable like list items is updated. global x is not needed.

my_list = [1, 2, 3]  # Global variable (a list)

def modify_list():
    # No need to use 'global' here because we're modifying the list in place
    print(f"Before modification, my_list = {my_list}, address = {id(my_list)}")
    my_list.append(4)  # Modify the list in place
    print(f"After modification, my_list = {my_list}, address = {id(my_list)}")

print(f"Initially, my_list = {my_list}, address = {id(my_list)}")
modify_list()
print(f"After function call, my_list = {my_list}, address = {id(my_list)}")

Initially, my_list = [1, 2, 3], address = 140517279715072
Before modification, my_list = [1, 2, 3], address = 140517279715072
After modification, my_list = [1, 2, 3, 4], address = 140517279715072
After function call, my_list = [1, 2, 3, 4], address = 140517279715072

################
nonlocal x
################
The nonlocal keyword is used to modify variables in the enclosing function’s scope.
It is useful for nested functions where you want to modify the state of a variable defined in an outer function.
nonlocal is needed because without it, Python treats variables in a nested function as local to that function,
unless they are declared as global.

def outer_function():
    x = 5  # Variable in the enclosing scope

    def inner_function():
        nonlocal x  # Refer to the 'x' in the outer function
        print(f"Before modification: x = {x}")
        x = 10  # Modify the variable from the enclosing scope
        print(f"After modification: x = {x}")

    print(f"Initially, x = {x}")
    inner_function()
    print(f"After inner_function call, x = {x}")

outer_function()

Initially, x = 5
Before modification: x = 5
After modification: x = 10
After inner_function call, x = 10   # nonlocal x let you modify the outfunction x=5 to x=10

however,  without nonloca x declaration. in inner_funciton a new x variable is created with value 10 and discarded
when the function call is over

def outer_function():
    x = 5  # Variable in the enclosing scope

    def inner_function():
        x = 10  # This creates a new local variable 'x'
        print(f"Inside inner_function: x = {x}")

    print(f"Initially, x = {x}")
    inner_function()
    print(f"After inner_function call, x = {x}")

outer_function()

Initially, x = 5
Inside inner_function: x = 10
After inner_function call, x = 5   # x=10 is discarded.

##################################################################################
Underscore in python and how underscore defines variable scope
Note: _ only highlight variable protection by syntax.
##################################################################################
 _var: Protected (internal use in class, module or in any function).   it can be accessed as object._varS.
 __var: Private (name in class, module or in any object). it can be accessed as object._mymodule_var
var_: Avoids naming conflicts with reserved words.
_var_: Special methods (dunder methods).   these are the system function defined in python language.  which can be
constructor, destructor,  special function call trasparent to programmer like in memory management context
- _: Temporary variable or last result in the shell.
#############################################################################

#####################
Example and Details
#####################
Underscores in Python- Single Leading Underscore (_var):
    - Purpose: Indicates a name is meant for internal use.
    - Usage: Treated as a non-public part of the API. It’s a hint for programmers and not enforced by Python.
    - Example: _function().  _x etc.
    - Import Behavior: Not imported with from module import *.
- Double Leading Underscore (__var):
    - Purpose: Triggers name mangling to avoid name conflicts in subclasses.
    - Usage: Makes a variable or method private within a class.
    - Example: __private_method().  here private is a class and __method is a function defined inside it
    - Name Mangling: __var in class Test becomes _Test__var.
- Single Trailing Underscore (var_):
    - Purpose: Used to avoid naming conflicts with Python keywords.
    - Example: class_ = 'MyClass'
- Double Leading and Trailing Underscore (var):
    - Purpose: Indicates special methods defined by Python (dunder methods).
    - Usage: Used for object initialization, operator overloading, etc.
    - Example: __init__, __add__, __iter__
- Single Underscore (_) as a Variable.  anonymous varaible
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
#####################################
Example use of underscore function
#####################################

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
    print(_)

When used as a variable, _ is indeed part of the namespace.  means that value of _ is stored in namespace
and can be accessed like any other variable.
However, its special uses, especially in the interactive interpreter and as a convention for ignoring values,
make it unique.

############################
Identifiers variable rules(Allowed Characters)
############################
Identifiers can include letters (a-z, A-Z), digits (0-9), and underscores (_).
Identifiers must begin with a letter or an underscore.

Case Sensitivity
-----------------
Names and identifiers are case sensitive. For example, Variable and variable are different identifiers.

Length of Identifiers
-------------------------
Identifiers can be of unlimited length.

#########################
underscore variable summary
#########################
Single Leading Underscore (_variable): Suggests a “private” method or variable name.
These are not imported when you use from module import *.
Single Trailing Underscore (variable_): Used to avoid conflicts with Python keywords (e.g., class_).
Double Leading Underscores (__variable): Used in class definitions to cause name mangling (weak hiding) private variable.
dunder method               __Init__  special methods. they are operators,  override methods which are part of based class
                                       or abstract class.  the methods like __init__ , __iter__ are called by compiler
                                       implicitly

##########################
Naming Conventions
##########################
Modules and Packages: Use all lower case (e.g., mymodule).
Globals and Constants: Use upper case (e.g., CONSTANT_VALUE).
Classes: Use CamelCase with an initial upper case letter (e.g., MyClass).
Methods and Functions: Use all lower case with words separated by underscores (e.g., my_function).
Local Variables: Use lower case with underscores between words (e.g., local_variable) or camelCase with an initial
lower case letter (e.g., localVariable), depending on your preference.
"""

"""
#########################
variable by reference 
###########################
In Python, variables are assigned by reference because of the way Python manages memory. Here’s a detailed explanation of how and 
why Python uses this approach:

1. Understanding Assignment by Reference:
When you assign a variable in Python, you're not copying the value itself but rather assigning a reference (or pointer) to the
object in memory. The variable is essentially a label that refers to an object, not the object itself. Here's how it works:

Mutable vs. Immutable objects:
Immutable objects (e.g., integers, strings, tuples): If you assign one variable to another like

x=10
y=x 

both variables will refer to the same object. However, since the object cannot be changed (it's immutable), 
if you perform an operation that modifies the value, Python will create a new object and the new reference will point to that.

Mutable objects (e.g., lists, dictionaries, sets): If you assign one variable to another, both variables will point to the same 
object in memory. If you modify the object using one variable, the changes will be visible through the other variable because 
they share the same reference.

Example of assignment by reference:
# Immutable object example (integers)
x = 10
y = x
y += 1
print(x)  # x is still 10, because integers are immutable
print(y)  # y is now 11

# Mutable object example (lists)
a = [1, 2, 3]
b = a
b.append(4)
print(a)  # a is [1, 2, 3, 4] because lists are mutable and b modified the shared reference
print(b)  # b is [1, 2, 3, 4]

Why is this approach used?
Efficiency: Passing references rather than copying entire objects is more memory-efficient and faster, especially for large or 
complex objects like lists and dictionaries. It avoids the overhead of creating duplicates.

Flexibility: It allows for easier sharing and modification of objects across different parts of the program, since any changes 
made to a mutable object will be reflected wherever the reference is used.

################################
2. Passing by Value in Python:
################################
In Python, there’s no direct mechanism to "pass by value" for mutable objects, but there are ways to simulate pass by value 
if needed:

For mutable objects (e.g., lists, dictionaries): To simulate passing by value, you can create a copy of the object, 
so modifications to the new object don’t affect the original.

Techniques for creating a copy:
Using the copy method (for shallow copies):

import copy

original_list = [1, 2, 3]
copy_list = original_list.copy()  # Shallow copy
copy_list.append(4)
print(original_list)  # Output: [1, 2, 3]
print(copy_list)      # Output: [1, 2, 3, 4]
Using the copy.deepcopy() function (for deep copies, which is needed if your object contains other nested mutable objects):


import copy

original_list = [[1, 2], [3, 4]]
deep_copy_list = copy.deepcopy(original_list)
deep_copy_list[0].append(5)
print(original_list)    # Output: [[1, 2], [3, 4]] (original remains unchanged)
print(deep_copy_list)   # Output: [[1, 2, 5], [3, 4]]
Shallow vs. Deep Copy:
Shallow copy: Creates a new object, but references to any mutable objects within the original object are still shared.
Deep copy: Creates a new object and recursively copies all objects inside it, ensuring no shared references remain.

Conclusion:
Python assigns variables by reference because it improves performance and memory efficiency. However, when working with mutable 
objects, you can simulate passing by value by creating a copy (either shallow or deep). For immutable objects, this isn't an issue,
 as any operation that would change the object creates a new one anyway.
"""