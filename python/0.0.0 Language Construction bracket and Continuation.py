""""""
"""
Construction of Python Program.
---------------------------------------
Compilation and Execution.
-----------------------------
0. Python interpreter how it works. 
    Compilation to Bytecode: When you run a Python program, the interpreter first compiles the entire source code into 
    bytecode. This bytecode is a lower-level, platform-independent representation of your code1.
    Execution of Bytecode: The compiled bytecode is then executed by the Python Virtual Machine (PVM). This execution 
    happens line by line, meaning the PVM interprets and runs each line of bytecode sequentially1.
    
    So, while the initial compilation step processes the whole program, the actual execution is done line by line. 
    This hybrid approach allows Python to catch errors early during the compilation phase and still provide the 
    flexibility of line-by-line execution during runtime
    
    \ and () help you write more readable code by allowing line continuation, they don’t directly affect the 
    line-by-line execution of the bytecode by the PVM.

A python program generally contains 3 constructs. 
-------------------------------------------------
1. Keywords: Reserved words that have special meaning in Python, such as if, else, for, while, def, class, etc.
2. Expressions: Combinations of values, variables, operators, lambda function definition and function calls 
   that are evaluated to produce a value.
3. Statements: Instructions that the Python interpreter can execute. Examples include assignment statements, control flow  
   statements (like if, for, while), and function calls.
   
   Expression are single line piece of code however,  they can be made multiple lines by \ using explict continuation or
   with implicit continuation.  for example
   
   add = (lambda x, y: 
                    x + y)  #implicit continuation
    
    add = lambda x, y: \
                    x + y   #explicit continuation 
                    
    add = lambda (x, y): x + y  is not allowed as syntax enforce it.  a lambda function is an expression which 
    should on one line.  here (x,y) can be spread to multiple lines if syntax allows it.
    
    if (x >0 
            and y>0): 
        print("no negative value")  #allow as expression is inside bracket.
        
     if (x >0): 
        print("no negative value") 
        #allow however since x>0 is single line expression so bracketless sytax is good.  if an express is on single
        line continuation is not needed.   
        Note:  in IF statement the relation expression x>0 was put in brakets due to continuation. this applies to 
               python and other language.  in if statement  (x>0) is not an argument. 
         
    try:
        # some code that may raise an exception
        pass
    except (TypeError, ValueError) as e:
        print("Error:", e)           #allowed. 
        
    try:
    # some code that may raise an exception
        pass
    except (TypeError) as e:
        print("Error:", e)      #allow.   however since TypeError is a single expression express bracketless syntax prefer. 

0.   Python has statement, blocks, context and context manager.
     there can be multiple statements in one block.
     there can be multiple blocks in one context. 

1.  : define the start of programming block. 
    in python : define the start of programming block.
    indentation level define the scope of the block
    end of indentation define end of this block.

    for example:
    if condition:
        # This is the start of the block
        print("Condition is true")
        # This is still part of the block
    print("This is outside the block")  # Indentation level decreased, so this is outside the block. 
    
2.  in python empty block is represented by pass after colon.  the empty block starts with a : and then pass keyword
    if emptyp:
       pass.

3. Statement Separator
    Semicolon (;): In Python, you can use a semicolon to separate multiple statements on a single line. For example
    x = 10; y = 20; print(x + y)

continuation. 
-------------
A python statement will on single line.  The only two ways to put statement on multiple lines is using \
and parentheses.  this is to note that.

lambda function are expression and single line statement. so lambda (x,y): x+y is not allowed as it makes 
it multiline.  so to make it multiline we have to use \ or (). 


4. Continuation Lines
    Backslash (\): If you have a long statement that you want to split across multiple lines, you can use a backslash at
    the end of a line to indicate that the statement continues on the next line. For example:
    total = 1 + 2 + 3 + \
        4 + 5 + 6

5. Implicit Continuation: If you’re inside parentheses (), square brackets [], or curly braces {}, you don’t need a
    backslash for continuation. For example:
    total = (1 + 2 + 3 +
            4 + 5 + 6)
    The objective of using parentheses (), square brackets [], or curly braces {} for implicit continuation is to make
     the code more readable and avoid the need for a backslash \ for line continuation.  in python lambda function is 
     single line expression so  lambda (x, y): x+y  is not allow.  as presence of () make it multiline statement which
     against the python lambda rule

5. The as keyword in Python is used to create an alias or to bind a name to an object within a specific context,
   such as with modules, exceptions, and context managers. This is different from the = operator, which is used for
   general assignment.

   import numpy as np  # 'np' is an alias for 'numpy'  here the context of np is whole module.
   this cannot be done with

   import numpy
   np = numpy  # This is not the same as using 'as' in the import statement
   

################################################
Brackets and their Uses in Python: (), [] and {}
################################################
Parentheses ():
-------------------
usage summary
1. tuple creation.
2. function calling.
3. creating generator throught comprehesion.  ( x for x in list)
4. continuation

Tuples: 
These are immutable, ordered collections. Example: (), (1, 2, 3). You can also create a tuple without
parentheses like this: t = 1, 2 results in (1, 2).

Order of Operations:Used to clarify the precedence of mathematical operations. Example: (n-1)**2.
Generator Expressions: A concise way to create iterators. Example: (i**2 for i in range(5)).
Function Calls: Used to call functions or methods. Example: print(), int(), range(5). You can also use
generator expressions within function calls: sum(i**2 for i in range(5)).
continuation:  if expression are multiline or contain more the one varaible or keyword. 
                return (x if x>0 else -1)
                assert (x>0 and y>0) "variable presents"       syntax :assert condition, message
                yield (1,2,3)                                  with single value yield 10

() complete usage in python
Passing arguments to functions
Implicit line continuation
Defining tuples
Grouping expressions
Calling functions and methods
Generator expressions
Defining lambda functions   # a =(lambda x, y : x+y)           #this is continuation usage of ()
Using in comprehensions with multiple conditions
Defining function signatures
Enclosing default parameter values in function definitions
Using in assert statements
Enclosing expressions in return statements
Enclosing expressions in yield statements
Enclosing expressions in raise statements                     #  raise ErrorValue("error message")
Using in with statements for context managers
Enclosing expressions in await statements
Enclosing expressions in async function definitions


Square Brackets []:
#######################

Summary
--------
used for 3 purpose. 
1.  create list
2.  indexing of all data types
3.  type Hint of all data types

Lists: 
These are mutable, ordered collections. Example: [], [1, 2, 3], [i**2 for i in range(5)]. list indexes are immutable 
while there values mutable

Indexing: 
Accessing a specific element in a sequence. Example: 'abc'[0] → 'a'. indexes are immutable.
used in tuples, list , dictionary for accessing values 

Lookup: ( same as indexing)
Retrieving values from a dictionary by key. Example: {0: 10}[0] → 10.   0 is key here
used in tuple, list, dictionary for accessing values. 

Slicing: (same as indexing)
Getting a part of a sequence. Example: 'abc'[:2] → 'ab'.   only used in list

Type Hints. 
used in list, tuple, dictionaries type hinting.
from typing import List
v_list: List[str] = ["one", "two", "three"]

List comprehension.
x = [x for x in list]


[] complete usage list in python
-----------------------------------
Creating lists                                          # a=[1,2,3]
Indexing elements in lists, tuples, and strings.        # list[0]   
Slicing lists, tuples, and strings                      #  list[2:]
List comprehensions                                     #  x = [x for x in list]
Accessing dictionary values                             #  dict['name']
Defining empty lists                                     # lis=[]
Selecting rows and columns in pandas DataFrames          # panda['row']['column']
Nested lists                                             #
Modifying elements in lists
Appending elements to lists
Removing elements from lists
Checking membership in lists                             
Iterating over lists
Using with enumerate for indexing
Using with zip for pairing elements

Keyobject (dictionary)
##########################
Python dictionary is a collection of key: value pairs.  therefore a python directory can be created by ways

my_dict = {'name': 'Amir', 'age': 30, 'city': 'Abu Dhabi'}    # normal creation.
my_dict = dict(name='Amir', age=30, city='Abu Dhabi')         # creation through dictionary constructor function. 
                                                              # passed values by name method 
                                                              
pairs = [('name', 'Amir'), ('age', 30), ('city', 'Abu Dhabi')]
my_dict = dict(pairs)

pairs = [('name', 'Amir'), ('age', 30), ('city', 'Abu Dhabi')]
my_dict = dict(pairs)

1.  Dictionaries: Curly braces are primarily used to define dictionaries, which are collections of key-value pairs.
    my_dict = {"name": "Alice", "age": 30}
2.  Sets: They are also used to define sets, which are unordered collections of unique elements.
    my_set = {1, 2, 3, 4}
3.  Dictionary Comprehensions: Curly braces can be used in dictionary comprehensions to create dictionaries in a concise way.
    squares = {x: x*x for x in range(6)}
4.  String Formatting: Curly braces are used in string formatting, especially with the str.format() method and f-strings.
    # Using str.format()
    message = "Hello, {}!".format("world")

    # Using f-strings
    name = "Alice"
    greeting = f"Hello, {name}!"
5. Escaping Braces in Strings: When you need to include literal curly braces in a formatted string, you can escape them by
   doubling the braces.
   # Using str.format()
    message = "This is a curly brace: {{}}".format()

    # Using f-strings
    message = f"This is a curly brace: {{}}"

Details on String formating

String Formatting: 
Curly braces are used to replace values inside strings in f-strings or .format() method. 
Example: f'{foobar}', '{0}'.format(foobar).
Curly braces, square brackets, and parentheses are also used in regular expressions:

[]: Defines character classes.
(): Groups expressions.
{}: Specifies repetition.

   
6.  # difference between (,) , [,], [] and ()
#################################################
    In Python, a tuple with a single element can be created by placing the element inside round brackets,
    which must be followed by a comma. The comma is not necessary for lists, but it is required for tuples to
    distinguish them from a single value in parentheses.

    single_element_tuple = (1,)
    print(single_element_tuple)  # Output: (1,)
    print(type(single_element_tuple))  # Output: <class 'tuple'>

 Note:The trailing comma is optional in Python and does not affect the function call.
    def tupetype2(a, b, c, d):
        print(a, b, c, d)

# Function call with a trailing comma
tupetype2(1, 2, 3, 4,)  # Output: 1 2 3 4

In Python, a list with a single element can be created by placing the element inside square brackets,
optionally followed by a comma. The comma is not necessary for lists, but it is required for tuples to 
distinguish them from a single value in parentheses.

a = [1,]
print(a)  # Output: [1]
print(type(a))  # Output: <class 'list'>

The tuple ll = (1, 2, 4, 5,) is a valid tuple with four elements. The trailing comma is
optional and does not affect the tuple’s validity or its contents

# List with a trailing comma
my_list = [1, 2, 4, 5,]

print(my_list)  # Output: [1, 2, 4, 5]
print(len(my_list))  # Output: 4
"""

"""
Why () is used inherited class. 
##################################
the child class is passed the type of parent class.  so that when child class is created. its parent class is created
first and then the child class

Class Definition: When you define a class, Python compiles the class definition into a class object. 
This includes both the child class and any parent classes it inherits from.

Inheritance: The child class inherits attributes and methods from the parent class. This means the child 
class has access to the parent’s methods and properties.

Instantiation: When you create an instance of the child class, Python:
Calls the __init__ method of the child class.
If the child class uses super(), it calls the __init__ method of the parent class to initialize inherited attributes.

class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

# Creating an instance of Child
child_instance = Child("Alice", 10)

Behind the Scenes:
Compilation: Both Parent and Child classes are compiled into class objects.
Inheritance: Child inherits from Parent, so it has access to Parent’s attributes and methods.
Instantiation: When child_instance is created, the __init__ method of Child is called, which in turn calls the __init__ method
 of Parent using super().
So, when you create an object of the child class, Python indeed uses the compiled code of both the child and parent 
classes to set up the object correctly.

"""