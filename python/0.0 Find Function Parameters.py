# explicit function
def fun(a, b):
    return a ** b


# import required modules
import inspect

# use signature()
print(inspect.signature(fun))