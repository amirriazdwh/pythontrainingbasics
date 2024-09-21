''''
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