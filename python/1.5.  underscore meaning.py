"""
Single Leading Underscore _var: Naming convention indicating name is meant for internal use. A hint for programmers and not enforced by programmers.
Double Leading Underscore __var: Triggers name mangling when used in class context. Enforced by the Python interpreter.
Single Trailing Underscore var_: Used by convention to avoid naming conflicts with Python keywords.
Double Trailing Underscore __var__: Indicates special methods defined by Python language.
Underscore _: Used as a name for temporary variables.
Python Features

_ is a somewhat special variable name. In the shell, it contains the value of the previously evaluated expression:

>>> 1+2
3
>>> _+4
7

"""
x = (11, 12, 1, 3)

_, _, _, c = x
(*b, _) = x

print(b, c)

# a loop require iterator or generator after in clause
for _ in range(len(x)):
    print("looping")

"""
1. Single Leading Underscore: _var
A name prefixed with an underscore (e.g. _spam) should be treated as a non-public part of the API (whether it is a 
function, a method or a data member). It should be considered an implementation detail and subject to change without notice.
"""


class Person:
    def __init__(self):
        self.name = 'Sarah'
        self._age = 26
        self.__id = 30


p = Person()
print("name public variable : ", p.name)
print("Age private variable ", p._age)

"""
2. Double Leading Underscore: __var
This is also called name mangling — the interpreter changes the name of the variable in a way that makes it harder to create collisions
 when the class is extended later.  p.__id will be mangled with object name and p.__id will give error 
>>> p.__id
AttributeError: 'Person' object has no attribute '__id'
dir(Person) will give all methods
"""
print(p._Person__id)

"""
3. Single Trailing Underscore: var_
Single trailing underscore naming convention is used to avoid conflicts with Python keywords.
"""


def method(name, class_='Classname'):
    pass


"""
4. Double Leading and Trailing Underscore: __var__
Names that have leading and trailing double underscores (“dunders”) are reserved for special use like the__init__ method 
for object constructors, or __call__ method to make object callable. These methods are known as dunder methods.

"""

class Person01:
    def __init__(self):
        self.__name__ = 'Sarah'    # its a method private in class __init__ is the constructor

Person01().__name__


"""
6.   as lambda function 
def __init__ (self, *args, **kwargs):  list constructor.   takes lambda function and generator  
lambda function contains anomous variables 
"""

my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda _: (_%2 == 0) , my_list))
print(new_list)

"""
7.   default value 
"""
default_variable =_
print (default_variable)
