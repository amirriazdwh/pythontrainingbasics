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
4.  function default variables are created in static scope
5.  since a function is an object,  it can be passed to another function which is another object
6.  since a function is an object   its object reference can be assigned to a variable.
7.  a function when assigned to a variable has reference to function object and this function variable to function
object
    has a mapping is store in high scope dictionary.  since function is a object it can be delete as del
    function_variable
8.  in python all the variable must be initialized before any operation like addition or subtraction should be done.
    if the variable initialization is global scope and addition operation in function has local scope then function
    will not
    able to mutate the global variable. for a variable to be modified in funcitons's local scope,  the function must
    be declared
    in local scope,  for a variable to be modified in global scope the variable must be define global scope.
9.  if we have a function lets say  fnc_sort.  it will only execute once we add () means fnc_sort().  doing so call the
    fnc_sort.__call__()  function behind the scenes

"""

"""
NOTE:

functions are objects with a dunder function __default__ this is when the default arguments are being declared. 
and the calling function does not give any values.  in this case when def statement is reached.  the function object
is created and __default__ function is executed.   the default variables are created in static scope of the function and
__default__ function is also static.  this means variables are bring shared across multiple objects.   

therefore , default variable  in __defalut__ functions must be immutable. 
"""

x = 10


def increment ( ) :
    # x=x+1  and x+=1 will not compile as x is in global scope and cannot be mutated in local scope. however we can
    # read and print it
    # for x to be modified,  it must be declared in scope where its been modified.
    print ( x )


increment ( )
# when we add () to increment object compiler will call it as increment.__call__().  it means all the logic of a
# function
# written in __call__ function.

"""
objects function behaviour can be describe in a better way with this example.
"""


class Printer :

    def __init__ ( self , s ) :
        self.str01 = s

    def __call__ ( self ) :
        # all the function logic will be in call function
        return self.str01.upper ( )


s1 = Printer ( 'hello' )  # Defining object of class Printer
# Calling object s1
s2 = s1 ( )  # Hello
print ( s2 )

## wrong implementations.
"""
functions are objects with a dunder function __default__ this is when the default arguments are being declared. 
and the calling function does not give any values.  in this case when def statement is reached.  the function object
is created and __default__ function is executed.   the default variables are created in static scope of the function and
__default__ function is also static.  this means variables are bring shared across multiple objects.   

therefore , default variable  in __defalut__ functions must be immutable. 
"""


def add_two_to_list ( my_list = [ ] ) :
    my_list.append ( 2 )
    return my_list


print ( add_two_to_list.__defaults__ )  # ([],)
add_two_to_list ( )
print ( add_two_to_list.__defaults__ )  # ([2],)
print ( globals ( ) )


def default_fn ( a = 2 , b = 3 ) :
    print ( a , b )


print ( default_fn.__defaults__ )
