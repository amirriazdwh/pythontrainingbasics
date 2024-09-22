"""
###############################################
-Internal Exception Handling Mechanism
##############################################
-Compilation and Bytecode:
When you run a Python script, the interpreter compiles the source code into bytecode. This bytecode is a low-level
representation of your code that the Python virtual machine (PVM) can execute.
During this compilation phase, the interpreter also identifies try and except blocks and prepares to handle exceptions.

-Execution and Exception Raising:
As the bytecode executes, if an error occurs (e.g., division by zero), the interpreter raises an exception.
This raising of an exception can be thought of as an “interrupt” that changes the normal flow of execution.
it transfer control from program to python interpreter which is over python virtual machine.
python interpreter maintains a list of exception it list at the compile time.
the interpreter compare the exception with the list of exception and find its exception handling functions

-Stack Unwinding:
The interpreter starts unwinding the call stack, looking for an appropriate exception handler.
Each function call is represented by a frame in the stack. The interpreter checks each frame for a try block that
can handle the exception.  each block has a list of exception.  if intrepter unwind 3 black as it does find
any exception handling list which matches with raised exception but find the exception in block 4.  after handling exception
it will transfer control to block 4 and code start executing at block 4

-Finding the Handler:
The interpreter maintains a list of active exception handlers, which are essentially the except blocks defined in the code.
It searches this list to find a matching handler for the raised exception.
e.g except Exception as m:
the raise exception type is compare with exception type in except block and exception handling function is discovered.

-Executing the Handler:
Once a matching except block is found, the interpreter transfers control to that block.
The except block executes, handling the exception.

-Uncaught Exceptions:
If no matching except block is found, the interpreter continues unwinding the stack until it reaches the top level of the program.
If the exception remains unhandled, the interpreter prints a traceback and terminates the program.
-----------------------------------------------------
"""

"""
########################
-Raising SystemExit:
#########################
When sys.exit() is called, it raises a SystemExit exception.
This exception can be caught and handled like any other exception using a try-except block.
+-
-Uncaught SystemExit:
If the SystemExit exception is not caught by any try-except block in the program, it propagates up the call stack.
Eventually, it reaches the top level of the program, where the Python interpreter catches it.

-Interpreter Handling:
When the interpreter catches the SystemExit exception, it performs cleanup operations and terminates the program.
The exit status code provided to sys.exit() (or the default code 0 if none is provided) is returned to the operating system.
"""

"""

####################################
Python Exception Handling code 
####################################

Method #1
-----------
 except Exception as e:
        raise Exception(sys._getframe(0).f_code.co_name + ' : ' + __name__ + ' : Line ' + str(
            sys.exc_info()[-1].tb_lineno) + ' : ' + str(e))


import sys

def faulty_function():
    try:
        1 / 0  # This will raise a ZeroDivisionError
    except Exception as e:
        raise Exception(sys._getframe(0).f_code.co_name + ' : ' + __name__ + ' : Line ' + str(
            sys.exc_info()[-1].tb_lineno) + ' : ' + str(e))

if __name__ == "__main__":
    try:
        faulty_function()
    except Exception as e:
        print(e)

result:
faulty_function : __main__ : Line 6 : division by zero
"""

"""
Method #2.
-----------
import sys
import traceback

def functionC():
    raise ValueError("An error occurred in functionC")

def functionB():
    functionC()

def functionA():
    functionB()

def main():
    try:
        functionA()
    except Exception as e:
        stack_trace = traceback.format_exc()
        current_function = sys._getframe(0).f_code.co_name
        module_name = __name__
        line_number = sys.exc_info()[-1].tb_lineno
        error_message = f"{current_function} : {module_name} : Line {line_number} : {str(e)}"
        print(f"Error Message: {error_message}\nStack Trace:\n{stack_trace}")

if __name__ == "__main__":
    main()

Result:
Error Message: main : __main__ : Line 20 : An error occurred in functionC
Stack Trace:
Traceback (most recent call last):
  File "example.py", line 18, in main
    functionA()
  File "example.py", line 12, in functionA
    functionB()
  File "example.py", line 9, in functionB
    functionC()
  File "example.py", line 6, in functionC
    raise ValueError("An error occurred in functionC")
ValueError: An error occurred in functionC
"""

"""
Method 3
-----------------
import sys
import traceback

def functionC():
    raise ValueError("An error occurred in functionC")

def functionB():
    functionC()

def functionA():
    functionB()

def main():
    try:
        functionA()
    except Exception as e:
        # Capture the stack trace
        stack_trace = traceback.format_exc()
        
        # Get the current function name
        current_function = sys._getframe(0).f_code.co_name
        
        # Get the module name
        module_name = __name__
        
        # Get the line number where the exception occurred
        line_number = sys.exc_info()[-1].tb_lineno
        
        # Construct the error message
        error_message = (
            f"Exception occurred in function '{current_function}' "
            f"in module '{module_name}' at line {line_number}:\n"
            f"{str(e)}\n\n"
            f"Stack Trace:\n{stack_trace}"
        )
        
        # Print or log the error message
        print(error_message)

if __name__ == "__main__":
    main()

Resut:
Exception occurred in function 'main' in module '__main__' at line 20:
An error occurred in functionC

Stack Trace:
Traceback (most recent call last):
  File "example.py", line 18, in main
    functionA()
  File "example.py", line 12, in functionA
    functionB()
  File "example.py", line 9, in functionB
    functionC()
  File "example.py", line 6, in functionC
    raise ValueError("An error occurred in functionC")
ValueError: An error occurred in functionC


import traceback

try:
    1 / 0
except Exception:
    print traceback.format_exc()
"""


'''
to see the exception heiracy see the following link
https://docs.python.org/3/library/exceptions.html#exception-hierarchy

example is for OS related activity is as under:
+-- OSError
|    +-- BlockingIOError
|    +-- ChildProcessError
|    +-- ConnectionError
|    |    +-- BrokenPipeError
|    |    +-- ConnectionAbortedError
|    |    +-- ConnectionRefusedError
|    |    +-- ConnectionResetError
|    +-- FileExistsError
|    +-- FileNotFoundError
|    +-- InterruptedError
|    +-- IsADirectoryError
|    +-- NotADirectoryError
|    +-- PermissionError
|    +-- ProcessLookupError
|    +-- TimeoutError
'''

import traceback

try:
    raise TypeError("Oups!")
except Exception as err:
    try:
        print(err)
        raise TypeError("Again !?!")
    except:
        raise TypeError("Oups Second!")
    finally:
        traceback.print_exc()