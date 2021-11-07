"""
types of functions in python
1.  dunder functions.     also call magic functions.
2.  function
3.  lambda functions
4.  object functions
5.  nested functions

important points
1.  functions are objects in same way as in scala and each functions has its __default__ dunder function which initial
    the default arguments.
2.  function objects are created when in code def is encounter.
3.  a function has its own dictionary so a function has its own scope.  in same way global and buildin has their own
    scope and own dictionary.    python compiler first looks for an variable in function in its own scope/dictionary if
    not found,  looks in global dictionary/scope
4.  function default variables are created in global scope
5.  since a function is an object,  it can be passed to another function
6.  since a function is a variable   its can be assigned to a variable.
7.  a function when assigned to a variable has reference to function object and this function variable to function object
    reference maping is store in dictionary.  since function is a object it can be delete as del function
8.  in python all the variable must be initialized before any operation like addition or subtraction should be done.
    if the variable initialization is global scope and addition operation is function local scope then function will not
    able to mutate the global variable as variable as immutable variable are not modifiable across scope.  however, you
    can read the variable from global scope.

"""

x = 10
def increment():
   # x=x+1  and x+=1 will not compile as x is in global scope and cannot be mutated in local scope. however we can read and print it
   # for x to be modified,  it must be declared in scope where its been modified.
    print(x)

increment()
# when we add () to increment object compiler will call it as increment.__call__().  it means all the logic of a function
# written in __call__ function.

"""
objects function behaviour can be describe in a better way with this example.
"""
class Printer:

    def __init__(self, s):
        self.str01 = s

    def __call__(self):
        # all the function logic will be in call function
         return self.str01.upper()


s1 = Printer('hello') # Defining object of class Printer
# Calling object s1
s2=s1()   # Hello
print(s2)
