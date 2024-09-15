"""
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