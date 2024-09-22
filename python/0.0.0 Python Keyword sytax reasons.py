""""""
"""
0.   Python has blocks, namespace ,context and context manager.
     a context can has multiple scopes, especially when dealing with nested structures or multiple context managers.

1.  :    define the start of programming block.  in java this is done by { }
    in python : define the start of programming block.
    indentation level define the scope of the block
    end of indentation define end of this block.

for example:

if condition:
    # This is the start of the block
    print("Condition is true")
    # This is still part of the block
print("This is outside the block")  # Indentation level decreased, so this is outside the block

2.  in python empty block is represented by pass after colon.  the empty block starts with a : and then pass keyword
    if emptyp:
       pass.

3. Statement Separator
Semicolon (;): In Python, you can use a semicolon to separate multiple statements on a single line. For example
x = 10; y = 20; print(x + y)

4. Continuation Lines
Backslash (\): If you have a long statement that you want to split across multiple lines, you can use a backslash at
the end of a line to indicate that the statement continues on the next line. For example:
total = 1 + 2 + 3 + \
        4 + 5 + 6

Implicit Continuation: If you’re inside parentheses (), square brackets [], or curly braces {}, you don’t need a
backslash for continuation. For example:
total = (1 + 2 + 3 +
         4 + 5 + 6)

5. The as keyword in Python is used to create an alias or to bind a name to an object within a specific context,
   such as with modules, exceptions, and context managers. This is different from the = operator, which is used for
   general assignment.

   import numpy as np  # 'np' is an alias for 'numpy'  here the context of np is whole module.
   this cannot be done with

   import numpy
   np = numpy  # This is not the same as using 'as' in the import statement

Identifiers.
-------------
6. Allowed Characters
Identifiers can include letters (a-z, A-Z), digits (0-9), and underscores (_).
Identifiers must begin with a letter or an underscore.

7. Case Sensitivity
Names and identifiers are case sensitive. For example, Variable and variable are different identifiers.

8.Length of Identifiers
Identifiers can be of unlimited length.

9.Special Name Classes
Single Leading Underscore (_variable): Suggests a “private” method or variable name.
These are not imported when you use from module import *.
Single Trailing Underscore (variable_): Used to avoid conflicts with Python keywords (e.g., class_).
Double Leading Underscores (__variable): Used in class definitions to cause name mangling (weak hiding) private variable.
This is not often used.

10. Naming Conventions
Modules and Packages: Use all lower case (e.g., mymodule).
Globals and Constants: Use upper case (e.g., CONSTANT_VALUE).
Classes: Use CamelCase with an initial upper case letter (e.g., MyClass).
Methods and Functions: Use all lower case with words separated by underscores (e.g., my_function).
Local Variables: Use lower case with underscores between words (e.g., local_variable) or camelCase with an initial
lower case letter (e.g., localVariable), depending on your preference.
"""