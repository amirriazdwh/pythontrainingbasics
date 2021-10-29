"""
in functions the values of argument is immutable.  the logic inside the fuction cannot change it

1.     lambda arguments: expression
2.     filter(<f>, <iterable>)  ,  map(<f>, <iterable>) ,
3.   from functools import reduce        reduce(<f>, <iterable>),   partial



---------------------------------------
1.  First-Class Functions
---------------------------------------
     means function can be assigned to variables
     functions can be passed as argument to functions
     function  can return functions
     functions can be used as expression.
     function can be defined and run inside function


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
        return incremented_nums      # this retruns a function ,  functions only execute if we add ( )

    return add_inc

@add_num
def message1():
    print("Doing something...")


#message1 = add_num(message1)
print(message1(5, [28, 93]))

