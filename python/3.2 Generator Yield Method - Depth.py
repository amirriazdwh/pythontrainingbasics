"""
A function with yield, when called, returns a Generator.
Generators are iterators because they implement the iterator protocol, so you can iterate over them.
A generator can also be sent information, making it conceptually a coroutine.
In Python 3, you can delegate from one generator to another in both directions with yield from.
(Appendix critiques a couple of answers, including the top one, and discusses the use of return in a generator.)
Generators:
yield is only legal inside of a function definition, and the inclusion of yield in a function definition makes it return a generator.

The idea for generators comes from other languages (see footnote 1) with varying implementations. In Python's Generators, the execution
of the code is frozen at the point of the yield. When the generator is called (methods are discussed below) execution resumes and
 then freezes at the next yield.

yield provides an easy way of implementing the iterator protocol, defined by the following two methods: __iter__ and next (Python 2)
or __next__ (Python 3). Both of those methods make an object an iterator that you could type-check with the Iterator Abstract Base Class
from the collections module.

"""



def func():
    yield 'I am'
    yield 'a generator!'


type(func)                 # A function with yield is still a function
# <type 'function'>

gen = func()
type(gen)                  # but it returns a generator

# <type 'generator'>
hasattr(gen, '__iter__')   # that's an iterable
# True

hasattr(gen, 'next')       # and with .next (.__next__ in Python 3)
# True                           # implements the iterator protocol.

# The generator type is a sub-type of iterator:

import collections, types
issubclass(types.GeneratorType, collections.Iterator)
# True
# And if necessary, we can type-check like this:

isinstance(gen, types.GeneratorType)
# True
isinstance(gen, collections.Iterator)
# True

# A feature of an Iterator is that once exhausted, you can't reuse or reset it:

list(gen)
# ['I am', 'a generator!']
list(gen)
[]
# You'll have to make another if you want to use its functionality again (see footnote 2):

list(func())
# ['I am', 'a generator!']
# One can yield data programmatically, for example:

def func(an_iterable):
    for item in an_iterable:
        yield item
# The above simple generator is also equivalent to the below - as of Python 3.3 (and not available in Python 2), you can use yield from:

def func(an_iterable):
    yield from an_iterable
# However, yield from also allows for delegation to subgenerators, which will be explained in the following section
# on cooperative delegation with sub-coroutines.

# Coroutines:
# yield forms an expression that allows data to be sent into the generator (see footnote 3)

# Here is an example, take note of the received variable, which will point to the data that is sent to the generator:

def bank_account(deposited, interest_rate):
    while True:
        calculated_interest = interest_rate * deposited 
        received = yield calculated_interest
        if received:
            deposited += received


my_account = bank_account(1000, .05)
# First, we must queue up the generator with the builtin function, next. It will call the appropriate next or __next__ method, depending on the version of Python you are using:

first_year_interest = next(my_account)
# first_year_interest
# 50.0
# And now we can send data into the generator. (Sending None is the same as calling next.) :

next_year_interest = my_account.send(first_year_interest + 1000)
# next_year_interest
# 102.5
# Cooperative Delegation to Sub-Coroutine with yield from
# Now, recall that yield from is available in Python 3. This allows us to delegate coroutines to a subcoroutine:


def money_manager(expected_rate):
    # must receive deposited value from .send():
    under_management = yield                   # yield None to start.
    while True:
        try:
            additional_investment = yield expected_rate * under_management 
            if additional_investment:
                under_management += additional_investment
        except GeneratorExit:
            '''TODO: write function to send unclaimed funds to state'''
            raise
        finally:
            '''TODO: write function to mail tax info to client'''
        

def investment_account(deposited, manager):
    '''very simple model of an investment account that delegates to a manager'''
    # must queue up manager:
    next(manager)      # <- same as manager.send(None)
    # This is where we send the initial deposit to the manager:
    manager.send(deposited)
    try:
        yield from manager
    except GeneratorExit:
        return manager.close()  # delegate?

# And now we can delegate functionality to a sub-generator and it can be used by a generator just as above:

my_manager = money_manager(.06)
my_account = investment_account(1000, my_manager)
first_year_return = next(my_account) # -> 60.0
# Now simulate adding another 1,000 to the account plus the return on the account (60.0):

next_year_return = my_account.send(first_year_return + 1000)
# next_year_return # 123.6
# You can read more about the precise semantics of yield from in PEP 380.

# Other Methods: close and throw
# The close method raises GeneratorExit at the point the function execution was frozen. This will also be called by __del__ so you can put any cleanup code where you handle the GeneratorExit:

my_account.close()
# You can also throw an exception which can be handled in the generator or propagated back to the user:

import sys
try:
    raise ValueError
except:
    my_manager.throw(*sys.exc_info())

# Raises:
# Traceback (most recent call last):
#   File "<stdin>", line 4, in <module>
#   File "<stdin>", line 6, in money_manager
#   File "<stdin>", line 2, in <module>
# ValueError

"""
Conclusion
I believe I have covered all aspects of the following question:
What does the yield keyword do in Python?
It turns out that yield does a lot. I'm sure I could add even more thorough examples to this. If you want more or 
have some constructive criticism, let me know by commenting below.

"""

