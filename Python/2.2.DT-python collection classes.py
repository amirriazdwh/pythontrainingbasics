""""""

"""
the collections module provides specialized container datatypes that offer alternatives to Python’s general-purpose built-in 
containers like dict, list, set, and tuple. These specialized containers are designed to provide additional functionality 
and efficiency for specific use cases

Key Classes in the collections Module:
namedtuple: Factory function for creating tuple subclasses with named fields

from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)  # Output: 1 2

deque: List-like container with fast appends and pops on either end.

from collections import deque
d = deque([1, 2, 3])
d.append(4)
d.appendleft(0)
print(d)  # Output: deque([0, 1, 2, 3, 4])

Counter: Dict subclass for counting hashable objects.

from collections import Counter
c = Counter('abracadabra')
print(c)  # Output: Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})

OrderedDict: Dict subclass that remembers the order entries were added.

from collections import OrderedDict
od = OrderedDict()
od['a'] = 1
od['b'] = 2
print(od)  # Output: OrderedDict([('a', 1), ('b', 2)])

defaultdict: Dict subclass that calls a factory function to supply missing values.
from collections import defaultdict
dd = defaultdict(int)
dd['a'] += 1
print(dd)  # Output: defaultdict(<class 'int'>, {'a': 1})

ChainMap: Dict-like class for creating a single view of multiple mappings.
from collections import ChainMap
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
cm = ChainMap(dict1, dict2)
print(cm)  # Output: ChainMap({'a': 1, 'b': 2}, {'b': 3, 'c': 4})

UserDict, UserList, UserString: Wrappers around dictionary, list, and string objects for easier subclassing.
from collections import UserDict
class MyDict(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value * 2)

d = MyDict()
d['a'] = 3
print(d)  # Output: {'a': 6}


Purpose of the collections Module:
The collections module is designed to provide additional data structures that are not available with the built-in types. 
These structures can help improve the efficiency and readability of your code, especially for specific tasks like
 counting elements, maintaining order, or creating custom container types12.

If you have any specific questions about any of these classes or need further examples, feel free to ask!

"""