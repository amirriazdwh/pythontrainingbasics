# theory
"""
1. Packing and Unpacking
packing means create an object from multiple objects.  from many attributes one object is created.  this is being handled by
 creation of one new object.  By composing mutliple object into one.
Unpacking means create multiple objects from one object.

2. a object contains method _new_ , _iter_ _init_  these methods are called from inside the functions,  for example _iter_ is called
from iter function.   _init_ is called when object is being created.

3.  *arg means,  the object has a single iterator so it can be a list, tuple, array or set.   **karg means the object has two iterators
     so it is a dictionary.  please note that arg and karg are iternator so they can be used in streaming and in for loop.  a dictionary is
     being created by zip function with two sequences lets say s1 and s2.  so dic =zip(s1,s2).  zip function stitch sequence by index
     means {s1[1]:s2[1], s1[2]:s2[2]}
4.  a statement *arg, =1,2,3  is called packing and a statement a,b,c,d =arg
"""
################################
# Examples
###############################
# normal packing and unpacking

# packing object of string to tuple and assigning it to pack
p0 = ("apple","mango","orange")

# unpacking here objects of pack are assigned to p1,p2,p3 by position
p1,p2,p3 =p0

# note a sequence is an iterator,  therefore (),[] and {} are all have iterators
# we can embed another iterators inside these iterator.  by *arg,  here outer iterator come for sequence and
# inner iterator comes from *arg. if a *arg iterator receive elements,  it perform packing,  it *arg gives values it unpack

# this is packing,  the object tuple packs object of type string to p4
p4 = ("apple","mango","orange", "banana", "fig")

#here outer iterator assign values to p5 and for p6 both out and inner iterator works to assign values and in end p7 is assigned a value
# if *arg, is assigned a tuple and its a part of tuple, it will unpack the element of tuples by iterator and then pack elements using
# iterator of arg.  *arg is used to pack unlimited element at function level. when *arg is function parameter
# here unpacking is happening but pack is happening for p6.
p5,*p6,p7 =p4
print("P5:",p5)
print("P6:",p6)
print("P7:",p7)

# *arg is used to pack a sequence of elements.
print("\n Packing values in a function")

v_list =[1,2,3,4,5]

print("\nPacking elements:")

# there is only one parameter, note in a function,  the arguments are passed by position , so if the defination is
#  def mySum(args):  we can only pass one parameter.  which can be either one variable or one sequence
#  in order to pass multiple parameter we have to pack those element using iterator and get a tuple
#  that is mySum(1,2,3,4) will be like  *args, =(1,2,3,4)

def mySum(*args):
    print(type(args))
    print(args)
    sum = 0
    for i in range(0, len(args)):
        sum = sum + args[i]
    return sum

# Driver code
print("Sum 1 to 5:",mySum(1, 2, 3, 4, 5))
print("sum 10 and 20:",mySum(10, 20))

#here *v_list will unpack and create elements 1,2,3,4, 5 which is being packed again by argument
# here iterator *v_list is producing values so its unpacking the list
print("sum a tuple passed unpack:",mySum(*v_list))

def dummy(*args):
    print(type(args))
    return args

# here iterator will add elements to tuple by position which are two lists.
print("This will add lists to tuple in args:",dummy(v_list, v_list))
print("This will add list to tuple and unpack elements to args:",dummy(v_list, *v_list))

print("\nUnpacking example")
my_list = [1, 2, 3, 4]

def fun(a, b, c, d):
    print(a, b, c, d)

# here *my_list will unpack [1,2,3,4] to 1,2,3,4  since *arg is always a tuple therefore 1,2,3,4 will beocme (1,2,3,4)
fun(*my_list)

print("############ Testing #############")

fruits =("apple","orange","mango")

# (*fruit, fruit) is a tuple first since value is being assigned it will unpack and give elements for first argument
v0=*fruits, fruits

#(*fruit, fruit) is translated to ('apple', 'orange', 'mango', ('apple', 'orange', 'mango'))

p =*v2,=*fruits, fruits
v3=fruits, fruits
print("P:",p)
print("v0:",v0)
print("v2:",v2)

print("v3:",v3)
print("(*v3,):",*v3,)

