"""
in python are variables are objects and can be deleted by del function
-------------------------------------------------------------------------
1.  Numbers  types are Int, float, bool and complex
-------------------------------------------------------------------------
int              defines integer. its an object of type <class 'Int'> an integer has derived types String so integer can be converted to string
float           defines  object of types <class 'float'>
bool           a boolean data types contains three values,  None, True and False and its of type <class 'bool'>
complex     number like 6+4j if of type <class 'complex'>
-------------------------------------------------------------------------
2.  String types are string
-------------------------------------------------------------------------
character  define by a single character and convert from digit to character by chr  function and from chr to ASCI digital by ord.  each character has
an ordinal number associated with it.  to convert a ord to character use chr(num) and a character can be convert to ord by ord() func
a sequence of characters list or tuples can be converted to string by "".join(sequence). we can represent string by ' or ".  we dont
have chr  datatype in python,  we have string.  character is of type String of class <class String>

String  defined by ""  double qoutte or ''  single quote.  The char is defined by ''. single or ""  double quote.  Multi-line strings can be denoted using triple quotes, a
string is a sequence so they can be accessed by index.  a string is basic data types of integer so string can be converted to int
using int. function.  a string can be converted to list and tuples by list() and tuples()
--------------------------------------------------------------------------
3.  There are seven sequence types: strings, Unicode strings, lists, tuples, bytearrays, buffers, and xrange objects.  sequences also called ordered collection
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
-------------------------------------------------------------
-   4.   Set and Dictionary  are unordered collection
-------------------------------------------------------------
A set object is an unordered collection of distinct hashable objects. Common uses include membership testing, removing duplicates from a sequence,
and computing mathematical operations such as intersection, union, difference, and symmetric difference. (For other containers see the built in dict, list,
and tuple classes, and the collections module.)

set     defined as {}.  since sets are unorders they dont have an index. we use set() function to convert all sequence to set
Dictionary   defined by {} with items as key:value  used dict() for covnersion.
                    note: that item inside {} are written as key:value or key=value but without {} its been represented as key=value
                    dic ={i:f"item{i}" for i in range(1,10)}.  with f you can using {}
                    Note:  a json file is a dictionary saved in a file
                    Note:  a dictionary is a ziping of two sequence stud by stud.  thats why zip function is using to
                    create a dictionary from two sequences. just like a zip can be unzipped.  we can use unzip funtion to
                    get key and values in two difference sequences.  keys are unique and immutable in dictionary
None    is an object defined to represent null values.   its type is <class 'NoneType'>.  when a variable is
         not assigned any value its None.  in if expresion is evaluated as  if varis is None:  print("None")
range    is data type with iterator its called generator its type is <class 'range'>
###########################################################################
in python string, list and tuples are order sequences so they can be type casted
in python set are unorder seqeuence. list, tuples, string, range are order sequence
since both order sequence and unorder sequence are derived for sequence therefore a set con be converts to list, tuple or stirng
###########################################################################
in dictionary key must be unique.  while values can be repeated.  thats why its being represent by {} since in sets the
values are not repeated. in same way in diction the keys are not repeated.  dictionary was created since it was not possible to
access an individual element in a set without scanning the whole set.
to get the keys we use.  d.keys and for values d.values and to get both keys and values as tuple we use d.items
--------------------------------------------------------------------
class dict(**kwarg)
class dict(mapping, **kwarg)
class dict(iterable, **kwarg)

There are three standard sequence operations (+, *, []) ==, >,< >= , <=
 that can be performed with tuples as well as lists and strings.
------------------------------------------------------------------------------------------------------------------------------
"""
########### complex data types ####
compNum = 6+4j   # instead of i j is being used in python
print(compNum)

############# boolean ########
vTrue =True
vTnum = int(vTrue) # gives 1
vTrue =False
vTnum =int(vTrue) # gives 0   false if null or empty

############# Integer ########
vChar ="23"  # define string
# convert Str to integer
vInt = int(vChar)
print(vInt)

# del will remove the memory allocation of vInt and therefore it will not be accessable in str(vInt).
#del vInt
#print(vInt)

# convert Integer to String.  since string is basic datatypes and integer is derived from it. string can be convert to int
vChar = str(vInt)
print(vChar)

############ charater to Asci and asci to charater ########
print("convert Character to ord",ord('c'))
print("convert ord to character ",chr(99))
print(chr(97))
print(chr(65))
print(chr(1200))

# return 65
print(ord('A'))

#####################################################
#bytes([source[, encoding[, errors]]])
#####################################################
string = "Python is interesting."

# string with encoding 'utf-8'
arr = bytes(string, 'utf-8')
print(arr)

string.encode(encoding='UTF-8',errors='strict')
print(string)

':'.join(['toto','12','pswd'])

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
#print("the number is  ", xx[1::-1])

print("------keys then value------")
tupleNum = tuple((x for x in (('x', 'y', 'z'),(1, 2, 3))))
print(tupleNum)

# first tuple added to tuple and then second tuple added

print("------create flat tuple------")

flatuple = tuple(x for ele in tupleNum for x in ele )
print(flatuple)

# a for loop need a sequence to run. left loop creates a sequence being used by the second loop

print("---- create diction -----")
tupleZipNum = tuple(zip(('x', 'y', 'z'), (1, 2, 3)))
print(tupleZipNum)

###########################
print("---- create enumeration -----")

a=('x', 'y', 'z')
b=(1, 2, 3)

for i,x in enumerate((a,b)):
    print(i,x)
"""
print('_____________________________________')
dic = dict((i, x) for tupEle in (xx,yy) for (i, x) in enumerate(tupEle))
print(dic)
print('_____________________________________')

"""


#def solve(lis, n):
#    it = iter(lis)
#    return [list(islice(it, n)) for _ in range(len(lis)/n)]

#solve(range(1,9),4)

##############################################
# list to dict conversion
###############################################
numbers1 = dict([('x', 5), ('y', -5)])
print('numbers1 =',numbers1)

# keyword argument is also passed a tuple is part of dictionary which can be represented as z=9
numbers2 = dict([('x', 5), ('y', -5)], z=8)
print('numbers2 =',numbers2)

###############################################
# zip() the list creates an iterable in Python 3
################################################
number0=zip(['x', 'y', 'z'], [1, 2, 3])
print(number0)
numbers3 = dict(zip(['x', 'y', 'z'], [1, 2, 3]))
print('numbers3 =',numbers3)
