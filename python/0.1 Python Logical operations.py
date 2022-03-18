"""
In Python, apart from obvious True and False values, all other objects also have false or true value:

True value:
any non-zero number
any non-empty string
any non-empty object

False value:
0
None
empty string
empty object


0.    NoneType is a singleton object in python with a refrence id in memory.  when any object has null value this
reference id is assigned to that object.
so   noneVar is None  means

----------------------------------------------------------------------------

in python classes are first loaded into memory as singleton class.   its means these classes are static classes
a programmer create an object from these classes.

since there is only one class of static and memory address of that class is fixed.  we can get the memory address of
the class by id() function.
to get class or type of object python uses   type( listobject )  which returns the static class of that object.

so  express "type(listobject)  is list "    is return true.   as its equal to  id(type(listobject)) ==id (list)

"""


def testNone ( noneVar ) :
    # noneVar is not null
    if noneVar :
        print ( "variable is present" )


testNone ( "hello" )

"""
while test for none,   id(var) ==id(NoneType)   is check.   NoneType is a singleton object in python 
"""


def testNoneis ( noneVar ) :
    if noneVar is None :
        print ( "var is null ".format ( noneVar ) )


a = None
testNoneis ( a )
