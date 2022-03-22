'''

1.    Python language is designed on the pattern of  yaml.    its a collection of key value pairs.    the keys are on left side and values are on right side.
       the association between a key and value is established by :

2.    on left side reserve words(keywords) must acts like keys which may contain conditional statements  like if statement. "if statement" is a key, which
        must have associated values after ":"

3a.    just like Yaml ,  the python statements should be programmed on one line as (key : value) pair.  However,  if statement contains more than one line
        then second  has to be written after an indent.

        key :
            value1
            value2.,
       Note:   ":"  is used to separate Key from values with an indent.

3b.   the keys acts like a variable, function , class , object  or keyword which points to a reference object stored in a specific scope.
        the object type(weather its, class , function or variable) is stored along with object in memory and can be determined by type()  functions.  the object reference
        memory address is stored in a dictionary in a key: object reference  format

3.    The format  of language is as under:    key: value.    keys can be any function name,  class name,  variable name,  special method (called dunder method)  and
       name module.  the variables are stored in a name space and points to  memory address to their respective module address, function address,
      special methods address, etc. The memory address is actually a reference to an object in memory after its been instantiation.or loaded.  Please note
      python code is first loaded into memory as a singleton object at a certain memory address.   this means for module,  class , functions types class there will
      always be a fix memory address for each class type and there will be a single memory address.   however, when the classes, funciton or types are instanciated
      there can be multiple objects from these classes.

      these key: value pairs are stored in 3 layers called
       name space which define the scope of these key value pairs.  these names space are:
                1.  builtin name space,
                2.  global namespace,
                3. local name space.

5.    The python philosophy is same as its in other code generating languages  like cloud formation or terraform or scala.   Programmer wirites Yaml
        code or json like code which is interpreted into byte code.  in same way, Python virtual machine convert byte code and runs.  Python module PY files
        are first discovered by loaded from paths sys.paths and then loaded into cache into sys.modules.  then the code is compiled and saved a pyc file.
        python then run the code in module.   please note,  python only compiles the imported modules ,   the __main__ module which is a file passed to
        python.sh executable is not compiled.  each file in python is called module ,  the file or module passed to python.sh is called __main__ module as it
        has name __main__ in dunder variable __name__.  the importing module has file name in __name__ variable

                **** main.globals *****
                __name__ __main__                                   # in case the module imported  __name__ will be module1.   if file name is module1.py
                __doc__ None
                __package__ None
                __loader__ <_frozen_importlib_external.SourceFileLoader object at 0x7f90c8f1c5e0>
                __spec__ None
                __annotations__ {}
                __builtins__ <module 'builtins' (built-in)>
                __file__ start.py
                __cached__ None

 6 .  when the python program starts.  which is python command give like "python calc.py".   python runtime environment create a thread or process
       (called interprter).  python finder finds the file passed with python command,   create a module object from it and loads it in memory.  This is the
       global scope of the program.  python automatically imports builtin modules as __builtins__ key.  this is the builtin scope.  all the types, class and
       functions of builtin modules are loaded into memory.   in same way,   python creates namespace for classes and functions.   in python __main__
       module is a tope level module.  while the imported module fall below it.   all modules contain dicttionary objects.   for example when the module type
       is loaded,  its dictionary is created inside it.  which links with variable , classes , function in that module.  a class type in python contains a dictionary.
       which is the dictionary of static variable and methods.    a function type is loaded ,   its methods are inhertied by subclass.   so the hierarchy is :
       main module -> imported module -> classes and variable -> functions.   all the linked list by dictionary variable. in a tree like form and can be seen
       by dir and __dict__.   dir function call __dict__.  but dir() also calls the base class __dict__ so dir give base class attributes also.

         #>>> globals()
            {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__':
            <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>}

6a.   Python keywords like class,  var, def, if  which actually are types, defines different types classes containing  dunder method in specific
         namespace according to their purpose. for example ,   running the program creates a builtin namespace and global  name space.
          class keywork loads a ClassType class and stores class method (which are dunder method) in its global dictionary as an attributes.
        def loads a class of FunctionType in local dictionary/namespace along with its attributes(dunder method).

         please note a function  creates its own local namespace.

        A modules has its own global namespace and a builtin package has it builtin name space
        each dictionary/name space contains different attributes or method as they are being created from different objects.
        for example,   FunctionType create function when it finds keyword  def or lambda.  ClassType creates a class and a ModuleType creates a modules
        when its been find an import statement.  moduleType,  find the module file and loads it into memory and runs it.   all type have a bit of different
         attributes

6b.   python objects can be associated with alias.   "as" keyword is used for that purposes.  "as" is translated as = in python.   for exampel
        import math as m
        which means

        m = importer (math)
        m. exp   # calls the funciton.

        or with (open()) as :    is same as   m=open().

        as means  alias

7 .    you can view the builtin classes, functions,  constants and exception of builtin in package by command   dir(__builtins__)  which gives all the
        functions, methods, variable defined in your current scope.  Note:  dir() gives you global scope and with dir(__builtins__) gives bultin scope
         you can view the bultin contents by this command.   globals() function does not take any parameter and it return
        you global namespace attributes list.  dir()  also function works with modules,   so you can view the contents of module by using,
        dir(math) will provide you all the function methods and constants of math class in math global namespace.  to see which package are being
        imported use dir() command in global name space. To know the keywords of python type  help('keywords').

8 .   dir take an class, object, funciton or module and returns the attribute.    for example  dir(math) return all the math class function.
        dir(math.exp) return the math function exp functions.  to see the function parameters type help(math).  for other use
            help(Function)
            help (str)
            help(sys.argv)
            help('modules')
            help('keywords')
            help('symbols')
            help('topics')

8a.  dir()  function gives the current attributes and all the attributes the functions, variable, scopes, class or object from which it has been inherited.  __dict__ only gives
        current context and does considers the base class attributes.  when the __dict__ function is called with a class it shows class attributes ( class variable and methods)
        but when its been called with an object.  it show object variables (note objects dont contain function,  they are attached with class by self ).

9 .   python also has local name space,  which exists when a function object is created from FunctionType class.   if you can see the function class
        method and variable by dir(FunctionType).   FunctionType table code defined in def ,  compiles it and create a function object.
        a function object creates it local name space which stores all the function variable not the methods.   you can view the values of these variables
        by calling local() functions in function.   if you use __dict__ for function,   you will get empty dictionary {}.   when a function executes
        local variables are created in local namespace and when the function finishes along then  the local scope and variables become out of scope and
        are clear by garbage collector.    since,  the local variable dictionary dies as soon as function call finishes.  you cannot get Function object variable by __dict__
        or dir().   however,  you can get Function class attributes by dir(fnc).  when you can use dir(fnc)  which will give you the special methods of types.FunctionType
        from which most functions are being created.  __dict__ should only be used with classes, modules and objects other than function types.  to see function variable
        you can use locals() function as under:

            def fnc(x=10):
                x =x+10
                print(locals())
                return x+1
        {'x': 20}

10.   everything python is an object.  all the objects are being inherited from object class.   means all data types ,  function,  class are subclasses of object class.
        object class has some predefined method.   which can be viewed by object.__dict__  while run(object) returns the same attributes but in list. these functions
         are available in all the classes.   in same way,   python FunctionType class has been derived from object class
        and contains some extra methods besides object methods.

       import types
       types.FunctionType.__dict__

       mappingproxy({'__repr__': <slot wrapper '__repr__' of 'function' objects>,
              '__call__': <slot wrapper '__call__' of 'function' objects>,                                    # call is Funciton method and not an object method.
              '__get__': <slot wrapper '__get__' of 'function' objects>,
              '__new__': <function function.__new__(*args, **kwargs)>,
              '__closure__': <member '__closure__' of 'function' objects>,                             # is Funciton method and not an object method.
              '__doc__': <member '__doc__' of 'function' objects>,
              '__globals__': <member '__globals__' of 'function' objects>,
              '__module__': <member '__module__' of 'function' objects>,
              '__code__': <attribute '__code__' of 'function' objects>,
              '__defaults__': <attribute '__defaults__' of 'function' objects>,                              #  is Funciton method and not an object method.
              '__kwdefaults__': <attribute '__kwdefaults__' of 'function' objects>,
              '__annotations__': <attribute '__annotations__' of 'function' objects>,
              '__dict__': <attribute '__dict__' of 'function' objects>,
              '__name__': <attribute '__name__' of 'function' objects>,
              '__qualname__': <attribute '__qualname__' of 'function' objects>})

       object.__subclasses__().
       this will return all the subclasses of object class.  A subclass will contain all the functions of a base class

       to get the base class of a class use the following function.
       str.__base__
       <class 'object'>

11   in python "()"  is mandatory at some places and at some place its not.  it mandatory on place  where variable should be immutable and ordering has be
       preserved( as parameters are passed by position)  please note the immutablity is ensured because () is a classType of tuple and tuples are immutable
       for example   def  test( a, b) : a=5  a+b  the a and b variables will be in local scope..   variable a and b are immutable in method.   This is to maintain the
       functional aspect of a function and to avoid side effect.   this means that when  x=5, y=1 and test(x, y) values of x and y does not changes,  however value of
       variables inside method can change.   when python assigns a new value to a, which is immutable it creates a new memory refrence and then assign that memory
        reference to a.  This way,  x and y do ote changes while a can be changed inside the function

            () is mandatory when passing base class to subclass
            (): Tuples, order of operations, generator expressions, function calls.
            Tuples: (), (1, 2, 3)  Although tuples can be created without parentheses: t = 1, 2 → (1, 2).  its , which creates the tuple not ()
            Order of operations: (n-1)**2
            Generator expression: gen = (i**2 for i in range(5)).   gen return generator
            Function or method calls: print(), int(), range(5), '1 2'.split(' ')
            with a generator expression: sum(i**2 for i in range(5))

       in function argument default values acts like static variable.  so  a function     def fun(a=10,b=10):a +b  has default values everywhere.   these variables are
       initialized in FunctionType class as static variables.    this is ok as a and b are immutable however for mutable objects it creates problem as in case of mutable
       object the reference memory address is not changed so  if we define a function like this   def fun(a=10,  b=[]) when the b changes in one function object.,  it will also
       change in another function object. therefore,  it recommended not to initialize   mutable objects  in arguments,   instead,   create an empty list inside
       a function body (as local variable)  to avoid this problem.


12   Python has three types of functions,    1.  methods,    2,  functions,   3.  lambda functions.     methods are binded to classes through self object. functions.
        Function and Lambda are the same concept, however  They are objects  of type  FunctionType or LambdaType.  see the code example below

13.   python object instance being created by __new__ function.   which is being call by interpreter automatically.

        class A(object):
            def __init__(self, name ):
                print("Init is called")
                self.name =name
        # new method calls class object and create a memory slot
        #  then return a reference to that memory slot and call __init__
        #  to initlize the object
            def __new__(cls, name):
                print("Creating instance")
                ins =object.__new__(cls)
                A.__init__(ins, name)
                return ins

            def show_name(self):
                print(self.name)

        ax = A.__new__(A,"Amir")
        ax.show_name()

            __new__ is not bounded to object  as not object has been created so far,  so no self in its arguments.   __new__ creates an instance and assigns it
            refrence address to "self"


13c.   __del__ dunder function is called destructor and __new__ is call constructor.  __del__ function is being called when we del the object by calling  "del  ax"
        __init__  function is called after __new__ constructor ,   __new__ function creates an object in heap and returns its address ,   which is being assinged to self.
        now to connect object with class further class methods are passed self object.   self object connects class with object. so  to initiize  object. __init__ function is called
        from inside __new__  with self object as argument.  Since the objective of __init__is to initialize class variable it does not return anything
        as object will be returned by __new__ function.  all objects in python are objects,   its means,   int, float, number,  string,  functions and
        classes can be deleted by del.   which calls objects __del__ dunder function which acts like destructor.
        There are other function __repr__  and  __str__ .   __str__ gives string representation of a class.

            class Rectangle :
                def __init__ ( self , width , height ) :
                    self.width = width
                    self.height = height
                def area ( self ) :
                    return self.width * self.height
                def perimeter ( self ) :
                    return 2 * (self.width + self.height)
                def __str__ ( self ) :
                    return 'Rectangle (width={0}, height={1})'.format ( self.width , self.height )
                def __repr__ ( self ) :
                    return 'Rectangle({0}, {1})'.format ( self.width , self.height )
                def __eq__ ( self , other ) :
                    print ( 'self={0}, other={1}'.format ( self , other ) )
                    if isinstance ( other , Rectangle ) :
                        return (self.width , self.height) == (other.width , other.height)
                    else :
                        return False

                r1 = Rectangle(10, 20)
                r2 = Rectangle(10,20)
                # done by __str__
                print(r1)

                # done by __repr__
                r1

                #done by __eq__
                r1 ==r2

        What about <, >, <=, etc.?  Again, Python has special methods we can use to provide that functionality. These are methods such as __lt__, __gt__, __le__, etc.

13a     A callable is an object that can be called (using the () operator), and always returns a value.We can check if an object is callable by using the built-in function
           callable

                l = [1, 2, 3]
                callable(l.append)

           for a function to execute in python it must have __call__  method.   which is translated when it encourter ().    so function fnc() translate to fnc.__call__()
           all function contains callable methods like __call__,  __default__ etc.   a function can be called  either by fun()  or by __call__().
           a class can be used as  function by adding the __call__.,   which is equal to () in python.   in this case the class acts like a one function.

            class MyClass:
                def __init__(self):
                    print('initializing...')
                    self.counter = 0

                def __call__(self, x=1):
                    self.counter += x
                    print(self.counter)
            my_obj = MyClass()
            callable(my_obj.__init__)   #  return true
            callable(my_obj.__call__)   #  return true

14     since a function is an object,  it can be passed to another function as parameter and can be returned as function.   This is called clouser.
         once return the outter function returns the inner function and its scope is terminated.  but the variable in outter function are still accessable by inner functions.
         these variable are called free variable and the inner function is call closure.   this is equivalent to object oriented programming encapsulation.

16.  a function object or variable object  when assigned to a variable has reference to that object and its reference counter is incremented by 1.   when another
        variables accesses  the same object memory reference increases by 2.   when no variable is reference any object the object reference counter in memory
        become i0 and python virtual machine garbadage  collection system will remove that variable from memory.   This is called refrene counter.

16a.   another concept is "Share reference and Mutability "   in this concept ,   if immutable objects have same value they can share the same memory address.
         This means two variable are pointing to same memory address.

           a = 10
            b = 10
            print(hex(id(a)))
            print(hex(id(b)))
            0x7559eaf0
            0x7559eaf0

17,  A function containing a variable in its local scope can access a variable in global scope.   however it cannot modify global variable in local scope.   this is because any
        function  which has a variable with same name in global scope as well as in local scope.   the variable in local scope will take precedence.   This is becasue python alway
         looks into its local scope before looking into global scope.  this is call masking
         if it has a variable say  A in global scope and same variable in local scope and we have to modify it.   python always looks into its local scope
        for variable reference and modify the local A variable  thus the global A variable remain unchanged.   to change global A  variable we have to use global
         keyword  in function,  the syntax is

                c=25
                def fun (a, b):
                    global c
                    c=10
                    return 0

        here global c is translated to global()['c']=10

            aa =10
            def  test():
                globals()['aa']=20

            test()
            print(aa)

18.   on same pattern,   if we have nested functions and outer function contains  "X" variable which needs to be modified in inner local function scope,
        we have to use nonlocal key word with the variable X of inner function.   the nonlocal keyword says,  variable is not in global scope and variable is not
        in local scope of this function.  its in outer function local scope.

        g =10
        def outer():
            lo=25
            def inner():
                nonlocal lo
                lo=35
                return lo
            return inner

        x = outer()
        print(x())   // 35

19.   python function arguments are of following types.   a.  positional argument   b.  keyword  arguments c.  default argument   d.  variable length.
        in case of postional arguments parameters are assigned by position ( first position parameter is assigned  to first position in argument),   in case of keyword
         assignment,   parameters keys are matched with argument keys and then values are assigned.   default arguments are those arugment which have default
        values assigned to them and they are optional.  * args are variable length arguments /parameters which are optional.  "*" means 0 or more values.in regular
        expression.   the same is true in python.  **kargs is key based option arguments.

19.   in python *args means slice values of args by position which can be determined from  sequence position(tuple or list).   the process is as under:

        a, *b, c  = (1,2,3,4,5,6).    here * is at index 1 from start and -1 from end.   so our slice is :
        b= d[1: -1]   where d =(1,2,3,4,5,6).
        which returns    (1,(2,3,4,5),6)

        however,  in case of positional functions arguments,   after *arg you cannot give more position argument. so  all the positional variable ends after *arg.
        if you want to add more variables after positional variables you have to use key argument.

        fun( a, b, *args,  **kargs)  or  fun(a,b,*c, d) and pass parameters as (1,2, 3,4,5, d=6).

20.  in python function argument  values are first assigned by position,   then by key words.     this means  def  arg( a, b=2, *c, d).    the parameters can be
        assigned by position till to *c ,   after c the only way you can assign the parameters is by keyworks.      so arg function will be   arg(1,2,,3,4,5,  d=7)
        note d is a dictionary element which is being represented by d=7 outside the {} braces.  here b and c are optional parameters.  as default and variable argument
        are optional

21.  to return a value python function must return a value.   if return statement is not given or nothing is return it will be NONE,  which is equal to null pointer  in java.

22.   in python ,  we can define inner function,   the technique is called closure.   a closure is a function which has a free variable.    so what is a free variable.   suppose you define a
        function outer  which contain one parameter x =5,   outer function also contains an inner function which accesses outer function.   the outer function returns inner funciton.
        when you call the statement    fn = outer().    python assign inner function to fn.    however,  before assigning inner function to fn,   it creates outer function local scoppe ,  create
        x variable and this variable is being accessed in inner.   once outer function finishes it local scope dies and variable x does not dies as its been accessed from inner function.
        this x varaible is called free variable.
        Closure is used in a replacement of encapsulation.   means closure is used in place of class which may have only one funciton.


23.   A closure function which increases the functionality of a already build function is called decorator.
 '''
