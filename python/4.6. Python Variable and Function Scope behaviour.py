"""
Note:
    1. in python all variable types are objects.
    2. variable types are store in object not in variable
    3. variable are assigned by reference and passed to function by reference. passing mutable object to functions create
       side effects
    4.
---------------------------
python variables.
-------------------------
how to access globals scope dictionary :  print(globals())
function local scope dictionary can be accessed as :function.__dict__

a variable in python must be initialized before any operation can be performed over it. during the variable initialization
phase compile check the variable type and creates an object and then assigned the reference to that object to variable. since a variable
is an object we can call its destructor by call del x to destroy that object.   calling del on any object in python calls
python object destructor __del__  here object memory is deallocated.

in python everything  is  object in python,   when you create a new varaible in python an object is being created in heap memory and
reference to that object is stored in that variable.   variable are being assigned in python by reference.   when a object variable
is assigned to a variable its reference count field becomes 1.   when the variable is being delete  with  del x  command it refrence
 count become 0.   when the refrence count of the object variable become0. python garbadage collector remove this variable from the heap.
please note that object type is not stored in variable but its stored in object
due to which same variable name can be used to host string, int,  float etc.   that is why python is called dynamic type language.
in dynamic type language variable types are not static and not bound to variables

object is the base object of all the objects in python.

when a new variable is assigned to reference variable already created and initialized with a value. no new object is created.
instead the reference object of same object is being assigned to new variables and its reference count incremented to 2

"""

"""
there are two types of languages.   1. static type reference languages  2.  Dynamic type reference language.  in static type reference 
you declare variable like 

va  a:int =10

in dynamic type reference we delare variable as 

val a =10  --scala language the result is 
val a: Int = 1

In python, compiler finds the assigned variable type and call the respect object constructor method to build object and assign
the reference of that object to variable.  below explicitly object int with argument 10 creates an object and assigned its reference to
variable aa.  compiler does this automatically.  compiler did this type searching only at variable initialization time 
thats why we can write x=[] a=0 etc.  0, 0.0 , [] and {} symbols helps compiler finds its variable types and this type search is not done 
anywhere else thats why we cannot specify these symbols anywhere else.  thats why to create list from generator we have to use list object like
ll = list(x*x for x in range(0,10)),  we cannot use  ll= [x*x for x in range(0,10)]

in case of function,  this type reference comes from calling methods.
"""

aa = int(10)   # which is actually  aa=10
ll = list()    # which is ll=[]
dd = dict()    # which is dd={}


# variable are assigned by reference.
x =543
y=x

# memory address of both the objects are same it means both variable are pointing to same reference object
print ("refrence id X",id(x))
print ("refrence id y",id(y))


"""
for sequence (all sequences can create iterators)  the object is pyvarobject. with type as list.   it has a pointer in value field to list of reference varaibles which 
each variable holding its own object.   pyvarobject has the size field which hold the size of array. 
why an array reference memory gets full,  python creates a memory area twice that size and moves the refrence of list objects to it

"""
xl = {1,2,3,4,5}
yl = xl
yl.add(6)

# xl and yl are pointing to same object.  adding an value to list is visiable to both places.
print (f"xl = {xl  }       yl ={yl }")

"""
Now lets what happens when you use None object.    None is also an object in python.   
"""
yn =None
xn=None

# compares the object by value
if (yn ==xn ):
    print ("both variables are equal")

#compare the object by refrence pointer. S
if (yn is xn):
    print ("both variables are equal")
else:
    print ("both variables are not equal")

"""
in python there are two equal operator == and is.    "==" check the equality variable by variable.  
while "is" checks weather the refrence object address is equal
or not
"""
xll = [1,2,3,4,5]
yll = [1,2,3,4,5]

if (xll ==  yll):
    print ("both variables are equal")
else:
    print ("both variables are not equal")

# here objects by value are same but they are two object with two difference refrence point
# there is give not equal. this is because xll and yll are pointing to different objects by reference
if (xll is  yll):
    print ("both variables are equal by is")
else:
    print ("both variables are not equal by is")

yll = xll

#here both objects are pointing to same reference variable so they should be equal
if (xll is  yll):
    print ("both variables are equal by is")
else:
    print ("both variables are not equal by is")

"""
how variable are assigned to functions arguments.   in python variables are passed by reference. 
in python functions are also object and function objects are created when compiler find def keyword  
"""

# refrence id of nums is being assigned to my_list and then reference object id returned which is being assign to numref
def assign_new_list (my_list):
    print(f"my_list = {id(my_list)} ")
    return my_list

nums = [50, 51,52]
numsref = assign_new_list(nums)

