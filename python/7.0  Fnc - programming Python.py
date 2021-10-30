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
2.       map(<f>, <iterable>) ,
3.   from functools import reduce        reduce(<f>, <iterable>),   partial
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
mapped_list = [x for x in genobj]
print(mapped_list)

"""








"""

# Program to show the use of lambda functions
double = lambda x: x * 2

print(double(5))

import functools

items = [1, 2, 3, 4, 5, 6, 7, 8, 9]
total = functools.reduce(lambda a, b: a + b, items)
print(total)

totallist = list(map(lambda b: b * 2, items))
print(totallist)

list(filter(lambda x: x > 100, [1, 111, 2, 222, 3, 333]))

"""
Decorates in python with tag and without tag
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
