""""""
"""
Construction of Python Program.
---------------------------------------
A python program generally contains 3 constructs. 
1. Keywords: Reserved words that have special meaning in Python, such as if, else, for, while, def, class, etc.
2. Expressions: Combinations of values, variables, operators, lambda function definition and function calls 
   that are evaluated to produce a value.
3. Statements: Instructions that the Python interpreter can execute. Examples include assignment statements, control flow  
   statements (like if, for, while), and function calls.
   
   Expression are single line piece of code however,  they can be made multiple lines by \ using explict continuation or
   with implicit continuation.  for example
   
   add = (lambda x, y: 
                    x + y)  #allowed. 
    
    add = lambda x, y: \
                    x + y   #allowed. 
                    
    add = lambda (x, y): x + y  is not allowed as syntax enforce it. 
    
    if (x >0 and y>0): 
        print("no negative value")  #allow as expression is inside bracket 
        
     if (x >0): 
        print("no negative value") #allow however since x>0 is single line expression so bracketless sytax is good
        
    try:
        # some code that may raise an exception
        pass
    except (TypeError, ValueError) as e:
        print("Error:", e)           #allowed. 
        
    try:
    # some code that may raise an exception
        pass
    except (TypeError) as e:
        print("Error:", e)      #allow.   however since TypeError is a single expression express bracketless syntax prefer. 

0.   Python has statement, blocks, context and context manager.
     there can be multiple statements in one block.
     there can be multiple blocks in one context. 

1.  : define the start of programming block. 
    in python : define the start of programming block.
    indentation level define the scope of the block
    end of indentation define end of this block.

    for example:
    if condition:
        # This is the start of the block
        print("Condition is true")
        # This is still part of the block
    print("This is outside the block")  # Indentation level decreased, so this is outside the block. 
    
2.  in python empty block is represented by pass after colon.  the empty block starts with a : and then pass keyword
    if emptyp:
       pass.

3. Statement Separator
    Semicolon (;): In Python, you can use a semicolon to separate multiple statements on a single line. For example
    x = 10; y = 20; print(x + y)

continuation. 
-------------
A python statement will on single line.  The only two ways to put statement on multiple lines is using \
and parentheses.  this is to note that.

lambda function are expression and single line statement. so lambda (x,y): x+y is not allowed as it makes 
it multiline.  so to make it multiline we have to use \ or (). 


4. Continuation Lines
    Backslash (\): If you have a long statement that you want to split across multiple lines, you can use a backslash at
    the end of a line to indicate that the statement continues on the next line. For example:
    total = 1 + 2 + 3 + \
        4 + 5 + 6

5. Implicit Continuation: If you’re inside parentheses (), square brackets [], or curly braces {}, you don’t need a
    backslash for continuation. For example:
    total = (1 + 2 + 3 +
            4 + 5 + 6)
    The objective of using parentheses (), square brackets [], or curly braces {} for implicit continuation is to make
     the code more readable and avoid the need for a backslash \ for line continuation.  in python lambda function is 
     single line expression so  lambda (x, y): x+y  is not allow.  as presence of () make it multiline statement which
     against the python lambda rule

5. The as keyword in Python is used to create an alias or to bind a name to an object within a specific context,
   such as with modules, exceptions, and context managers. This is different from the = operator, which is used for
   general assignment.

   import numpy as np  # 'np' is an alias for 'numpy'  here the context of np is whole module.
   this cannot be done with

   import numpy
   np = numpy  # This is not the same as using 'as' in the import statement


"""