print (f"nums = {id(nums)  }       numsref ={id(numsref)}")

"""
empty list in function arguments
in a function the default argument are being created by __default__ method in function object in static scope. 
therefore default variables are same across all the objects.   this also means the default objects must be 
immutable.  as the side effect show below can noticed if method arguments are not immutable.  if we have use immutable
default arguments in method.  you can see the right implementation.
"""

# wrong implementation
def add_two_to_list(my_list=[]):
    my_list.append(2)
    return my_list


print(globals())
firstcall =add_two_to_list()
secondcall = add_two_to_list()
print(secondcall)

# right implementation
def add_two_to_list_none(my_list=None):
    if not my_list:
        my_list=[]
    # append to list 2
    my_list.append(2)
    return my_list

firstcall1 =add_two_to_list_none()
secondcall1 = add_two_to_list_none()
print(secondcall1)

"""

"""
lvar = 1, [1,2,3,4,5]

#in older version this works with exception
#lvar[1] += [11, 12]
print(lvar)

"""
In Python, when variables are passed into functions, they are passed by reference—more specifically, by "object reference." This means that the function receives a reference to the object the variable points to, not a copy of the object itself. However, the behavior differs depending on whether the object is mutable or immutable.

Behavior with Immutable Objects (like integers, strings, tuples):
When an immutable object is passed to a function, since the object itself cannot be changed (it’s immutable), any operation that might seem to "modify" the object will actually create a new object. This means that the original variable outside the function remains unchanged.
Example:
python
Copy code
def modify_immutable(x):
    print("Original x:", x)
    x += 10  # This creates a new integer object
    print("Modified x inside function:", x)

a = 5
modify_immutable(a)
print("Value of a after function call:", a)  # a remains unchanged
Output:

r
Copy code
Original x: 5
Modified x inside function: 15
Value of a after function call: 5
Here, x refers to an immutable object (an integer), and when we do x += 10, Python creates a new integer object 15 and x now points to this new object inside the function. But outside the function, a still refers to 5, as the function's modification does not affect it.

Potential Problems with Immutable Objects:
The key issue arises when you expect the function to "modify" the original object (as happens with mutable objects), but that doesn’t happen with immutables. For example:

You might expect a function to modify a string or number directly, but it won’t work because they are immutable.
The result can be confusion if you're unaware of the distinction between mutable and immutable objects in Python.

Example of this problem:

def modify_string(s):
    s += " world"  # Creates a new string object
    print("Inside function:", s)

original_string = "Hello"
modify_string(original_string)
print("Outside function:", original_string)  # The string remains unchanged

Output:
Inside function: Hello world
Outside function: Hello

This could be a problem if you expected original_string to be "Hello world" after the function call,
but because strings are immutable, the function's changes did not affect the original variable.

How to Fix It:
If you want a function to "modify" the original variable, there are a few approaches depending on what you want to achieve.

1. Return the modified value from the function:
A common way to handle immutables is to return the new value from the function and explicitly reassign it to the original variable.

python
Copy code
def modify_immutable(x):
    return x + 10  # Return the modified value

a = 5
a = modify_immutable(a)  # Explicitly reassign the result to 'a'
print("Value of a after function call:", a)  # Now a is 15
2. Use mutable objects instead:
If you need to modify the contents of an object inside the function, you can use mutable objects like lists, dictionaries, or custom objects. Since mutable objects are passed by reference, any changes made inside the function will be reflected outside the function.

python
Copy code
def modify_list(lst):
    lst.append(4)  # This modifies the original list

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # Output: [1, 2, 3, 4]
3. Use a Wrapper Class:
Another approach is to use a class or a mutable container that wraps the immutable object, allowing the object to be modified indirectly. This is useful if you still want to work with "immutable-like" values but require a way to change them through a reference.

python
Copy code
class Wrapper:
    def __init__(self, value):
        self.value = value

def modify_wrapper(wrap):
    wrap.value += 10  # Modify the wrapped value

a = Wrapper(5)
modify_wrapper(a)
print(a.value)  # Output: 15
Key Takeaways:
Immutable objects (like integers, strings, and tuples) cannot be changed in-place. Any operation that seems to modify them will result in the creation of a new object, and the original object remains unchanged.
When passing an immutable object to a function, modifications inside the function do not affect the original variable.
To address this:
Return the modified value and reassign it outside the function.
Use mutable objects if in-place modifications are needed.
Use a wrapper class or a container if you want to modify the immutable-like value inside a function.
By understanding how Python handles immutable objects and how references work, you can choose the most appropriate approach for your use case.
"""


