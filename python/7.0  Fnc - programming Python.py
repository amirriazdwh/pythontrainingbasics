"""
---------------------------
1.   pure functions
---------------------------
      a.   idempotent  ( a function you can apply multiple times without changing the result)                  -  idempotent
      b.   global state    ( does not change the global state)                                                                             -   No side effects
      c.    function argument ( cannot be changed )                                                                                          -   no mutation of variable or sharable objects
      d.    because of b and c the return will always be same.    means result will be idempotent

---------------------------------------
2.  First-Class Functions  - (functions can act like variables)
---------------------------------------
     means function can be assigned to variables
     functions can be passed as argument to functions
     function  can return functions
     functions can be used as expression.
     function can be defined and run inside function

in order to build to make a functions as first class citizen following things are needed.
1,    lambda functions
2.    partical functions
3.    clousures
4.    recursions
5.    decorators
6.     currying function
----------------------------
3.  lambda function   ( these functions can be passed as argument,  assigned to variable and return from function).
----------------------------
these are anonymous functions are called lambda functions because  they are nameless and can be returned, passed to functions
or assigned to a variable.

lambda arguments: expression
in functions the values of argument is immutable.  the logic inside the fuction cannot change it

1.     filter(<f>, <iterable>)  ,
2.     map(<f>, <iterable>) ,
3.    from functools import reduce        reduce(<f>, <iterable>),   partial
"""

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# Use lambda function with `filter()`_ under score are throw away
# variables

filtered_list = list(filter(lambda x: (x * 2 > 10), my_list))
filtered_list1 = list(filter(lambda _: (_ * 2 > 10), my_list))
# filtered_list2 = [filter(lambda _: (_ * 2 > 10), my_list)]   this will not work as [] cannot convert generator to list

print(filtered_list)

# Use lambda function with `map()`
mapped_list = list(map(lambda x: x * 2, my_list))

print('.... this is list ...')
genobj = map(lambda x: x * 2, my_list)

# genobj can be used in for loop
mapped_list = [x for x in genobj]
print(mapped_list)

#  use lambda with reduce function.   it comes from functools

from functools import *

items = [1, 2, 3, 4, 5, 6, 7, 8, 9]
total = reduce(lambda a, b: a + b, items)
print(total)

"""
----------------------------
Partical Functions 
----------------------------
Partial functions can be used to derive specialized functions from general functions and therefore help us to reuse our code.
this is more like a method oops in sub class which has been specialized with one value but not being privided with second values 
the second value needs to be privided by sub-class method
"""


# A normal function
def add(a, b, c):
    return 100 * a + 10 * b + c


# A partial function with b = 1 and c = 2
add_part = partial(add, c=2, b=1)

# Calling partial function
print(add_part(3))

"""
--------------------------
currying function
--------------------------
We define the composition h of two functions f and g
h(x)= f(g(x))
in the following Python example.
The composition of two functions is a chaining process in which the output of the inner function becomes the input of the outer function.

def compose(g, f):
    def h(x):
        return g(f(x))
    return h
"""
from compose import compose

def celsius2fahrenheit(t):
    return 1.8 * t + 32

def readjust(t):
    return 0.9 * t - 0.5

convert = compose(celsius2fahrenheit, readjust)

measurement_of_thermometer = 10
print("Temperature is :", convert(measurement_of_thermometer))

"""
----------------------------
 recursive function
 -----------------------------
 in procedural language we used loops to compute iterative values.   in functional programming recursive function do the same
 reasons are,  some formula are being represented in a simple way,  so recursive function make code easy.    also since pure functions 
 are being used for computation so calculation is less error pron.   for example factorial is being represented as 
 
 factorial(x)  =  {  1                          }     if x=0
                         {   x* factorial(x)    }  for all value of x other than x=1
"""
def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


num = 3
print("The factorial of", num, "is", factorial(num))


"""
-------------------
closure
-----------------
This technique by which some data ("Hello in this case) gets attached to the code is called closure in Python.

Closures can avoid the use of global values and provides some form of data hiding. It can also provide an object oriented solution to the problem.
When there are few methods (one method in most cases) to be implemented in a class, closures can provide an alternate and 
more elegant solution. But when the number of attributes and methods get larger, it's better to implement a class.
Here is a simple example where a closure might be more preferable than defining a class and making objects. But the preference is all yours.

"""
def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier


# Multiplier of 3
times3 = make_multiplier_of(3)

# Multiplier of 5
times5 = make_multiplier_of(5)

# Output: 27
print(times3(9))

# Output: 15
print(times5(3))

# Output: 30
print(times5(times3(2)))
"""
------------------------------------------------------------------------
Decorates in python with tag and without tag
------------------------------------------------------------------------
"""


def add_num(message):
    def add_inc(increment, numbers):
        message()
        incremented_nums = []
        for n in numbers:
            incremented_nums.append(n + increment)
        return incremented_nums  # this retruns a function ,  functions only execute if we add ( )

    return add_inc


@add_num
def message1():
    print("Doing something...")


# message1 = add_num(message1)
print(message1(5, [28, 93]))

even_square_numbers = [x ** 2 for x in range(5)
                       if x % 2 == 0]
even_square_numbers  # [0, 4, 16]
