"""

###############
IMPORTANT
###############
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


In Python, None is considered a falsy value, meaning it evaluates to False in a boolean context.

Other Falsy Values:
None
0 (zero)
False
Empty sequences like [], '', ()
Empty dictionaries {} or sets set()

b=[]
if b:
    print("List is truthy")
else:
    print("List is falsy")  # This will be printed because the list is empty


acts like bool() is added implicitly.
if bool(b):
    print("List is truthy")
else:
    print("List is falsy")  # This will be printed because the list is empty

Summary:
In Python, you can check variable equality in two ways:

Memory address comparison using the "is" operator (e.g., x is y), which checks if two variables point to 
the same object in memory. The opposite is is not.
Data value comparison using the == operator (e.g., x == y), which checks if the values are equal. 
The opposite is !=.

In Python, objects are evaluated as True or False based on their contents:

True: Any non-zero number, non-empty string, or non-empty object.
False: Zero (0), None, empty strings, or empty objects.
Special Concepts:
None: Python uses a special singleton object for None (a null-like value). When a variable is set to None,
it gets this unique reference in memory.  since None is singleton object therefore all the variable which
are none point to same memory address.

Example:
python
Copy code
noneVar is None  # Checks if noneVar is None
Classes in Python: Classes are loaded into memory as singleton classes (static). The memory address of a class 
can be obtained using the id() function, and you can check the type of an object using type(). 

For example:

python
Copy code
type(listobject) is list  # Returns True

Example Functions:
testNone(): Checks if a variable is None and prints a message if it is.
testNoneis(): Tests for a None object and prints its length if it's not None.
None and Option:
A companion object of Option can handle None values by providing an apply method that converts a null to None or wraps it as Some(x) if it's not null.

"""