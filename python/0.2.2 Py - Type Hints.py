"""
check the feature for python 3.10

duck typing helps IDE.   for example  if a function is being defined as

def foo (item1):
    item1.append(10)
    return tuple(item1)

in IDE we cannot find the functions of List as item1 is expected to be a list variable
pycharm will only give pycharm  templates to write the code   no list function will be
avaiable in intellsense.
"""

from typing import List , Tuple , Optional , Sequence , ClassVar

Vector = List [ float ]


def scale ( scalar: float , vector: Vector ) -> Vector :
    return [ scalar * num for num in vector ]


# typechecks; a list of floats qualifies as a Vector.
new_vector = scale ( 2.0 , [ 1.0 , -4.2 , 5.4 ] )


# ------------------------------------------------
#   List  and Tuple example
# ------------------------------------------------
def List2Tuple ( item1: List [ int ] ) -> Tuple [ int ] :
    item1.append ( 10 )
    return tuple ( item1 )


ListOfint: List [ int ] = [ 1 , 2 , 3 , 4 , 5 , 67 ]
print ( List2Tuple ( ListOfint ) )


# ---------------------------------------------------------------
#   in some function its being expected that they will
#   return some value or return None.   in Other functions
#   case we dont expect None values,   we always expect them
#    to return a functions.
#   returnNone ( item1: List[float]) -> int will return a type
#   if we are returning None anywhere in procedure.
#   to correct  use Optional
# ----------------------------------------------------------------

def returnIntOrNone ( item1: List [ float ] ) -> Optional [ int ] :
    if item1 :
        return 10
    else :
        return None


"""
as sequence is super type of List, tuple or String we can pass this 
"""


def seqtofloat ( seq: Sequence [ int ] ) -> List [ float ] :
    return list ( float ( x ) for x in seq )


print ( seqtofloat ( ListOfint ) )

tstr: Tuple [ int , ... ] = (1 , 2 , 3 , 4 , 5)
print ( seqtofloat ( tstr ) )

# why can i give string of integers.
strint: str = "1234567"
print ( seqtofloat ( strint ) )


class MyClass :
    # You can optionally declare instance variables in the class body
    attr: int
    # This is an instance variable with a default value
    charge_percent: int = 100

    # The "__init__" method doesn't return anything, so it gets return
    # type "None" just like any other method that doesn't return anything
    def __init__ ( self ) -> None :
        pass

    # For instance methods, omit type for "self"
    def my_method ( self , num: int , str1: str ) -> str :
        return num * str1


# User-defined classes are valid as types in annotations
x: MyClass = MyClass ( )


# You can use the ClassVar annotation to declare a class variable
class Car :
    seats: ClassVar [ int ] = 4
    passengers: ClassVar [ List [ str ] ]


# You can also declare the type of an attribute in "__init__"
class Box :
    def __init__ ( self ) -> None :
        self.items: List [ str ] = [ ]


#############################
from typing import List, Set, Dict, Tuple, Optional

# For simple built-in types, just use the name of the type
x: int = 1
x: float = 1.0
x: bool = True
x: str = "test"
x: bytes = b"test"

# For collections, the type of the collection item is in brackets
# (Python 3.9+)
x: list[int] = [1]
x: set[int] = {6, 7}

# In Python 3.8 and earlier, the name of the collection type is
# capitalized, and the type is imported from the 'typing' module
x: List[int] = [1]
x: Set[int] = {6, 7}

# Same as above, but with type comment syntax (Python 3.5 and earlier)
x = [1]  # type: List[int]

# For mappings, we need the types of both keys and values
x: dict[str, float] = {"field": 2.0}  # Python 3.9+
x: Dict[str, float] = {"field": 2.0}

# For tuples of fixed size, we specify the types of all the elements
x: tuple[int, str, float] = (3, "yes", 7.5)  # Python 3.9+
x: Tuple[int, str, float] = (3, "yes", 7.5)

# For tuples of variable size, we use one type and ellipsis
x: tuple[int, ...] = (1, 2, 3)  # Python 3.9+
x: Tuple[int, ...] = (1, 2, 3)

# Use Optional[] for values that could be None
x: Optional[str] = some_function()
# Mypy understands a value can't be None in an if-statement
if x is not None:
    print(x.upper())
# If a value can never be None due to some invariants, use an assert
assert x is not None
print(x.upper())
