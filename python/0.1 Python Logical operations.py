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

"""


def testNone(noneVar):
    # noneVar is not null
    if noneVar:
        print("variable is present")


testNone("hello")

"""
while test for none,   id(var) ==id(NoneType)   is check.   NoneType is a singleton object in python 
"""
def testNoneis(noneVar):
    if noneVar is None:
        print("var is null " .format(noneVar) )


a = None
testNoneis(a)
