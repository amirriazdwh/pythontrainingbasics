"""
create by :  Amir Riaz
Key Points to Understand Python's Structure:

############################
Python's Architecture:
############################

A namespace in Python is essentially a container that holds a mapping between names (like variable names, 
function names, etc.) and objects. Each name points to an object stored in memory, so when you use a name in 
your code, Python uses the namespace to look up the associated object in memory.

why a namespace is required.  a namespace is required because everything in python is object.  basic objects are 
function, class, module, variable etc.   when you create a function like 

def check_balance:
   pass
   
python create a function object and store it with name check_balance in namespace.  when its been called from 
any function refrence.  python looks into the namespace(also call dictionary). takes function objects and runs.
like function.run()

How Namespaces Work in Memory:
At Runtime: When you run a Python program, these namespaces are created dynamically at runtime. Names 
(like variable names) in a namespace are simply keys that reference objects in memory (like values in a dictionary).

Memory Storage: Each object in Python lives somewhere in memory. The namespace is like a table (dictionary) that
 maps names to these memory locations. When you use or define a name, Python checks the relevant namespace to find 
 the associated memory location of the object.

Python has three main types of namespace scopes:
--------------------------------------
Built-in Scope: 
This contains the built-in objects and functions available in every Python program, like print(), int(), etc.

Global Scope: 
This refers to variables defined at the top level of the code or module. They can be accessed from 
anywhere in the code unless shadowed by a local variable.

Local Scope: 
These are variables that are defined inside a function or a block and are only accessible within that
function/block. Everything in Python is an Object:

Whether it's a class, data type, function, module, or import, everything in Python is an object. 
Each object or scope (like variables, classes, or functions) has an associated dictionary 
(often referred to as a "namespace") where its data and attributes are stored.

################################################
Brackets and their Uses in Python:
################################################

Square Brackets []:

Lists: 
These are mutable, ordered collections. Example: [], [1, 2, 3], [i**2 for i in range(5)]. list indexes are immutable 
as they are variable to a function. 

Indexing: 
Accessing a specific element in a sequence. Example: 'abc'[0] → 'a'. indexes are immutable.

Lookup: 
Retrieving values from a dictionary by key. Example: {0: 10}[0] → 10.

Slicing: 
Getting a part of a sequence. Example: 'abc'[:2] → 'ab'.


Parentheses ():

Tuples: 
These are immutable, ordered collections. Example: (), (1, 2, 3). You can also create a tuple without parentheses like this: t = 1, 2 results in (1, 2).
Order of Operations: Used to clarify the precedence of mathematical operations. Example: (n-1)**2.
Generator Expressions: A concise way to create iterators. Example: (i**2 for i in range(5)).
Function Calls: Used to call functions or methods. Example: print(), int(), range(5). You can also use generator expressions within function calls: sum(i**2 for i in range(5)).

Keyobject:
in python an object define the key value pair.  its basic object for creating dictionary

Curly Braces {}:

Dictionaries: 
These are key-value pairs. Example: {}, {0: 10}, {i: i**2 for i in range(5)}.
Sets: These are unordered collections of unique elements. Example: {0}, {i**2 for i in range(5)}.

String Formatting: 
Curly braces are used to replace values inside strings in f-strings or .format() method. 
Example: f'{foobar}', '{0}'.format(foobar).
Curly braces, square brackets, and parentheses are also used in regular expressions:

[]: Defines character classes.
(): Groups expressions.
{}: Specifies repetition.

-
Special Methods in Python:
__call__(self[, args...]): This is a special method for making an instance of a class callable like a function.
__getitem__(self, key): This special method is used to make objects indexable, just like lists or dictionaries.
Finally, typing help('modules') in the Python interpreter will list all the available modules in your environment.
"""



