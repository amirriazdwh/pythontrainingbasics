""""""
"""
Duck Typing
Concept: Duck typing is a type system where the type or class of an object is determined by its behavior 
(methods and properties) rather than its explicit inheritance.

Principle: “If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck.”
Usage: In Python, if an object implements the necessary methods and properties, it can be used in place of another object,
regardless of its actual type.

Dynamic Typing
Concept: Python is dynamically typed, meaning variable types are determined at runtime, not in advance.
Behavior: You can assign any type of value to a variable, and it can change type as the program executes.
Example:
Python

x = 10      # x is an integer
x = "hello" # now x is a string

Both concepts contribute to Python’s flexibility and ease of use, allowing for more adaptable and less rigid code structures.
"""


"""
In Python, the concept of abstract base classes (ABCs) and interfaces is a bit different from some other object-oriented 
languages like Java or C#. 

In Python, you can implement methods that conform to an interface without explicitly 
inheriting from an abstract base class. This is possible due to Python’s dynamic and duck-typed nature,
where an object’s suitability is determined by the presence of certain methods and properties, rather than 
the object’s inheritance hierarchy.

Example: Implementing Methods Without Extending an ABC
Let’s create a custom class that behaves like a sequence by implementing the necessary methods (__getitem__, __len__, 
and __contains__) without explicitly inheriting from the Sequence ABC.

"""
from collections.abc import Sequence

class MySequence:
    def __init__(self, data):
        self._data = data

    def __getitem__(self, index):
        return self._data[index]

    def __len__(self):
        return len(self._data)

    def __contains__(self, item):
        return item in self._data

# Create an instance of MySequence
my_seq = MySequence([1, 2, 3, 4, 5])

# Check if MySequence instance behaves like a sequence
print(isinstance(my_seq, Sequence))  # Output: True
print(len(my_seq))  # Output: 5
print(my_seq[2])  # Output: 3
print(3 in my_seq)  # Output: True

"""
Explanation:
MySequence Class: This class implements the methods __getitem__, __len__, and __contains__, which are required by
 the Sequence interface.
 
isinstance(my_seq, Sequence): This checks if my_seq is considered an instance of Sequence. The output is True because
MySequence implements the necessary methods defined by Sequence.

Key Points:
Duck Typing: In Python, if an object implements the methods required by an interface, it is considered to conform to
 that interface, regardless of its inheritance hierarchy.
 
Dynamic Typing: Python’s dynamic nature allows you to create classes that implement specific methods without
needing to inherit from a particular base class.
 
This example demonstrates how you can create a class that behaves like a sequence by implementing the required 
methods, without explicitly inheriting from the Sequence ABC. If you have any more questions or need further clarification, 
feel free to ask!
"""

"""
The methods like __eq__ (equality) and __ge__ (greater than or equal to) are special methods (also known as “dunder” methods) 
that belong to the base object class in Python. These methods can be overridden in any class to customize the behavior of
comparison operators.

"""
class MyClass:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if isinstance(other, MyClass):
            return self.value == other.value
        return False

    def __ge__(self, other):
        if isinstance(other, MyClass):
            return self.value >= other.value
        return False

# Create instances
a = MyClass(10)
b = MyClass(20)

# Comparison
print(a == b)  # Output: False
print(a >= b)  # Output: False
print(a <= b)  # Output: True

print(isinstance(a, MyClass))  # Output: True
print(isinstance(a, object))   # Output: True

"""
Benefits Over Multiple Inheritance
Simplifies Code: Duck typing allows you to focus on what an object can do (its behavior) rather than its place in
a class hierarchy. This reduces the need for complex inheritance structures.

Reduces Coupling: By relying on behavior rather than inheritance, duck typing reduces the coupling between classes. 
This makes your code more modular and easier to maintain.

Avoids Diamond Problem: Multiple inheritance can lead to the “diamond problem,” where a class inherits from two 
classes that both inherit from a common superclass. Duck typing sidesteps this issue by not relying on inheritance chains.

Example
Instead of creating a complex inheritance structure, you can use duck typing to ensure that objects can be used
 interchangeably based on their behavior:
"""

class FileWriter:
    def write(self, text):
        print(f"Writing to a file: {text}{self}")   # pycharm is suggesting that write may be static method as self was used in body

class NetworkWriter:
    def write(self, text):
        print(f"Sending over network: {text}")

def process(writer):
    writer.write("Hello, World!")

file_writer = FileWriter()
network_writer = NetworkWriter()

process(file_writer)  # Writing to a file: Hello, World!
process(network_writer)  # Sending over network: Hello, World!



class FileWriter:
    @staticmethod
    def write(text):
        print(f"Writing to a file: {text}")

class NetworkWriter:
    @staticmethod
    def write(text):
        print(f"Sending over network: {text}")

# Usage
FileWriter.write("Hello, World!")  # Writing to a file: Hello, World!
NetworkWriter.write("Hello, World!")  # Sending over network: Hello, World!
