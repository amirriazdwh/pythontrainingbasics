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


"""