def divide_by_zero( func ):
    def inner (a, b):
        print(" i am going to divide {} by {}".format(a,b))
        if b==0 :
            print(" Divide by Zero")
            return None
        else:
            return func(a,b)
    return inner

#   divide= divide_by_zero(divide)    note the divide as function and as a parameter for this python property
@divide_by_zero
def  divide (a, b):
    return a/b

c=divide(5, 2)
print(c)

#  above is equivalent to
# divide = divide_by_zero(divide)
# print(divide(10,2))
'''
24.   clousure example.  __closure__
'''
# this is a nested function
def gfg(raise_power_to):
    def power(number):
        return number ** raise_power_to
    return power

raise_power_to_3 = gfg(3)
print(raise_power_to_3.__closure__)
print(raise_power_to_3.__closure__[0].cell_contents)

"""
which returns
(<cell at 0x0000025F0BA4A828: int object at 0x00007FFE64857C80>,)
3
"""

"""
25.   python standard function.  the compiler compile the code in def structure 
        put it to a temporary file and then compiles and save into a temporary location.   
        the compiled code can be instanciated as Function object and called. 
"""
print("----code__ function")
def csum(a=10, b=5):
    return a+b

print(csum())

print(csum.__code__)

"""
<code object csum at 0x00000222BA6846F0, file "C:/Users/amirr/PycharmProjects/pythontraining/python/0.0 Python Architect.-lang-Fnc.py", line 299>
code at line 299 is compiled and then called as function 
"""

