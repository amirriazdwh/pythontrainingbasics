############################
# Tuples are immutable
############################
# x,y =(2,3) unpacking a tuple.  dictionary return tuples
# a tuple is immutable while list is mutable
#all sequence in python are inter-changable, sequence are list, tuple, xrange,string
# all sequences have iterators through which they can be iterated
## * and ** function argument unpacking.  * will unpack sequence and ** will unpack dictionary by same key names
# if * is on variable side,  it will pack sequence list, string for example def foo(*ll) will pack foo(1,2,3,4)
# if * is on argument side it will unpack for example def foo(x, y, z)  ll=(1,2,3)  foo(*ll)
#There are three standard sequence operations (+, *, []) ==, >,< >= , <=
# that can be performed with tuples as well as lists and
# a list has a key and values you can get the key values pairs by list.items
# * in function, or in tuple will unpack any struct of types seq that is list or tuple
# in python list and tuples are type of sequence and can be unpacked in a similar way
# strings.
from itertools import islice

# define any empty tuple
tup =()
# define any empty list
ls =[]
# define dictionary
dic ={}

t1 = ('a',)
print(type(t1))

t2 = ('a')
print(type(t2))

t = tuple()
print(t)

##################
# conversion,  all sequence in python are inter-changable, sequence are list, tuple, xrange,string
##################
#
# string to tuple
print("**** string to tuple *****")
str1="lupins"
print(str1)
tt = tuple(str1)
print(tt)

print("**** tuple to string *****")
#tupel to string
print(tt)
str01=''.join(tt)
str01=str().join(tt)
print(str01)
#
print("*************** convert tuple to list *****************")
print(tt)
# convert tuple to list
lstup = list(tt)
print(lstup)

# convert list to tuple
print("***************Convert list to Tuples*****************")
print(lstup)
tt=tuple(lstup)
print(tt)


print("*************** + is concatination operator ***************")
rr=(1,2,3)
xx=(1,2,3)
yy=(4,5,6)

# this is concatinate
zz = xx + yy
print(zz)

print("******** this is concatination with itself two fold **************")
# this is concatination with itself two fold
zz = xx*2
print(zz)

# 3 fold concatination
zz = xx*3
print(zz)

#not allowed
# zz=xx*yy
# zz=xx-yy
# zz=xx/yy

if(xx==rr):
    print(" the tuples are equal")

if( xx >= rr):
    print("x is greater than yy")

###############
# Tuples unpacking
###############
print("____tuple packing unpacking_____")
# unpacking means remove brackets and assign if variables are available,  for example
# x, *y =(1,(2,3)). *y means unpack tuple, list,
# set it remove () from tuples, list. here x,*y=(1,(2,3)) is translated as
# x, y[0], y[1]
# *y is translated to y[], y[] its call list or tuple or set
print("####### packing tuple #########")
x,*y=(1,2,3)
print("x is ",x)
print("Y is ",y)

x,y =(2,3)
print(x,y)

# x,y and (x,y) is the same
(x,y) =(1,(2,3,4,5,6,7))
print(x)
print(y)

print("######### unpacking a list###############")
data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
name, shares, price, date = data
print( name, shares, price, date)


print("#### packing tuples #########")
t1=(1,2,3,4)
t2=(5,6,7,8)

z=(*t1,*t2)
print(z)
print("########## Packing tuples without * ############")
zz=(t1,t2)
print(zz)
x, y =zz

# x is normal arg,  *y converts the tuples into list in function parameter
# any list inside tuples is coverted to tuples
lstoup =[1,2,3,4,5]
z =(100,*lstoup)
print(z)
# in function parameters
def unpack_tuple(x, *y):
    # conc
    print(y + (x,))

unpack_tuple(10,zz)
unpack_tuple(10,lstoup)

print("____tuple packing unpacking_____")

##############################
# TUPLES OPERATIONS
#############################

# vowels tuple
vowels = ('a', 'e', 'i', 'o', 'i', 'o', 'e', 'i', 'u')

# count element 'i'
count = vowels.count('i')

# print count
print('The count of i is:', count)
print('The Tuple Length is:', len(vowels))

txt = 'but soft what light in yonder window breaks'
words = tuple(txt.split())
print(words)

addr = 'monty@python.org'
uname, domain = addr.split('@')
print(uname,domain)
#############################################################
# zip performs cross product.  zip, filter, iter and map function
#  return object
zz=tuple(zip(xx,yy))
print(zz)

a=['a1']
b=['b1','b2','b3']
c=['c1','c2']
print(tuple(zip(a,b,c)))

#############################
# Slice concept in python
#############################
print("######### Slicing ###########")
lst =(10,20,30,40,50)
# -1 step require that startvalue is bigger and end value is smaller
#  +1 step require smaller startvalue and bigger end value to get result
# each -ive number is converted to positive by substracting for length
# here -1 is converted to 5-1=4 and -3 to 5-3=2. when -1 step start will be greater
#  and end will be smaller.  first impression is converted to second
# number of elements are determined by (startvalue-endvalue) for +ive and vice versa for -ive
print("the number is  ", lst[-1:-3:-1])
print("the number is  ", lst[4:2:-1])

