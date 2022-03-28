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
import time
from typing import List , Tuple , Optional , Sequence , ClassVar , Iterator , cast , Any

"""
Every class is also a valid type. Any instance of a subclass is also compatible with all superclasses – it follows 
that every value is compatible with the
object type (and incidentally also the Any type, discussed below). Mypy analyzes the bodies of classes to determine 
which methods and attributes 
are available in instances. This example uses subclassing:
"""


class A :
    def f ( self ) -> int :  # Type of self inferred (A)
        return 2


class B ( A ) :
    def f ( self ) -> int :
        return 3

    def g ( self ) -> int :
        return 4


#  method defined with class A
def foo ( a: A ) -> None :
    print ( a.f ( ) )  # 3


foo ( B ( ) )  # OK (B is a subclass of A)

"""
A value with the Any type is dynamically typed. Mypy doesn’t know anything about the possible runtime types of such 
value. Any operations are
 permitted on the value, and the operations are only checked at runtime. You can use Any as an “escape hatch” when 
 you can’t use a more 
 precise type for some reason.
Any is compatible with every other type, and vice versa. You can freely assign a value of type Any to a variable with 
a more precise type:
"""
a: Any = None
s: str = ''
a = 2  # OK (assign "int" to "Any")
s = a  # OK (assign "Any" to "str")

"""
You should give a statically typed function an explicit None return type even if it doesn’t return a value, 
as this lets mypy catch additional type errors:
"""


def wait ( t: float ) :  # Implicit Any return value
    print ( 'Waiting...' )
    time.sleep ( t )


# print( wait(2) > 1)   Mypy will not catch this error and program with give runtime error

def wait ( t: float ) -> None :  # Implicit Any return value
    print ( 'Waiting...' )
    time.sleep ( t )


# print ( wait ( 2 ) > 1 )  # Expected int got None. error

"""
Tuple types
The type tuple[T1, ..., Tn] represents a tuple with the item types T1, …, Tn:
"""


# Use `typing.Tuple` in Python 3.8 and earlier
def f ( t: Tuple [ int , str ] ) -> None :
    t = 1 , 'foo'  # OK


#   t = 'foo' , 1   Type check error

"""
A tuple type of this kind has exactly a specific number of items (2 in the above example). Tuples can also be used as 
immutable, 
varying-length sequences. You can use the type tuple[T, ...] (with a literal ... – it’s part of the syntax) for this 
purpose. Example:
"""


def print_squared ( t: Tuple [ int , ... ] ) -> None :
    for n in t :
        print ( n , n ** 2 )


print_squared ( () )  # OK
print_squared ( (1 , 3 , 5) )  # OK
print_squared ( [ 1 , 2 ] )  # Error: only a tuple is valid

"""
as sequence is super type of List, tuple or String we can use it.  if we have to pass a sequence subtypes
"""
ListOfint: List [ int ] = [ 1 , 2 , 3 , 4 , 5 , 67 ]


def seqtofloat ( seq: Sequence [ int ] ) -> List [ float ] :
    return list ( float ( x ) for x in seq )


print ( seqtofloat ( ListOfint ) )

tstr: Tuple [ int , ... ] = (1 , 2 , 3 , 4 , 5)
print ( seqtofloat ( tstr ) )

# why can i give string of integers.
strint: str = "1234567"
print ( seqtofloat ( strint ) )

"""
You can pass around function objects and bound methods in statically typed code. The type of a function that accepts 
arguments A1, …, An
 and returns Rt is Callable[[A1, ..., An], Rt]. Example
"""

from typing import Callable


def twice ( i: int , next: Callable [ [ int ] , int ] ) -> int :
    return next ( next ( i ) )


def add ( i: int ) -> int :
    return i + 1


print ( twice ( 3 , add ) )  # 5

"""
You can only have positional arguments, and only ones without default values, in callable types. These cover the vast 
majority of uses of callable types, 
but sometimes this isn’t quite enough. Mypy recognizes a special form Callable[..., T] (with a literal ...) which can 
be used in less typical cases. It is compatible 
with arbitrary callable objects that return a type compatible with T, independent of the number, types or kinds of 
arguments. Mypy lets you call such callable
 values with arbitrary arguments, without any checking – in this respect they are treated similar to a (*args: Any, 
 **kwargs: Any) function signature. Example:
"""


def arbitrary_call ( f: Callable [ ... , int ] ) -> int :
    return f ( 'x' ) + f ( y = 2 )  # OK


# arbitrary_call(ord)   # No static error, but fails at runtime
# arbitrary_call(open)  # Error: does not return an int
# arbitrary_call(1)     # Error: 'int' is not callable

"""Union types Python functions often accept values of two or more different types. You can use overloading to 
represent this, but union types are often more convenient. Use the Union[T1, ..., Tn] type constructor to construct a 
union type. For example, if an argument has type Union[int, str], both integers and strings are valid argument 
values. You can use an isinstance() check to narrow down a union type to a more specific type: """

from typing import Union


def f ( x: Union [ int , str ] ) -> Union [ int , str ] :
    if isinstance ( x , int ) :
        # Here type of x is int.
        return x + 1  # OK
    else :
        # Here type of x is str.
        return x + 'a'  # OK


print ( f ( 1 ) )  # OK
print ( f ( 'x' ) )  # OK
# print(f ( 1.1 ) ) # Error  unsupported operation for float and Str

"""Optional types and the None type¶ You can use the Optional type modifier to define a type variant that allows 
None, such as Optional[int] (Optional[X] is the preferred shorthand for Union[X, None]): """