"""
26.    A function is an instance of FunctionType. 
"""
import types
print("This is a  function {0}".format(isinstance(csum , types.FunctionType)))

"""
26.   A lambda function is an instance of LambdaType
"""
lam = lambda a,b : a+b
print("This is a Lambda function {0}".format(isinstance(lam, types.FunctionType)))

"""
27.   since everything is an object.   this section demonstrated now a function object is being 
        created. 
"""
dynfl = types.FunctionType(compile('2/3', 'dyn.py','eval'), {})
print("The function object is {0}".format(dynfl()))

print("Dynfi is a instance of function and is being "
      "created from FunctionType (y/N): {0}".format(isinstance(dynfl, types.FunctionType)))

print(type(dynfl))

"""
28.   A lambda function is also a function object. 
"""

dynflam01 = types.LambdaType(compile( '2/3', '','eval'), {})
print("This is a Dynamic Lambda function {0}".format(dynflam01()))


print("dynflam01 is a instance of function and is being "
      "created from LambdaType (y/N): {0}".format(isinstance(dynflam01, types.LambdaType)))

"""
29.   function defined in classes are called method and they are joined to classes through self method.  
        function containing self argument cannot be called without instanciating the object as no function is bind
        to class
"""

# class created with one method
class A:
    def func(self):
        print('I am called from', self)