# here -1 is converted to 4 while 1 is not converted since it +ive
print("the number is  ", lst[-1:1:-1])
# here -1 converted to 4 and our range is 1:4 which will only give result with +ive step
# if you make the step positive we will get the result
print("the number is  ", lst[1:-1:-1])
print("the number is  ", lst[1:-1:1])

# in same way this gives result
print("the number is  ", lst[2:4:1])
# while this nothing
print("the number is  ", lst[2:4:-1])
########################################################
print("############# print expression ###############")

#'__iter__' in dir([1,2,3])           # returns True
#'__iter__' in dir((1,2,3))           # returns True
#'__iter__' in dir(range(3))      # returns True
#'__iter__' in dir(3)                   # returns False

pow2 = (2 ** x for x in range(10))
print(list(pow2))

# expression are like foreach loop is scala
pow2 = (2 ** _ for _ in range(10))
print(list(pow2))

# this is like for loop in scala
def create_tuple():
    for x in range(10):
     yield x

# this creates an expression object which is iterables
# sometuple + (someitem,)
tip = (x for x in create_tuple())
print(tuple(tip))

print("________how to add tuple element by for loop_______")
a=tuple()
for x in range(10):
    a+=(x,)

print(a)

print("_________ Dictionary conversion from single tuples _________")
dicpow = tuple((i,x) for i,x in enumerate(('x', 'y', 'z')))
print(dicpow)
# convert tuple to dictionary
print(dict(dicpow))

print("______convert two dimension tuple to_______ ")
# here x=1 with no natural index
tupleNum = tuple((x for x in zip(('x', 'y', 'z'),(1, 2, 3))))
print(dict(tupleNum))

print("______ flaten two dimensional tuples__________")
flatuple = tuple(x for ele in tupleNum for x in ele)
print(flatuple)

print("________zip__tuples_____________")
tupleZipNum = tuple(zip(('x', 'y', 'z'), (1, 2, 3)))
print(tupleZipNum)

a=(4, 5, 6)
b=(1, 2, 3)

print("__two dimension tuples to dictionary with index____")
# here a and b are elements of tuples with index 0 and 1
flat_tup_index=( (i,x)for i,x in enumerate((*a,*b)))
print(dict(flat_tup_index))

print('____flaten__two_dimensional_tuples_to_one___')
tdic = dict((i, x) for tupEle in (a,b) for (i, x) in enumerate(tupEle))
print(tdic)

flat_tup_index=( x for x in (*a,*b))
print(tuple(flat_tup_index))

print('_____________________________________')


#def solve(lis, n):
#    it = iter(lis)
#    return [list(islice(it, n)) for _ in range(len(lis)/n)]

#solve(range(1,9),4)
print(" List Work____________________________________________________")
import itertools

zz = tuple(itertools.zip_longest(a, b, c))
print(zz)

tzz = tuple(itertools.zip_longest(*zz))
print(tzz)

print("____________________________________________________")
A = (1,2,3,4,5,6,7,8,9)
B = ("A","B","C")

from itertools import cycle

zip_list = tuple(zip(A, cycle(B)) if len(A) > len(B) else zip(cycle(A), B))
print(zip_list)

print("____________________________________________________")

kk =('a', 'b', 'c', 'd')
mm =(1, 2, 3, 4)
nn = tuple (zip (kk, mm))
print(nn)
ll = tuple(zip(*nn))
print(ll)

print("____________________________________________________")
from itertools import chain
tt=tuple(chain.from_iterable(nn))
print(tt)
print("____________________________________________________")


def print_vectory(x, y , z):
    print("<%s %s, %s>" %(x,y,z))
unpseq = (1,0,-1)
print_vectory(*unpseq)

unpdic ={'x':1, 'y':0, 'z':-1}
print_vectory(**unpdic)

def foo(required, *args, **kwargs):
    # args collect position operator
    # kwags collect key values function
    print(required)
    if args:
        print(args)
    if kwargs:
        print(kwargs)

foo("Hello")
foo("Hello", 1,2,3,4, key1=10, key2=20)

# packing function
def listPack (*lis):
    print(lis)
listPack(1,2,3,4,5,67)

def listunPack(x,y,z):
    print("<%s %s %s>"%(x,y,z))
ll =(1,2,3)
listunPack(*ll)

# convert list to dictionary
# enumerate is a class which take the iterator and return a index and value
enls =[100,200,300,400]
pairls =enumerate(enls,start=1)
print(dict(pairls))

# List of strings
listOfStr = ["hello", "at" , "test" , "this" , "here" , "now" ]
# List of ints
listOfInt = [56, 23, 43, 97, 43, 102]

# Create a zip object from two lists
zipbObj = zip(listOfStr, listOfInt)
# Create a dictionary from zip object
dictOfWords = dict(zipbObj)