# ---------------------------------------------------------------
#   in some function its being expected that function will
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


from typing import Optional


def strlen ( s: str ) -> Optional [ int ] :
    if not s :
        return None  # OK
    return len ( s )


# def strlen_invalid(s: str) -> int:
#     if not s:
#         return None  # Error: None not compatible with int
#     return len(s)

"""
Most operations will not be allowed on unguarded None or Optional values:
"""


def my_inc ( x: Optional [ int ] ) -> int :
    return x + 1  # Error: Cannot add None and int a if condition is required here.


# my_inc ( None )
"""
Instead, an explicit None check is required. Mypy has powerful type inference that lets you use regular Python idioms to
 guard against None values. For example, mypy recognizes is None checks:
"""


def my_inc ( x: Optional [ int ] ) -> int :
    if x is None :
        return 0
    else :
        # The inferred type of x is just int here.
        return x + 1


def concat ( x: Optional [ str ] , y: Optional [ str ] ) -> Optional [ str ] :
    if x is not None and y is not None :
        # Both x and y are not None here
        return x + y
    else :
        return None


print ( concat ( 'a' , 'b' ) )
print ( concat ( None , 'b' ) )
# print ( concat ( 1, 'b' ) )


"""
Type aliases¶
In certain situations, type names may end up being long and painful to type:
"""
T = Optional [ str ]

def concat2 ( x: T , y: T ) -> T :
    if x is not None and y is not None :
        # Both x and y are not None here
        return x + y
    else :
        return None

print ( concat2 ( 'a' , 'b' ) )

Vector = List [ float ]


def scale ( scalar: float , vector: Vector ) -> Vector :
    return [ scalar * num for num in vector ]


# typechecks; a list of floats qualifies as a Vector.
new_vector = scale ( 2.0 , [ 1.0 , -4.2 , 5.4 ] )

"""
Named tuples
Mypy recognizes named tuples and can type check code that defines or uses them. In this example, we can detect code trying to access a missing attribute:
"""

# ------------------------------------------------
#   List  and Tuple example
# ------------------------------------------------
def List2Tuple ( item1: List [ int ] ) -> Tuple [ int ] :
    item1.append ( 10 )
    return tuple ( item1 )


ListOfint: List [ int ] = [ 1 , 2 , 3 , 4 , 5 , 67 ]
print ( List2Tuple ( ListOfint ) )


# --------------------------------------------------------
#  Custom classes as type.
# --------------------------------------------------------
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
newCar: MyClass = MyClass ( )


# You can use the ClassVar annotation to declare a class variable
class Car :
    seats: ClassVar [ int ] = 4
    passengers: ClassVar [ List [ str ] ]


vCar = Car ( )
seats = vCar.seats

print ( type ( seats ) )


# You can also declare the type of an attribute in "__init__"
class Box :
    def __init__ ( self ) -> None :
        self.items: List [ str ] = [ ]


#############################
from typing import List , Set , Dict , Tuple

# For simple built-in types, just use the name of the type
x1: int = 1
x2: float = 1.0
x3: bool = True
x: str = "test"
x5: bytes = b"test"

# For collections, the type of the collection item is in brackets
# (Python 3.9+)
x6: List [ int ] = [ 1 ]
x7: Set [ int ] = { 6 , 7 }

# In Python 3.8 and earlier, the name of the collection type is
# capitalized, and the type is imported from the 'typing' module
x8: List [ int ] = [ 1 ]
x9: Set [ int ] = { 6 , 7 }

# Same as above, but with type comment syntax (Python 3.5 and earlier)
x10 = [ 1 ]  # type: List[int]

# For mappings, we need the types of both keys and values
x11: Dict [ str , float ] = { "field" : 2.0 }  # Python 3.9+
x12: Dict [ str , float ] = { "field" : 2.0 }

# For tuples of fixed size, we specify the types of all the elements
x13: Tuple [ int , str , float ] = (3 , "yes" , 7.5)  # Python 3.9+
x14: Tuple [ int , str , float ] = (3 , "yes" , 7.5)

# For tuples of variable size, we use one type and ellipsis
x15: Tuple [ int , ... ] = (1 , 2 , 3)  # Python 3.9+
x16: Tuple [ int , ... ] = (1 , 2 , 3)

# Use Optional[] for values that could be None
# x17: Optional [ str ] = some_function ( )

# Mypy understands a value can't be None in an if-statement
if x is not None :
    print ( x.upper ( ) )
# If a value can never be None due to some invariants, use an assert
assert x is not None
print ( x.upper ( ) )


##################################################################
# Add default value for an argument after the type annotation
def f ( num1: int , my_float: float = 3.5 ) -> float :
    return num1 + my_float


# This is how you annotate a callable (function) value
#  function take two parameter in and float and returns float.
x: Callable [ [ int , float ] , float ] = f


# A generator function that yields ints is secretly just a function that
# returns an iterator of ints, so that's how we annotate it
def g ( n: int ) -> Iterator [ int ] :
    i = 0
    while i < n :
        yield i
        i += 1


# Use Union when something could be one of a few types
x20: List [ Union [ int , str ] ] = [ 3 , 5 , "test" , "fun" ]

a = [ 4 ]
b = cast ( List [ int ] , a )  # Passes fine
c = cast ( List [ str ] , a )  # Passes fine (no runtime check)
# reveal_type ( c )  # -> Revealed type is "builtins.list[builtins.str]"
print ( c )  # -> [4]; the object is not cast
