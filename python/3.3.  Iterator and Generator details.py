
"""
In summary: Iterators are objects that have an __iter__ and a __next__ (next in Python 2) method.
Generators provide an easy, built-in way to create instances of Iterators.
A function with yield in it is still a function, that, when called, returns an instance of a generator object:

"""

def a_function():
    "when called, returns generator object"
    yield
#A generator expression also returns a generator:

a_generator = (i for i in range(0))
#For a more in-depth exposition and examples, keep reading.

"""
A Generator is an Iterator
Specifically, generator is a subtype of iterator.
"""
import collections, types
issubclass(types.GeneratorType, collections.Iterator)

#True
#
# We can create a generator several ways. A very common and simple way to do so is with a function.
# Specifically, a function with yield in it is a function, that, when called, returns a generator:

def a_function():
        "just a function definition with yield in it"
        yield

type(a_function)
# <class 'function'>

a_generator = a_function()  # when called
type(a_generator)           # returns a generator
# <class 'generator'>
# And a generator, again, is an Iterator:

isinstance(a_generator, collections.Iterator)

# True
# An Iterator is an Iterable
# An Iterator is an Iterable,

issubclass(collections.Iterator, collections.Iterable)
# True
# which requires an __iter__ method that returns an Iterator:

collections.Iterable()
# Traceback (most recent call last):
#   File "<pyshell#79>", line 1, in <module>
#     collections.Iterable()
# TypeError: Can't instantiate abstract class Iterable with abstract methods __iter__
# Some examples of iterables are the built-in tuples, lists, dictionaries, sets, frozen sets, strings, byte strings, byte arrays,
# ranges and memoryviews:

all(isinstance(element, collections.Iterable) for element in (
        (), [], {}, set(), frozenset(), '', b'', bytearray(), range(0), memoryview(b'')))
# True
# Iterators require a next or __next__ method
# In Python 2:

collections.Iterator()
# Traceback (most recent call last):
#   File "<pyshell#80>", line 1, in <module>
#     collections.Iterator()
# TypeError: Can't instantiate abstract class Iterator with abstract methods next
# And in Python 3:

collections.Iterator()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: Can't instantiate abstract class Iterator with abstract methods __next__
# We can get the iterators from the built-in objects (or custom objects) with the iter function:

all(isinstance(iter(element), collections.Iterator) for element in (
        (), [], {}, set(), frozenset(), '', b'', bytearray(), range(0), memoryview(b'')))
# True

# The __iter__ method is called when you attempt to use an object with a for-loop. Then the __next__ method
# is called on the iterator object to get each item out for the loop. The iterator raises StopIteration when
# you have exhausted it, and it cannot be reused at that point.
#
# From the documentation
# From the Generator Types section of the Iterator Types section of the Built-in Types documentation:
#
# Python’s generators provide a convenient way to implement the iterator protocol. If a container object’s __iter__() method
# is implemented as a generator, it will automatically return an iterator object (technically, a generator object)
# supplying the __iter__() and next() [__next__() in Python 3] methods. More information about generators can be found
# in the documentation for the yield expression.

# (Emphasis added.)
#
# So from this we learn that Generators are a (convenient) type of Iterator.
#
# Example Iterator Objects
# You might create object that implements the Iterator protocol by creating or extending your own object.

class Yes(collections.Iterator):

    def __init__(self, stop):
        self.x = 0
        self.stop = stop

    def __iter__(self):
        return self

    def next(self):
        if self.x < self.stop:
            self.x += 1
            return 'yes'
        else:
            # Iterators must raise when done, else considered broken
            raise StopIteration

    __next__ = next # Python 3 compatibility

# But it's easier to simply use a Generator to do this:

def yes(stop):
    for _ in range(stop):
        yield 'yes'

# Or perhaps simpler, a Generator Expression (works similarly to list comprehensions):

stop = 4
yes_expr = ('yes' for _ in range(stop))

# They can all be used in the same way:

#for i, y1, y2, y3 in zip(range(stop), Yes(stop), yes(stop), ('yes' for _ in range(stop))):
#print('{0}: {1} == {2} == {3}'.format(i, y1, y2, y3))


# 0: yes == yes == yes
# 1: yes == yes == yes
# 2: yes == yes == yes
# 3: yes == yes == yes
# Conclusion
# You can use the Iterator protocol directly when you need to extend a Python object as an object that can be iterated over.
#
# However, in the vast majority of cases, you are best suited to use yield to define a function that returns a Generator Iterator or consider Generator Expressions.
#
# Finally, note that generators provide even more functionality as coroutines. I explain Generators, along with the yield statement, in depth on my answer to "What does the “yield” keyword do?".
