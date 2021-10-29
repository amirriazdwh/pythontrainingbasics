"""
in functions the values of argument is immutable.  the logic inside the fuction cannot change it
---------------------------------------
1.  First-Class Functions
---------------------------------------
     means function can be assigned to variables
     functions can be passed as argument to functions
     function  can return functions
     functions can be used as expression.
     function can be defined and run inside function
"""
import functools

items =[1,2,3,4,5,6,7,8,9]
total = functools.reduce(lambda a, b: a+b, items)
print(total)

totallist =list(map(lambda b: b*2 ,items))
print(totallist)

list(filter(lambda x: x > 100, [1, 111, 2, 222, 3, 333]))
