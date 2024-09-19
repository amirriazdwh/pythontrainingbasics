"""
In Python, the import and from ... import statements are used to include code from one module into another
. Here’s a breakdown of how they work and their differences:

import math
print(math.sqrt(16))  # Output: 4.0

Usage: You need to prefix the module name (math) to access its functions or variables.
Scope: Imports the entire module, making all its functions and variables available.

from math import sqrt
print(sqrt(16))  # Output: 4.0

Usage: You can directly use the imported function (sqrt) without prefixing it with the module name.
Scope: Imports only the specified functions, classes, or variables, not the entire module.


from ... import *: Imports all public names from a module.
Namespace Pollution: Can lead to name conflicts and harder-to-read code.
__all__ Attribute: Controls what gets imported with import *.

# math_utils.py
__all__ = ['PI', 'add']

PI = 3.14159

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def _private_function():
    pass


from math_utils import *

print(PI)          # Output: 3.14159
print(add(2, 3))   # Output: 5
# print(subtract(5, 2))  # This will raise an error


Example with Filtering
If you want to import specific functions or classes based on a condition, you can use a combination of from ... import and
 conditional logic. However, the import itself doesn’t support filtering directly. Here’s an example:

# Conditional import based on a condition
if some_condition:
    from math import sqrt
else:
    from math import pow

# Use the imported function
if some_condition:
    print(sqrt(16))  # Output: 4.0
else:
    print(pow(2, 4))  # Output: 16.0


"""


