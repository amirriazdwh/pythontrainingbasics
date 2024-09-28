"""
################################################
Brackets and their Uses in Python:
################################################

Square Brackets []:
--------------------
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
-------------------
Tuples: 
These are immutable, ordered collections. Example: (), (1, 2, 3). You can also create a tuple without
parentheses like this: t = 1, 2 results in (1, 2).

Order of Operations:
Used to clarify the precedence of mathematical operations. Example: (n-1)**2.

Generator Expressions: A concise way to create iterators. Example: (i**2 for i in range(5)).

Function Calls: Used to call functions or methods. Example: print(), int(), range(5). You can also use
generator expressions within function calls: sum(i**2 for i in range(5)).

Keyobject:
--------------
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



