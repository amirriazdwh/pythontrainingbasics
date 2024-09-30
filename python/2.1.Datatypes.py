"""
in python all variables are objects of their respective classes. variable can be deleted by del function

Type Conversion is the conversion of object from one data type to another data type.
Implicit Type Conversion is automatically performed by the Python interpreter.
Python avoids the loss of data in Implicit Type Conversion.
Explicit Type Conversion is also called Type Casting, the data types of objects are converted using predefined
functions by the user.
In Type Casting, loss of data may occur as we enforce the object to a specific data type.
"""

"""
collections are abstract class of  sequences which contains  __getitem__, __len__ methods for iteration.  
sequences are further divided into ordered and unordered sequences
-------------------------------------------------------------------------
--1.  Numbers  types are Int, float, bool and complex
-------------------------------------------------------------------------
1. Integer (int)
Default Value: 0
Maximum Value: Python’s int type can handle arbitrarily large values, limited only by the available memory. 
There is no fixed maximum value.
<class 'int'>

2. Floating-point (float)
Default Value: 0.0
Maximum Value: The maximum value for a float is approximately 1.8 x 10^308. This is defined by the IEEE 754 double-precision
floating-point standard.
<class 'float'>

3. Complex (complex)
Default Value: 0j (which is equivalent to 0 + 0j)
Maximum Value: Complex numbers in Python do not have a maximum value for their real or imaginary parts,
similar to integers. They are limited by the available memory.
<class 'complex'>



int              defines integer. its an object of type <class 'Int'> an integer has derived types String so integer 
                 can be converted to string
float           defines  object of types <class 'float'>
bool           a boolean data types contains three values,  None, True and False and its of type <class 'bool'>
complex     number like 6+4j if of type <class 'complex'>
"""

"""
-------------------------------------------------------------------------
--2.  String types are string
-------------------------------------------------------------------------
character  define by a single character and convert from digit to character by chr  function and from chr to ASCI digital by ord.  each character has
an ordinal number associated with it.  to convert a ord to character use chr(num) and a character can be convert to ord by ord() func
a sequence of characters list or tuples can be converted to string by "".join(sequence). we can represent string by ' or ".  we dont
have chr  datatype in python,  we have string.  character is of type String of class <class String>

String  defined by ""  double qoutte or ''  single quote.  The char is defined by ''. single or ""  double quote.  Multi-line strings can be denoted using triple quotes, a
string is a sequence so they can be accessed by index.  a string is basic data types of integer so string can be converted to int
using int. function.  a string can be converted to list and tuples by list() and tuples()
"""

"""
--------------------------------------------------------------------------
--3.  There are seven sequence types: strings, Unicode strings, lists, tuples, bytearrays, buffers, and xrange objects.  sequences also called ordered collection
--------------------------------------------------------------------------
In Python programming, sequences are a generic term for an ordered set which means that the order in which we input the items
 will be the same when we access them. Python supports six different types of sequences. These are strings, lists, tuples, byte sequences
 , byte arrays, and range objects.

 () tuple is immutable.   so it can be used in place where variable should not change like  function parameters.   tuples..
 tuple are order sequence, immutable and since they are a sequence they contain an iterator
 List    defined by [],  used List() for conversion to list all sequence.  List are order sequence , mutable and contain iterators, so they have index

all sequence create iterator if the values are hardcoded.   however,  once these values pass through some rules a generator is  created.

Sequences also support slicing: a[i:j] selects all items with index k such that i <= k < j. When used as an expression,
a slice is a sequence of the same type. This implies that the index set is renumbered so that it starts at 0.

Some sequences also support “extended slicing” with a third “step” parameter: a[i:j:k] selects all items of a with index x
where x = i + n*k, n >= 0 and i <= x < j.

"""

"""
-------------------------------------------------------------
-   4.   Set and Dictionary  are unordered collection
-------------------------------------------------------------
A set object is an unordered collection of distinct hashable objects. Common uses include membership testing, removing duplicates from a sequence,
and computing mathematical operations such as intersection, union, difference, and symmetric difference. (For other containers see the built in dict, list,
and tuple classes, and the collections module.).   sets are immutable and have a iterator for iteration.
set     defined as {}.  since sets are unorders they dont have an index. we use set() function to convert all sequence to set

Dictionary   defined by {} with items as key:value  used dict() for covnersion.
These represent finite sets of objects indexed by nearly arbitrary values. The only types of values not acceptable as keys are values containing lists
or dictionaries or other mutable types that are compared by value rather than by object identity, the reason being that the efficient implementation of
 dictionaries requires a key’s hash value to remain constant. Numeric types used for keys obey the normal rules for numeric comparison: if two numbers
  compare equal (e.g., 1 and 1.0) then they can be used interchangeably to index the same dictionary entry.

note: that item inside {} are written as key:value or key=value but without {} its been represented as key=value
dic ={i:f"item{i}" for i in range(1,10)}.  with f you can using {}
Note:  a json file is a dictionary saved in a file
Note:  a dictionary is a ziping of two sequence stud by stud.  thats why zip function is using to
create a dictionary from two sequences. just like a zip can be unzipped.  we can use unzip funtion to
get key and values in two difference sequences.  keys are unique and immutable in dictionary

as dictionary are set of  key: value pairs,  they are being defined as   s={'a':1, 'b':2}  or s={(a,1), (b, 2)}
key values pairs without {} are represented as a=1 and b=2.    note a & b are string otherwise compiler looks for their values and data type
"""

