"""
with statement helps in simplifying some common resource management patterns by abstracting their functionally and
allowing them to be factored out and reused.

it is used to manage the safe acquistion and release of system resources.   resource are acquired by the with statement
and release when the execution leaves the with context.  since its an alternative form of try/catch statement and relies
on context to release.  its called context manager.

A good way to see this feature used effectively is looking at examples in the python standard library.  The build-in
open() function provides us with an excellent use case:
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Context manager allows specified actions to be performed at the beginning and end of with block. Two methods are responsible
for context manager:

__enter__(self) - indicates what should be done at the beginning of with block. Value that returns method is assigned
to variable after as.

__exit__(self, exc_type, exc_value, traceback) - indicates what should be done at the end of with block or when it
is interrupted. If there is an exception

within block, then exc_type, exc_value, traceback will contain exception information, if there is no exception
they will be equal to None.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
# opens the file for write and writes hello world
with open('D:\python_data\hello_file.txt', 'w') as f:
    f.write("hello world")

"""
#################################
What are Context Managers.
#################################
Any object that implements the __enter__ and __exit__ methods can be used as a context manager in Python. 
This allows you to use the with statement to manage resources efficiently and ensure proper cleanup.

Key Points:
__enter__ Method: This method is called when the execution flow enters the context of the with statement. 
It typically sets up the resource and returns it.

__exit__ Method: This method is called when the execution flow exits the context of the with statement.

It handles cleanup actions and can also manage exceptions.

Example: Custom Context Manager
#####################################
Here’s a simple example of a custom context manager:

class MyContextManager:
    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print(f"Exception caught: {exc_value}")
        print("Exiting the context")
        return True  # Suppress the exception

with MyContextManager() as manager:
    print("Inside the context")
    raise ValueError("An error occurred")
print("Program continues")


Explanation
__enter__ Method: Prints a message and returns the context manager object.
__exit__ Method: Prints a message, handles any exceptions, and optionally suppresses them by returning True.

########################################
Using Built-in Context Managers
########################################
Python provides several built-in context managers, such as for file handling:

with open('data.txt', 'r') as f:
    data = f.read()

In this case, the file object returned by open has __enter__ and __exit__ methods, making it a context manager.

Summary
Any object that implements the __enter__ and __exit__ methods can be used as a context manager,
 allowing you to use the with statement to manage resources efficiently and ensure proper cleanup.
"""

"""
when interpreter find with clause.   it generates the following code. 

# Pseudocode for the with statement
context_manager = ContextManager()  # Create the context manager object
value = context_manager.__enter__()  # Call __enter__ and get the value to be used in the block

try:
    # Execute the block of code within the context
    # If an exception occurs, it is caught and passed to __exit__
    # If no exception occurs, the block executes normally
    result = block_of_code(value)
except Exception as e:
    # If an exception occurs, __exit__ is called with exception details
    suppress = context_manager.__exit__(type(e), e, e.__traceback__)
    if not suppress:
        # If __exit__ returns False, re-raise the exception
        raise
else:
    # If no exception occurs, __exit__ is called with None
    context_manager.__exit__(None, None, None)
"""


"""
writing class is not the only way to support context managers. python provides a buildin package to do it.
this code is being implemented by decorator.

from contextlib import contextmanager

@contextmanager
def managed_context_file(name):
    try:
        f=open(name, 'w')
        yield f
    finally:
        f.close()
        
with managed_context_file("D:\python_data\hello_file.txt") as f:
    f.write("writing via context tag")
"""


"""
with open('D:\\python_data\\hello_file.txt', 'w') as fild:
    fild.write("hello world")

The with statement ensures that the file is properly opened and closed, even if an exception occurs.
 Here’s how the Python interpreter translates it:


fileobj = open('D:\\python_data\\hello_file.txt', 'w')  # Create the file object
try:
    fild = fileobj.__enter__()  # Call the __enter__ method
    fild.write("hello world")  # Execute the block of code
except Exception as e:
    # If an exception occurs, call the __exit__ method with exception details
    suppress = fileobj.__exit__(type(e), e, e.__traceback__)
    if not suppress:
        raise  # Re-raise the exception if __exit__ returns False
else:
    # If no exception occurs, call the __exit__ method with None
    fileobj.__exit__(None, None, None)


"""