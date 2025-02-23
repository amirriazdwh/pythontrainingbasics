"""
only _ means variable which is aynonmous.  means variable is not named and should not be used in program.   if you assigned any value to
          _,   you can access it by _ reference.  however,  if we use _ inplace of variable means we are planning to ignore that variable

Remember:
in python there are not public, protected and private clauses.  these are being implemented as hints through  _.

one time _ means variable or method cannot be imported into a module.   therefore its protected.  if in class it means
two times __

var is a public variable,
_var is protected variable
__var is private variable.
 __ double__ underscore is called dunder.

1, Single Leading Underscore _var:
 Naming convention indicating name is meant for internal use.
this means variable/method is protected. A hint for programmers and not enforced by programmers. _method name can be
called without any problem

leading _methods are not import from module if the import statement is from foo import *.  however,  importing as
import foo will import the method.

from underscore_module import *   #file created for example a file is a module and a module is an object

_internal_fnc()  will not be imported as its considered a protect function which cannot be accessed outside the module

2, Double Leading Underscore __var: Triggers name mangling when used in class context. Enforced by the Python interpreter
this means variable/method is private.  in class if class name is Test then due to automatic name mangling the method
will be available as _Test__var. this is to enforce private nature of variable/method.  in same way, method names are
also mangled with class name.
.
3. Single Trailing Underscore var_: Used by convention to avoid naming conflicts with Python keywords.

4. Double Trailing Underscore __var__: Indicates special methods defined by Python language.  they are used in python
for object initialization and operators in class and in operator overloading.  most dunder methods are called by python
for example in case + then mathod __add__ is called.  in case of iteration __iter__ and __next__ is being called.  in case
of class __init__ is used for object initialization.  in same way some method like next and iter call __next__ and __iter__
method explicitly

5. Underscore _: Used as a name for temporary variables.
Python Features

6. _ is a somewhat special variable name. In the shell, it contains the value of the previously evaluated expression:

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

class Test:
    def __init__(self, foo, bar, baz):
        self.foo =foo
        self._bar=bar
        self.__baz=baz


class ExtendedTest(Test):
    def __init__(self):
        super.__init__(self, 11,23, 42)
        self.foo="overridden"
        self._bar="overridden"
        self.__baz="overridden"

t2=ExtendedTest()

print("public variable",t2.foo)
print("protected variable",t2._bar)

# retrun error as no __baz variable exists
#print("public variable",t2.__baz)

"""
you can see that __bar got truned int _Ex-tendedTest__baz to prevent accidently modify private value of __baz in Test class
therefore Test has a method _Test__baz

__ name mangling does effect the methods names 
"""

class MangledMethod ():
    def __method(self):
        return 42

    def call_it(self):
        return self.__method()

# this will give error
#    MangledMethod.__method()

# here is another good example of name mangling.

_MangledGlobal__mangled=23

class MangledGlobal:
    def test(self):
        return __mangled

    MangledGlobal().test()
    # return 23

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
7.   as lambda function 
def __init__ (self, *args, **kwargs):  list constructor.   takes lambda function and generator  
lambda function contains anomous variables 
"""

my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda _: (_%2 == 0) , my_list))
print(new_list)

"""
-------------------
7.   default value 
--------------------

Linked to, but not explicitly mentioned here, is exactly when __all__ is used. It is a list of strings defining what symbols 
in a module will be exported when from <module> import * is used on the module.

For example, the following code in a foo.py explicitly exports the symbols bar and baz:

__all__ = ['bar', 'baz']

waz = 5
bar = 10
def baz(): return 'baz'
These symbols can then be imported like so:

from foo import *

print(bar)
print(baz)

# The following will trigger an exception, as "waz" is not exported by the module
print(waz)

NOTE: __all__ affects the from <module> import * behavior only. Members that are not mentioned in __all__ are still 
accessible from outside the module and can be imported with from <module> import <member>.



"""