# object create for A and named a
a=A()

# this method is not binded to class.  but it can be binded to object
def func2(self):
    print('I am func2')

##
#func2()

''''
called func2 without binding to object creates the following exception
Traceback (most recent call last):
  File "C:/Users/amirr/PycharmProjects/pythontraining/python/0.0 Python Architect.-lang-Fnc.py", line 364, in <module>
    func2()
TypeError: func2() missing 1 required positional argument: 'self'
'''

# function func2 is being binded to object a.
a.func2 = types.MethodType(func2,a)

# or types.MethodType(func, a, A) for PY2
a.func2()

"""
30 :   a module (python file)  is also an object.  so once a module or package is being created.  you can access its functions,
         variable or constant through object name.   
         
         import math as m
         m.exp()
         
         loading a module to python is two way, process.  1.  find and load module   2.  compile and run
         
         importer is module we create to demonstrated how modules works.   detailed in another section
"""
import importer
import sys

mod = importer.import_('mody','mody.py', '.')

# when a package is found and loaded ,  it is loaded into sys.modules cache
# and later an entry is being added to the global directory with key mod.
#  when the module is deleted  by del m.   the entry from the global directory
#  is being remove but the module remains cached in sys.
print("sys says:", sys.modules.get('mody','modules not found '))

# this is module object and it acts similar to a class object
mod.test_func()

#The __dict__ attribute of a function object stores attributes assigned to the function object.

def foo():
    a = 2
    return a

foo.bar = 12
print(foo.bar)
foo.__dict__

#{'bar': 12}
#Attributes of the function object are not related to the local variables that exist during the function call. The former is unique
#there is one __dict__ per function object) the latter are not (a function may be called multiple times with separate local variables).

def nfoo(n: int):
    print(f'level {n} before:', locals())
    if n > 0:
        nfoo(n - 1)
    print(f'level {n} after: ', locals())

nfoo(2)
#level 2 before: {'n': 2}
#level 1 before: {'n': 1}
#level 0 before: {'n': 0}
#level 0 after:  {'n': 0}
#level 1 after:  {'n': 1}
#level 2 after:  {'n': 2}


"""
31.  Note:   you can use *arg and **kargs to pass one parameter, two parameters or no parameters.   *args and **kargs are optional positional and keyword parameters
"""
def test_args_kargs(*arg, **karg):
    if arg:
        return len(arg)
    else:
        return len(karg)

print ("dictionary:{0}".format(test_args_kargs(k=1,l=2,m=3, n=4)))
print ("tuple:{0}".format(test_args_kargs(1,2,3, 4)))
print ("None:{0}".format(test_args_kargs()))








