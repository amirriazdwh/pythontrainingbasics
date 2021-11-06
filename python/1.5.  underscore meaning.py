"""
Remember:  in python there are not public, protected and private clauses.  these are being implemented as hints through
           _.   var is a public variable,  _var is protected variable and __var is private variable.
           __ double underscore is called dunder.

Single Leading Underscore _var: Naming convention indicating name is meant for internal use.
this means variable/method is protected. A hint for programmers and not enforced by programmers.

Double Leading Underscore __var: Triggers name mangling when used in class context. Enforced by the Python interpreter
this means variable/method is private.  in class if class name is Test then due to automatic name mangling the method
will be available as _Test__var. this is to enforce private nature of variable/method.
.
Single Trailing Underscore var_: Used by convention to avoid naming conflicts with Python keywords.

Double Trailing Underscore __var__: Indicates special methods defined by Python language.  they are used in python
for object initialization and operators in class and in operator overloading.  most dunder methods are called by python
for example in case + then mathod __add__ is called.  in case of iteration __iter__ and __next__ is being called.  in case
of class __init__ is used for object initialization.  in same way some method like next and iter call __next__ and __iter__
method explicitly

Underscore _: Used as a name for temporary variables.
Python Features

_ is a somewhat special variable name. In the shell, it contains the value of the previously evaluated expression:

#>>> 1+2
3
#>>> _+4
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

# here the method argument name is class which will conflict with python keywords so its been changed to class_
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


#here the __call__ function make the object callable just like a function.  it works by creating an object and them
# implicitly calling the object method __call__.   so s1=print("Hello").__call__ will take place once developer used
# below code
class Printer:

    def __init__(self, s):
        self.str01 = s

    def __call__(self):
         return self.str01.upper()


s1 = Printer('hello') # Defining object of class Printer
# Calling object s1
s2=s1()   # Hello
print(s2)



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
