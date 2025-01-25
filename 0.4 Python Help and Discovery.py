#  find the memory address of the a variable

a =25
print(hex(id(a)))

#-------------------------------------------------
# explicit function
def fun(a, b):
    return a ** b

fun.__dict__


#---------------------------------------------------
#  Find a method signature
#---------------------------------------------------
# import required modules
import inspect

# use signature()
print(inspect.signature(fun))

# use signature()
print(inspect.signature(super.__init__))
print(inspect.signature(super.__new__))
print(inspect.signature(super.__getattribute__))

#----------------------------------------------------------
#  Find builtin module
#-----------------------------------------------------------
import sys
a = sys.builtin_module_names
for x in a:
    print(x)

#--------------------------------------------------------------
# help for building objects and data types
help(list)

#help on custom functions
help(fun)
help (str)
help(sys.argv)
help('modules')
help('keywords')
help('symbols')
#------------------------------
help('topics')

"""
to any further help type,   LOOPING, which is a topic where got by typeing help(topics)
to get any futher help types ,   glob which is a module we got by type help(modules)
"""


dir(__builtin__)

# to clear python interprete screen type
print("\033[H\033[J", end="")