"""
-------------------------
-  5     None    
-------------------------
         is an object defined to represent null values.   its type is <class 'NoneType'>.  when a variable is
         not assigned any value its None.  in if expresion is evaluated as  if varis is None:  print("None")
"""

"""
-------------------------
-  6.    range    
-------------------------
        is data type with iterator its called generator its type is <class 'range'>
"""

"""
------------------------------------------------------------------------------------------------------------------------------------
-  7.   sequence Casting
------------------------------------------------------------------------------------------------------------------------------------
in python string, list and tuples are order sequences so they can be type casted
in python set are unorder seqeuence. list, tuples, string, range are order sequence
since both order sequence and unorder sequence are derived for sequence therefore a set can be converts to list, tuple or stirng

in dictionary key must be unique.  while values can be repeated.  thats why its being represent by {} since in sets the
values are not repeated. in same way in diction the keys are not repeated.  dictionary was created since it was not possible to
access an individual element in a set without scanning the whole set.
to get the keys we use.  d.keys and for values d.values and to get both keys and values as tuple we use d.items

"""

"""

--------------------------------------------------------------------
-- 8.   list,  tuples, string iterators, set  are represented by *  while dictionary iterators are represented by **
--------------------------------------------------------------------
class dict(**kwarg)
class dict(mapping, **kwarg)
class dict(iterable, **kwarg)

*list   means   tuple(x for x in list)
**dic   menas   dict(k,x for k,x in dic)

chars = ['g', 'b', 'e', 'b', 'g']
result = list(map(lambda s: str(s).upper(), chars))
print(set(result))
-------------------------------
-- 9.   standard operation allowed on sequences.
----------------------------------------------
There are three standard arithmatic operation sequence operations   (  +   ,  *   , [  ]  )     while comparison operations are :  ==, >,< >= , <=
 that can be performed with tuples as well as lists and strings.
------------------------------------------------------------------------------------------------------------------------------
"""


########### complex data types ####
compNum = 6 + 4j  # instead of i j is being used in python
print(compNum)

############# boolean ########
vTrue = True
vTnum = int(vTrue)  # gives 1
vTrue = False
vTnum = int(vTrue)  # gives 0   false if null or empty

############# Integer ########
vChar = "23"  # define string
# convert Str to integer
vInt = int(vChar)
print(vInt)

# del will remove the memory allocation of vInt and therefore it will not be accessable in str(vInt).  all variables in python are objects therefore can be deleted by del
# del vInt
# print(vInt)

# convert Integer to String.  since string is basic datatypes and integer is derived from it. string can be convert to int
vChar = str(vInt)
print(vChar)

############ charater to Asci and asci to charater ########
print("convert Character to ord", ord('c'))
print("convert ord to character ", chr(99))
print(chr(97))
print(chr(65))
print(chr(1200))

# return 65
print(ord('A'))

#####################################################
# bytes([source[, encoding[, errors]]])
#####################################################
string = "Python is interesting."

# string with encoding 'utf-8'
arr = bytes(string, 'utf-8')
print(arr)

string.encode(encoding='UTF-8', errors='strict')
print(string)

':'.join(['toto', '12', 'pswd'])

"words with spaces".split()

#####################################################
size = 5
arr = bytes(size)
print(arr)

rList = [1, 2, 3, 4, 5]
arr = bytes(rList)
print(arr)

####################################################
# unicode string
string = 'pythön!'

# print string
print('The string is:', string)

# default encoding to utf-8
string_utf = string.encode()

# print result
print('The encoded version is:', string_utf)
print(b'pyth\xc3\xb6n!'.decode("utf-8"))
#####################################################

# unicode string
string = 'pythön!'

# print string
print('The string is:', string)

# ignore error
print('The encoded version (with ignore) is:', string.encode("ascii", "ignore"))

# replace error
print('The encoded version (with replace) is:', string.encode("ascii", "replace"))

######### tuple ####

# -1 reverses the tuple and gives output
# print("the number is  ", xx[1::-1])

print("------keys then value------")
tupleNum = tuple((x for x in (('x', 'y', 'z'), (1, 2, 3))))
print(tupleNum)

# first tuple added to tuple and then second tuple added

print("------create flat tuple------")

flatuple = tuple(x for ele in tupleNum for x in ele)
print(flatuple)

# a for loop need a sequence to run. left loop creates a sequence being used by the second loop

