"""
# what is :
: is the language construct which connects one language element with another. for example : connect function definition with body.
def max(a):
    a =a+1
    return a

here : links one construct with another. its connects function name with body

a=(1,2,3,4)
a=[1:2]   here : tell compile take index from 1 to 2 with step 1

dic ={1:"one", 2:"two"}  dictionary items inside {} can be key:value or key=value but without {} items are represented by key=value
here : associate key with value in dictionary
######################################################
# difference between (,) and [,]
These () are Associative Arrays called Tuples. And these [] are dynamic arrays called Lists. List are used generally for temporarily
storing data to be handled as mutable data-types(where they can be changed

In Python, a tuple with a single element can be created by placing the element inside square brackets,
which must be followed by a comma. The comma is not necessary for lists, but it is required for tuples to
distinguish them from a single value in parentheses.

single_element_tuple = (1,)
print(single_element_tuple)  # Output: (1,)
print(type(single_element_tuple))  # Output: <class 'tuple'>

 The trailing comma is optional in Python and does not affect the function call.
def tupetype2(a, b, c, d):
    print(a, b, c, d)

# Function call with a trailing comma
tupetype2(1, 2, 3, 4,)  # Output: 1 2 3 4



In Python, a list with a single element can be created by placing the element inside square brackets,
optionally followed by a comma. The comma is not necessary for lists, but it is required for tuples to distinguish them from a single value in parentheses.


a = [1,]
print(a)  # Output: [1]
print(type(a))  # Output: <class 'list'>


The tuple ll = (1, 2, 4, 5,) is a valid tuple with four elements. The trailing comma is
optional and does not affect the tuple’s validity or its contents


# List with a trailing comma
my_list = [1, 2, 4, 5,]

print(my_list)  # Output: [1, 2, 4, 5]
print(len(my_list))  # Output: 4


Associated arrary as immutables.   where dynamic arrays are mutable.
that is why () are passed to functions and procedures like
def maximum(a,b,c)  here function is being called as maximu(1,2,3) and the assiciated array passed is (1,2,3) in function
a=array[1],  b=array[2] and c=array[3].   the function take care of this assignment automatically

Tuples on the other hand are Immutable and cannot be changed and handle much more than data-types but can handle everything as Mapped
 pointer stored objects such as Built In Functions, Methods, Functions, Classes, Data-types, Sets, among hundreds more and Lists also.

Tuple’s are also the Associative Array Structure that sets the entire Python language to be Object Oriented along with allowing Functional
Programming and Procedural to flourish side by side with it.

These Tuples give Python its Multi Paradigm Punch while Python’s List Dynamic arrays are not set in any specific numeric order as most other
languages arrays do. Except for Java’s ArrayList arrays which work the same.

In Python everything is set inside Tuples. Such as:

everything_named_here_and_inside(—here—) are Associative Arrays Tuples . Including examples:
print()
int()
str()
bool()
float()
myMethod()
Pythons built in “methods()”
They are also used to create these below but without the “()” and these require the user to implement the Object or Method
“Name-????” along with the closing brackets—“()”.

A C’s Class class(name, *args, **kwargs): creates them. And In the Python Lib’s become a “class ??name??():”—which then allows creation of
the Class method as class ????() in Python.
And def(): is also created by a C’s Class as an Associative Array “def()”—-which is also created using a class object tuple() def ????().
And in fact Lists are also created by Tuples in C language which Python calls to build their lists method: —-list()—to—name????[].


basic classes in python

name = "YouTube"
type(name)
<class str>

int()
float()
str()
set()
list()
slice()
name ="YouTube"
name.
"""

def apply_discount(product, discount):
    price = int(product['price']* (1.0 - discount))
    assert 0 <= price <= product['price'], " The Given Discount is invalid ..."
    return price

shoe ={'name' :'Fancy Shoes', 'price':14900}
print("Price as discount is: %i" %apply_discount(shoe, 0.25))

# assert implement _DEBUG_ if -O option is not given in compiler.  the option is used for testing
# and used for debugging
# asset is used for debugging the programing.
#print("Price as discount is: %i" %apply_discount(shoe, 2.0))

a = [1,2,3,4,5,6,7,8]

y =   tuple(x*x  for x in a)
print(y)

y= list(x*x  for x in a)
print (y)

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