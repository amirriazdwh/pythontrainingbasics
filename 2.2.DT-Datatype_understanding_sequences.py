"""
a[i:j] is a order sequence of length j+1.  where k is index seuqence
Sequences also support slicing: a[i:j] selects all items with index k such that i <= k < j. When used as an expression,
a slice is a sequence of the same type. This implies that the index set is renumbered so that it starts at 0.

Some sequences also support “extended slicing” with a third “step” parameter: a[i:j:k] selects all items of a with index x
where x = i + n*k, n >= 0 and i <= x < j

note: order sequence are   string, list, tuple, range, xrange,
      Unorder sequence are:  set, dictionary,

      immutable : frozenset(), bytes,
      mutable :bytearray
-------------------------------
basic operations on sequences,  these operation are common is all classes derived from sequence
------------------------------
x in s	1 if an item of s is equal to x, else 0
x not in s	0 if an item of s is equal to x, else 1
s + t	the concatenation of s and t
s * n , n * s	n copies of s concatenated	(1)
s[i]	i'th item of s, origin 0	(2)           all sequence can be accessed by s[k] where k is index
s[i:j]	slice of s from i to j	(2), (3)          all sequence can be accessed as slice,  the same behave is present in range function
len(s)	length of s
min(s)	smallest item of s
max(s)	largest item of s
"""
####################################
# a tuple is an order sequence which is immutable
####################################
print("\nusing tuples:")

t1 = ("Apple","Oranges")
t2 = ("Banana","Fig")

# get by index
print(t1[0])
# concatinate
print(t1+t2)
# check in list
if "Apple" in t1:
    print("Apple is in list t1")


# basic sequence functions
rr=(1,2,3)
xx=(1,2,3)
yy=(4,5,6)

zz=xx+yy
print(zz)

zz = xx*2
print(zz)

#not allowed
# zz=xx*yy
# zz=xx-yy
# zz=xx/yy

if(xx==rr):
    print(" the tuples are equal")

if  (xx>=rr):
    print("x is greater than yy")

################
# a list is an order sequence which is mutable
##################
print("\nusing lists:")

a0=[10,20,30,40,50]

if 10 in a0:
    print("10 is in sequence")
    print(a0[0])

# sequence concations both a and b should be sequence
a1=[10,20,30,40,50]
b1=[60,70]

print(a1+b1)

# print(a1+100) will not work
# concate multiple times, this will concatinate the list to same list by n
a1=[10,20,30,40,50]
print(a1*3)

# Sequence slicing operation
a=[10,20,30,40,50]
b=[60,70]
print(len(a))
print(a[1:3])

# length is 5 so i=1 and j=5 so k=1,2,3,4.  note that at j=5 no out of index exception is thrown
print(a[1:])

# length is 5 and i=1 and j=5-2=3 so k =1,2
print(a[1:-2])
print(a[1:-2])

#####################
# a string is can order sequence which is immutable
####################
print("\nusing string:")

name = "YouTube"
print(name[1])

if 'Y' in name:
    print(" Y is in youtube")

################
# using xrange
#################
print("\nusing xrange:")

r = range(1,10)
print(r[3])
print(type(r))

#####################################################################################
# dictionary is an unorder sequence therefore cannot access by index
# we cannot access a specific elements in a set.  we have to iterate over whole set
# to get the element in for loop.  thats why map or dictionaries are being used.
# dictionary mark a specific element by key while keeping the key unique like a set
###################################################################################
# initialize my_set
my_set = {1,3}
print(my_set)

# if you uncomment line 9,
# you will get an error
# TypeError: 'set' object does not support indexing

#my_set[0]

# add an element
# Output: {1, 2, 3}
my_set.add(2)
print(my_set)

# add multiple elements
# Output: {1, 2, 3, 4}
my_set.update([2,3,4])
print(my_set)

# add list and set
# Output: {1, 2, 3, 4, 5, 6, 8}
my_set.update([4,5], {1,6,8})
print(my_set)
############################
# a dictionary is mutable
# a dictionary is an unorder sequence and is a set with index used as key
# dictionary are like sets which are index by key
# here to keep the properties of set key is unique while values can duplicate
###########################

m = {1:"Apple",2:"Orange",3:"Banana"}
print(m[1])

import collections
print('Regular dictionary:')
d = {chr(k):k for k in range(ord('a'), ord('g'))}
for k, v in d.items():
    print(k, v)
print('\nOrderedDict:')
d = collections.OrderedDict()
[d.setdefault(chr(k), k) for k in range(ord('a'), ord('g'))]
for k, v in d.items():
    print(k, v)

#############################
#   Map is not a datatype in python. It applies a function to a series of values and returns the result.
#############################