
"""
__name__ is a boilerplate code that protects users from accidentally invoking the script when they didn't intend to run in that name space
Here are some common problems when the guard is omitted from a script:

1.  If you import the guardless script in another script (e.g. import my_script_without_a_name_eq_main_guard),
then the second script will trigger the first to run at import time and using the second script's command line
arguments. This is almost always a mistake.

2.  f you have a custom class in the guardless script and save it to a pickle file, then unpickling it in another script
will trigger an import of the guardless script, with the same problems outlined in the previous bullet.

Long Answer
To better understand why and how this matters, we need to take a step back to understand how Python initializes
scripts and how this interacts with its module import mechanism.

Whenever the Python interpreter reads a source file, it does two things:
1.  it sets a few special variables like __name__, and then
2. it executes all of the code found in the file.

Let's see how this works and how it relates to your question about the __name__ checks we always see in Python scripts.

Code Sample
Let's use a slightly different code sample to explore how imports and scripts work. Suppose the following is in a file
called foo.py.

"""
# Suppose this is foo.py.
print("before import")
import math

print("before functionA")
def functionA():
    print("Function A")

print("before functionB")
def functionB():
    print("Function B {}".format(math.sqrt(100)))

print("before __name__ guard")
if __name__ == '__main__':
    functionA()
    functionB()
print("after __name__ guard")
# foo.py end here
"""
----------------
Note
----------------
Special Variables
When the Python interpreter reads a source file, it first defines a few special variables. In this case, 
we care about the __name__ variable.

When Your Module Is the Main Program

If you are running your module (the source file) as the main program, e.g.

python foo.py

the interpreter will assign the hard-coded string "__main__" to the __name__ variable, i.e.
"""

# as the interpreter inserts this at the top of your module when run as the main program.
__name__ = "__main__"
"""
suppose some other module is the main program and it imports your module. This means  that  __name__ code part defined in foo.py is still there
 and it should not execute.  only the main of other module importing foo module should execute

 import foo   the foo is imported in some other module

The interpreter will search for your foo.py file (along with searching for a few other variants), and prior to
# executing that module, it will assign the name "foo" from the import statement to the __name__ variable, i.e.

 It's as if the interpreter inserts this at the top of your module when it's imported from another module.
"""
__name__ = "foo"
"""
Executing the Module's Code
After the special variables are set up, the interpreter executes all the code in the module, one statement at a time. 
You may want to open another window on the side with the code sample so you can follow along with this explanation.

 Always
 
It prints the string "before import" (without quotes).
It loads the math module and assigns it to a variable called math. This is equivalent to replacing import math with 
the following (note that __import__ is a low-level function in Python that takes a string and triggers the actual import):
"""

# Find and load a module given its string name, "math",
# then assign it to a local variable called math.
math = __import__("math")

"""
It prints the string "before functionA".
It executes the def block, creating a function object, then assigning that function object to a variable called functionA.
It prints the string "before functionB".
It executes the second def block, creating another function object, then assigning it to a variable called functionB.
It prints the string "before __name__ guard".
Only When Your Module Is the Main Program
If your module is the main program, then it will see that __name__ was indeed set to "__main__" and it calls the two 
functions, printing the strings "Function A" and "Function B 10.0".
Only When Your Module Is Imported by Another

(instead) If your module is not the main program but was imported by another one, then __name__ will be "foo",
 not "__main__", and it'll skip the body of the if statement.
Always

It will print the string "after __name__ guard" in both situations

Summary
In summary, here's what'd be printed in the two cases:
# What gets printed if foo is the main program
before import
before functionA
before functionB
before __name__ guard
Function A
Function B 10.0
after __name__ guard
# What gets printed if foo is imported as a regular module
before import
before functionA
before functionB
before __name__ guard
after __name__ guard
Why Does It Work This Way?
You might naturally wonder why anybody would want this. Well, sometimes you want to write a .py file that can be both
 used by other programs and/or modules as a module, and can also be run as the main program itself. Examples:

Your module is a library, but you want to have a script mode where it runs some unit tests or a demo.

Your module is only used as a main program, but it has some unit tests, and the testing framework works by importing .py 
files like your script and running special test functions. You don't want it to try running the script just because 
it's importing the module.

Your module is mostly used as a main program, but it also provides a programmer-friendly API for advanced users.

Beyond those examples, it's elegant that running a script in Python is just setting up a few magic variables and 
importing the script. "Running" the script is a side effect of importing the script's module.
"""
#
# Food for Thought
# Question: Can I have multiple __name__ checking blocks? Answer: it's strange to do so, but the language won't stop you.
#
# Suppose the following is in foo2.py. What happens if you say python foo2.py on the command-line? Why?

# Suppose this is foo2.py.
import os, sys; sys.path.insert(0, os.path.dirname(__file__)) # needed for some interpreters

def functionA():
    print("a1")
    # from foo2 import functionB
    print("a2")
    functionB()
    print("a3")

def functionB():
    print("b")

print("t1")
if __name__ == "__main__":
    print("m1")
    functionA()
    print("m2")
print("t2")
      
# Now, figure out what will happen if you remove the __name__ check in foo3.py:
# Suppose this is foo3.py.
import os, sys; sys.path.insert(0, os.path.dirname(__file__)) # needed for some interpreters

def functionA():
    print("a1")
    # from foo3 import functionB
    print("a2")
    functionB()
    print("a3")

def functionB():
    print("b")

print("t1")
print("m1")
functionA()
print("m2")
print("t2")
# What will this do when used as a script? When imported as a module?
# Suppose this is in foo4.py
__name__ = "__main__"

def bar():
    print("bar")

"""
# all the objects in python has name guards to protect themselves from running in module.   for example 
"""
print("before __name__ guard")
if __name__ == "__main__":
    bar()
print("after __name__ guard")

# Share
# Improve this answer
# Follow
# edited Apr 5 at 21:28
# answered Jan 7 '09 at 4:26