# A Python program to demonstrate both packing and
# unpacking.

# A sample python function that takes three arguments
# and prints them
def fun1(a, b, c):
    print(a, b, c)

# Another sample function.
# This is an example of PACKING. All arguments passed
# to fun2 are packed into tuple *args.
def fun2(*args):
#   in case of *args are tuples ('Hello', 'beautiful', 'world!')
    print(args)
    print(type(args))
    # Convert args tuple to a list so we can modify it
    args = list(args)
    # Modifying args
    args[0] = 'Geeksforgeeks'
    args[1] = 'awesome'
# UNPACKING args and calling fun1()
    fun1(*args)

# Driver code
fun2('Hello', 'beautiful', 'world!')

print("\n############## Swaping in Python ###########")
##################
# swap values
##################
a=2
b=3

#swapping the a with b
a,b =b, a

print("A:",a)
print("B:",b)

################################################
# use of _ in unpacking,  its similar to scala
###############################################

print("\n using _ in python similar to scala")
test =(1,2000,3)
_, x, _ =test
print("x:",x)

##########################################
# unpacking arbiltary number of tuples
###########################################
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print(phone_numbers)

##############################
#  some package practice
###############################
import heapq
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums)) # Prints [42, 37, 23]
print(heapq.nsmallest(3, nums)) # Prints [-4, 1, 2]


#from collections import deque
#def search(lines, pattern, history=5):
#    previous_lines = deque(maxlen=history)
#    for line in lines:
#        if pattern in line:
#            yield line, previous_lines
#        previous_lines.append(line)

# Example use on a file
#if __name__ == '__main__':
#    with open('somefile.txt') as f:
#        for line, prevlines in search(f, 'python', 5):
#            for pline in prevlines:
#                print(pline, end='')
#        print(line, end='')
#        print('-'*20)

##################################
#  Working with dictionaries
###################################

row1= {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003}
row2= {'fname': 'David', 'lname': 'Beazley', 'uid': 1002}
row3 ={'fname': 'John', 'lname': 'Cleese', 'uid': 1001}
row4 ={'fname': 'Big', 'lname': 'Jones', 'uid': 1004}

print("\n############## Get both iterator ############")
for key, value in row1.items():
    print(key, value)

print("\n############## Get items ############")
for item in row1.items():
    print(item)
    print(type(item))

print("\n############## Get Key ############")
for key in row1.keys():
    print(key)

print("\n############## Get both value ############")
for value in row1.values():
    print(value)

def showRecord (**arg):
    # packs the argument passed into dictionary
    print(type(arg))
    # the arguments have been packed into a dictionary
    print(arg)
    print("First name:", arg['fname'])
    print("Last name:", arg['lname'])
    print("uid:", arg['uid'])
    print("\n")


showRecord(fname="amir", lname="Riaz", uid=1000)
showRecord(**row1)

print("\nUpacking rows contain dictionary")
def showRecord2 (fname, lname, uid):
    print("First name:", fname)
    print("Last name:", lname)
    print("uid:", uid)
    print("\n")

showRecord2(**row1)



d = {
'a' : [1, 2, 3],
'b' : [4, 5]
}
e = {
'a' : {1, 2, 3},
'b' : {4, 5}
}


rows= [
{'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
{'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
{'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
{'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

from operator import itemgetter
rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print("Row Sorted by First Name:\n",rows_by_fname)
print("Row Sorted by uid:\n",rows_by_uid)

# in a function if an argument, *arg and **karg is define,  there must be a order

def foo(requried, *args, **kwargs):
    print(requried)
    if args:
        print(args)
    if kwargs:
        print(kwargs)

# * and ** say,  0 or more than one arguments.
foo("hello")
foo("hello",1,2,3,4)
foo("hello", 1,2,3,4, key1='values', key2=999)
foo("hello", 1,2,3,4, key1='values', key2=999)

# args and kargs are using to modify arguments and then call a new function.  here print(new_args) is called
def foo1(x, *args, **kwargs):
    kwargs['name']='Alice'
    new_args = args+ ('Extra',)
    print (new_args)

foo1("hello", 1,2,3,4, key1='values', key2=999)


