"""
There are three types of sequence.
1. ITERATOR
2. Generator
3. Enumerator ( a special type of iterator)
"""
"""
WHAT IS ITERATOR
-----------------
iterable  --  is a object in which either contains __iter__() or __getitem__() object is defined.  we can get iterator object by running them
          --  you can get iterator by running iter or getitem method also.  __iter__() always return self
iterator  --  is an object in which __next__ method is defined.  they can be called by __next__() or by next function. at the end of each iterator
          -- # when the function terminates, StopIteration exception is raised. __next__(self) take self as object and return values of object
iteration -- ability to iterate is called iteration.   for example for loop. a for loop get iterator by running iter method and then run next
          -- method to get the next values.  the loop terminates when the StopIteration exception is being raised in iterator next method
          -- in iteratoble objects all the values are generated in memory.  therefore iterable objects consume a lot of memory
          -- in case Stopiteration exception is not raised,  the loop will continue and give None as values
"""
"""
WHAT ARE GNERATORS
Yield      --  yield is called from a function,  it converts the values into a object and return an generator.  when the yield function is 
           -- being called on a values,  that value is stored in stack or heap as object and function processing stops and control is switched 
           -- caller function or loop
Generators -- are iterators are objects which contains __next_ method. the values of which are returned by next objects.  
iternation --  iteration is any for loop which takes iterator and triversed over a loop.  it end when StopIteration exception is being raised
         --    Once the function yields, the function is paused and the control is transferred to the caller.
          --  # Local variables and their states are remembered between successive calls.
         --   xrange is a generator function.  
         --  a generator generates the values on the fly and therefore values can be traversed only once.
"""

"""
WHAT ARE ENUMERATOR
an enumberator is an object of a class which takes a sequence and retruns the an iterator.  its an iterator as it contains _iter_()
and _next_() function
Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object. This enumerate object can then be 
used directly in for loops or be converted into a list of tuples using list() method.

"""

nums = [x * x for x in [1, 2, 3, 4, 5, 6, 7, 8]]
print(nums)

# this is a generator expression,  my_nums is a generator object
my_nums = (x * x for x in [1, 2, 3, 4, 5, 6, 7, 8])

# Generator expression returns a generator object which contain next method
# list object takes generator object and use next method to load data into list
print(list(my_nums))

my_num01 = (x * x for x in [1, 2, 3, 4, 5, 6, 7, 8])

# here casting the done automatically as for loop takes sequence object
for x in my_num01:
    print(x)


# execution stops at each yield procedure
# point to be noted here that yield object contains a next procedure
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


print("___________________________________")
genObj = my_gen()
print(type(genObj))
print(next(genObj))


######################################################################
def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1, -1, -1):
        yield my_str[i]


# here method returns a yield object by function
for char in rev_str("hello"):
    print(char)


##########################################################################

class PrintNumber:
    def __init__(self, max):
        self.max = max

    # an iter always return self
    def __iter__(self):
        self.num = 0
        return self

    # a next always return self.value
    def __next__(self):
        if (self.num >= self.max):
            raise StopIteration
        self.num += 1
        return self.num


printNum = PrintNumber(3)
# this call the _iter_ procedure in class and declare and initialize
# variable which we have to use in __next_

print("_______________Start____________________")
# printNumIter = iter(printNum)
# print(printNumIter)
print("___________________________________")
# print(next(printNumIter))
for x in printNum:
    print(x)
print("________________stop___________________")


###################################################
#   yield in class
###################################################
class TestNum:
    def __init__(self, max):
        self.max = max
        self.num = 0

    # with yield the iteration procedure is implemented and _next_ is ignored.
    # the next method you dont have to implement,  it come with object returned
    # by yield
    def __iter__(self):
        print(self.num)
        if (self.num >= self.max):
            raise StopIteration
        self.num += 1
        yield self.num


# def __next__(self):
#        print(self.num)
#        if(self.num >= self.max):
#            raise StopIteration
#        self.num += 1
#        yield self.num

fib = TestNum(3)
print("###################################")
for i in fib:
    print(i)
print("###################################")


class IterableContainer:
    def __init__(self, data=(1, 2, 3, 4, 5)):
        self.data = data

    def __iter__(self):
        for x in self.data:
            yield x


itobj = IterableContainer()
for i in itobj:
    print(i)


##############################################
# Pipleline Generators
###############################################

# Generators can be used to pipeline a series of operations. This is best illustrated
#  using an example.
# Suppose we have a log file from a famous fast food chain. The log file has a
#  column (4th column) that keeps track of the number of pizza sold every hour and we want to sum it to find the total pizzas sold in 5 years.
# Assume everything is in string and numbers that are not available are marked as
#  'N/A'. A generator implementation of this could be as follows.

# with open('sells.log') as file:
#    pizza_col = (line[3] for line in file)
#    per_hour = (int(x) for x in pizza_col if x != 'N/A')
#    print("Total pizzas sold = ",sum(per_hour))

def double_inputs():
    while True:
        x = yield
        yield x * 2


gen = double_inputs()
next(gen)  # run up to the first yield
gen.send(10)  # goes into 'x' variable


# next(gen)       # run up to the next yield
# gen.send(6)     # goes into 'x' again

# next(gen)       # run up to the next yield
# gen.send(94.3)  # goes into 'x' again


class Enum(set):
    def __getattr__(self, name):
        if name in self:
            return name
        raise AttributeError


Animals = Enum(["DOG", "CAT", "HORSE"])
print(Animals.DOG)


class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)


# Example
if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)

for ch in root:
    print(ch)


# Outputs Node(1), Node(2)

def squares(start, stop):
    for i in range(start, stop):
        yield i * i


x1 = [x for x in squares(1, 10)]

myls = [1, 2, 3, 4, 5, 6]
print(myls)

print(x1)


def multi_yield():
    yield_str = "This will print the first string"
    yield yield_str
    yield_str = "This will print the second string"
    yield yield_str


multi_obj = multi_yield()
print(next(multi_obj))
print(next(multi_obj))
print(next(multi_obj))



# Python program to illustrate
# enumerate object adds an index to sequence by position
l1 = ["eat", "sleep", "repeat"]
s1 = "geek"

# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)

#here object type is enumberator which is an iterator.
# therefore this object can be converted to tuple,list, dictionary etc
print("Return type:", type(obj1))
print(list(enumerate(l1)))

# changing start index to 2 from 0
print(list(enumerate(s1, 2)))