print("---- create diction -----")
tupleZipNum = tuple(zip(('x', 'y', 'z'), (1, 2, 3)))
print(tupleZipNum)

###########################
print("---- create enumeration -----")

a = ('x', 'y', 'z')
b = (1, 2, 3)

for i, x in enumerate((a, b)):
    print(i, x)
"""
print('_____________________________________')
dic = dict((i, x) for tupEle in (xx,yy) for (i, x) in enumerate(tupEle))
print(dic)
print('_____________________________________')

"""

# def solve(lis, n):
#    it = iter(lis)
#    return [list(islice(it, n)) for _ in range(len(lis)/n)]

# solve(range(1,9),4)

##############################################
# list to dict conversion
###############################################
numbers1 = dict([('x', 5), ('y', -5)])
print('numbers1 =', numbers1)

# keyword argument is also passed a tuple is part of dictionary which can be represented as z=9
numbers2 = dict([('x', 5), ('y', -5)], z=8)
print('numbers2 =', numbers2)

###############################################
# zip() the list creates an iterable in Python 3
################################################
number0 = zip(['x', 'y', 'z'], [1, 2, 3])
print(number0)
numbers3 = dict(zip(['x', 'y', 'z'], [1, 2, 3]))
print('numbers3 =', numbers3)


# in diction we have a safe method called get which return None when key does not match
#  List does not have any such method however,  we can implement get method in list also
class safelist(list):
    def get(self, index, default=None):
        try:
            return self.__getitem__(index)
        except IndexError:
            return default

def _test():
    l = safelist(range(10))
    print( l.get(20, "oops"))

if __name__ == "__main__":
    _test()

"""
Note: A sequence is order collection of element ordered by an index
In Python, a container is an abstract base class defined in the collections.abc module. It represents objects that 
can contain other objects and defines the __contains__ method, which checks for membership. Containers are 
fundamental to Python’s data structures, providing a way to group and manage collections of items.

Purpose of Containers
----------------------
Containers serve several key purposes:

Grouping Data: 
Containers allow you to group multiple items together, making it easier to manage and manipulate collections of data.

Membership Testing:
 Containers support membership testing using the in and not in operators, enabling you to check
if an item exists within the container.

Iteration: 
Containers can be iterated over, allowing you to process each item in the collection.

Flexibility: 
Containers can hold heterogeneous data types, meaning you can store different types of objects
within the same container.


object
├── int
├── float
├── complex
├── collections.abc.Container                    # Defines the __contains__ method.
│   ├── collections.abc.Iterable                 # Defines the __iter__ method.
│   │   ├── collections.abc.Iterator             # Inherits from Iterable and defines the __next__ method.      
│   │   │   └── collections.abc.Generator        # Inherits from Iterator and extends it with the generator protocol.
│   │   ├── collections.abc.Sequence             # Inherits from Sized, Iterable, and Container. Defines methods like __getitem__ and __len__.  
│   │   │   ├── str                              
│   │   │   ├── list
│   │   │   ├── tuple
│   │   │   └── range
│   │   ├── collections.abc.Set                  # a set is unordered collection of distinct elements
│   │   │   ├── set
│   │   │   └── frozenset
│   │   ├── collections.abc.Mapping              # Inherits from Sized, Iterable, and Container.  A mapping is unorder collection
│   │   │   └── collections.abc.MutableMapping   # Adds methods for modifying the mapping, like __setitem__, __delitem__, etc
│   │   │       └── dict
│   │   └── collections.abc.AsyncIterable
│   │       └── collections.abc.AsyncIterator
│   ├── collections.abc.Sized                    # Defines the __len__ method.
│   │   ├── collections.abc.Sequence
│   │   ├── collections.abc.Set
│   │   ├── collections.abc.Mapping
│   │   └── collections.abc.MappingView
│   │       ├── collections.abc.ItemsView
│   │       ├── collections.abc.KeysView
│   │       └── collections.abc.ValuesView
│   ├── collections.abc.Callable                 # Defines the __call__ method.  a functiontype has callable as its base
│   ├── collections.abc.Hashable
│   └── collections.abc.Awaitable
│       └── collections.abc.Coroutine
├── bool
├── bytes
├── bytearray
├── memoryview
└── NoneType

"""

from collections.abc import Iterable

class MyIterable(Iterable):
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return MyIterator(self.data)  # Returns an instance of MyIterator

class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0  # Start index

    def __iter__(self):
        return self  # Returns itself as an iterator

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1  # Move to the next index
            return result
        else:
            raise StopIteration  # No more items to return

# Using the custom iterable
my_iterable = MyIterable([1, 2, 3])
for item in my_iterable:
    print(item)
"""
Explanation:
MyIterable Class: This class is designed to be an iterable. It implements the __iter__ method, which returns an 
instance of MyIterator.
MyIterator Class: This class is the actual iterator. It keeps track of the current position in the data 
(self.index) and provides the __next__ method to return the next item in the sequence.
"""