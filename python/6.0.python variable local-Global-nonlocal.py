"""
---------------------------
python variables.
-------------------------
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
"""

# wrong implementation
def add_two_to_list(my_list=[]):
    my_list.append(2)
    return my_list

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
Global Variables
In Python, a variable declared outside of the function or in global scope is known as a global variable.
This means that a global variable can be accessed inside or outside of the function.

when a function has global  variable with same name as it has in function.   the compiler look for that variable first in function
and then in its global region

Let's see an example of how a global variable is created in Python.

Example 1: Create a Global Variable

"""
x = "global"

def foo():
    print("x inside:", x)


foo()
print("x outside:", x)

"""
In the above code, we created x as a global variable and defined a foo() to print the global variable x. Finally, we call the foo() 
which will print the value of x.

What if you want to change the value of x inside a function?
"""

x = "global"

def foo():
    x = x * 2
    print(x)

#foo()

"""
The output shows an error because Python treats x as a local variable and x is also not defined inside foo().

To make this work, we use the global keyword. Visit Python Global Keyword to learn more.
"""

"""
Local Variables
A variable declared inside the function's body or in the local scope is known as a local variable.

Example 2: Accessing local variable outside the scope
"""
def foo():
    y = "local"


foo()
print(y)

"""
Example 3: Create a Local Variable
Normally, we declare a variable inside the function to create a local variable.
Let's take a look at the earlier problem where x was a global variable and we wanted to modify x inside foo().
"""

def foo():
    y = "local"
    print(y)

foo()

"""
Global and local variables
Here, we will show how to use global variables and local variables in the same code.

Example 4: Using Global and Local variables in the same code
"""
x = "global "

def foo():
    global x
    y = "local"
    x = x * 2
    print(x)
    print(y)

foo()

"""
In the above code, we declare x as a global and y as a local variable in the foo(). Then, we use multiplication operator * to modify
 the global variable x and we print both x and y.

After calling the foo(), the value of x becomes global global because we used the x * 2 to print two times global. 
After that, we print the value of local variable y i.e local
"""

x = 5

def foo():
    x = 10
    print("local x:", x)


foo()
print("global x:", x)


"""
In the above code, we used the same name x for both global variable and local variable. We get a different result 
when we print the same variable because the variable is declared in both scopes, i.e. the local scope inside foo() and global scope outside foo().
When we print the variable inside foo() it outputs local x: 10. This is called the local scope of the variable.
Similarly, when we print the variable outside the foo(), it outputs global x: 5. This is called the global scope of the variable.
"""

"""
Nonlocal Variables
Nonlocal variables are used in nested functions whose local scope is not defined. 
This means that the variable can be neither in the local nor the global scope.
Let's see an example of how a nonlocal variable is used in Python.
We use nonlocal keywords to create nonlocal variables.
Example 6: Create a nonlocal variable
"""

def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)


outer()

"""
In the above code, there is a nested inner() function. We use nonlocal keywords to create a nonlocal variable. 
The inner() function is defined in the scope of another function outer().
"""
