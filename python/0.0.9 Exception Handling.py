''''''
"""
-Raising SystemExit:
When sys.exit() is called, it raises a SystemExit exception.
This exception can be caught and handled like any other exception using a try-except block.
+-
-Uncaught SystemExit:
If the SystemExit exception is not caught by any try-except block in the program, it propagates up the call stack.
Eventually, it reaches the top level of the program, where the Python interpreter catches it.

-Interpreter Handling:
When the interpreter catches the SystemExit exception, it performs cleanup operations and terminates the program.
The exit status code provided to sys.exit() (or the default code 0 if none is provided) is returned to the operating system.

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

faulty_function : __main__ : Line 6 : division by zero
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