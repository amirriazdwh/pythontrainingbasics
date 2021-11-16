"""
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


