"""
with statement helps in simplifying some common resource management patterns by abstracting their functionally and
allowing them to be factored out and reused.

it is used to manage the safe acquistion and release of system resources.   resource are acquired by the with statement
and release when the execution leaves the with context.  since its an alternative form of try/catch statement and relies
on context to release.  its called context manager.

A good way to see this feature used effectively is looking at examples in the python standard library.  The build-in
open() function provides us with an excellent use case:

"""
# opens the file for write and writes hello world
with open('D:\python_data\hello_file.txt', 'w') as f:
    f.write("hello world")

"""
with clause creates an With object and open function is passed to With object therefore creating a decorator 
with clause has standard call to __enter__ and __exit__ and all the code after "as f :" comes inside the body of decorator
to create a wraper or extended function "write"

def With (open('D:\python_data\hello_file.txt', 'w'): 
    f = fnc.__enter()__
    f.write ("hello world")
    f.__exit__()

"""

"""
opening the files using the with stateemnt is generally recommended because it ensure that open file descriptor is close
automatically after program execution leaves the context of the with statement.  Internally ,  the above code sample 
translate to:
"""

f=open("D:\python_data\hello_file.txt","w")
try:
    f.write("hello world from exception loop")
finally:
    f.close()


"""
without the try and finally clause the implementation dont gurantee that file will close.  therefore you have to either 
use try and finally or with statement.   

def get_all_songs():
    with sqlite3.connect('db/songs.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM songs ORDER BY id desc")
        all_songs = cursor.fetchall()
        return all_songs

"""

"""
you can use with clase with your own objects.  this is being implement by context manager.  its simple set of methods which
take care of resource management.   all we need to all is __enter__ and __exist__
"""

class ManagedFile:
    def __init__(self,name):
        self.name=name

    def __enter__(self):
        self.file= open(self.name, 'w')
        return self.file                  # if you dont specify return the function returns none


    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()



with ManagedFile('D:\python_data\hello_file.txt') as f:
    f.write("hello from objects")


#here is how it execute with in With clause object.  With has standard calls to __enter()__ and __exit__ in decorator
# def with ( f) :
f =  ManagedFile('D:\python_data\hello_file.txt').__enter__()
f.write("hello from object decoding")   # as a decorator extension,  this code is being add in decorator method.
f.__exit__()                            # when all the extended functions are being executed __exit()__ is add



"""
writing class is not the only way to support context managers. python provides a buildin package to do it.
"""

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
 to udnerstand the above example a knowledge of decorator and generators is required. 
"""