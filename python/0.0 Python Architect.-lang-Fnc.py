'''
1. Python language is made on the pattern of  yaml.    its a collection of key value pairs.    the keys are on left side and values are on right side.
2. on left side reserve words most acts like key which may contains conditions.  like if statement.   if statement is a key which must have
3.  on right side values acts and  define scope,  which can be global,  builtin or local.   in reality value section is store in a dictionary which can be global, builtin or local
4.  just like Yaml ,  its a (key : value) language,   and if value has more than one field.  its store in next line after indentation.   exmaple

        key :
            value1
            value2.,
    Note:   ":"  is used to separate Key from values.

5.   The philosophy is same as its in other code generating system  like loud formation or terraform.   Programmer wirites Yaml  code
        which Python virtual machine convert to code and runs.

6.   when the python interpretor run a python file,   it looks for keywords and its matching pair keys.   for example,   in case of   if statement  compiler looks for else key pairs and thats
      how it confirms that language sytax is correct.   after confirmation that sytax is correct,   it generates the c core.

7.   in python ()  is mendatory at some places and at some place its not.    it mandatory  on place where variable should be immutable and ordering has be preserved..
      python accomplish this by hiding the entries of these variables in dictionary.    so that they cannot be modified.   for exmaple   def  test( a, b) :  a+b  the a and b variables
      will not be in local dictionary.   in same way,   for class the parent class based entry will be in child class but it will not be visiable.     also  it means that you can inhert class
      as     class child ( partent) :

8.   Python has different by of dictionary which contain different attributes.   these dictionaries define the scope of the object.   as everything in python is an object..  these scopes are:
        1.1   Builin scope
        1.2   Global scope
        1.3   local scope.

        builltin scope is python kernal,   kernal interpretes the yaml like code.   it contains builtin functions and system module (sys)  to manage
         virtual machine.  the builtin functions are part of python kernal and therefore available to all programs.  these builtin fuctions has dictionary where they store data.
         https://docs.python.org/3/library/functions.html.   all the builtin functions,   types , keywords are inside interpretor
         As an implementation detail, most modules have the name __builtins__ made available as part of their globals. The value of __builtins__
         is normally either this module or the value of this module’s __dict__ attribute. Since this is an implementation detail, it may not be used by alternate
          implementations of Python.  The means are builtin modules are automatically imported into all the global scopes.
          #>>> globals()
            {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__':
            <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>}

        Global scope is your python file,  a  file is first  loaded into memory and then its dictionary is created. please note that modules in python file are first loaded into memory
         and then run.   During the load phase,  the python file is being search and  then its dictionary is being created in memory which is called global dictionary.  A global dictionary
         contains all the imports builtin or custom,   which are stored in dictionary as key values.   the modules , variables, functions which are in global scope are available to all
         the object and function in file.   each object and function in a file then have a local scope.

         local scope,   is created once function, classs or any object are loaded into memory.    please note objects are first loaded into memory and then executed.   during the
        class loading phase a class create its own local dictionary this dictionary is different from object diction,   class dictionary icreated is a way to create static variables,
        as any variable inside class is stored in its class dictionary and is different from object instance dictionary which is being created which the object is being
        create with __New__ function

9. .    Everything in python is an object.   class,  data types,  functions,  import ,  modules,
10.    keywords like class,  var, def at the start of class variable, function defination define the type of dictionary which that object creates.
        thats why class dictionary is a bit different  from variable and a variable dictionary is a bit different from function.

11.   python objects can be associated with alias.   as keyword is used for that purposes.

12   a function has its own dictionary so a function has its own scope.  in same way global and buildin has their own
        scope and own dictionary.    python compiler first looks for an variable in function in its own local scope/dictionary if
        not found,  looks in global dictionary/scope else finally looks into builtin scope

13.   function default variables are created in static scope as function or function class being loaded into memory.   this is accomplish by __default__ method execution
       python function object being created by __new__ function.   which is being call by interpreter automatically.  for a function to execute in python it must has () along with his name

 13a.  an object can be as function by adding the __call__.,   which is equal to () in python.   in this case the class acts like a one function.

14   since a function is an object,  it can be passed to another function which is also an  object function and can be returned as function.
      this means a  function object can be assigned to a variable also and can be delete by del.   which call object destructor

15.  all objects in python are objects,   its means,   int, float, number,  string ,  functions and classes can be deleted by del.   which calls objects __del__ dunder function which acts like destructor.

16.  a function when assigned to a variable has reference to object function  and its reference counter is incremented by 1.   when two variables are being assigned to same object,
       object memory refrence 2 two.   when no variable is refrencing any function object the object reference counter in memory become i0 and
       virtual machine garbadage collection system will remove this variable from memory.

17,  A function which has a varaible in local scope (dictionary)  can access a variable in global scope.   however it cannot modify global variable in local scope.   this is because any function
       if it has a variable say  A in global scope and same variable in local scope ( which we require to modify) and we have to modify it.   python always looks into its local scope
       for variable reference and modify the local A variable  while the global A variable remain unchanged.   to change global A  variable we have to use global key work in function,  which copy
       the global variable object refrence to local variable and then perform the variable modifications.

18.   on same pattern,   if we have nested functions and outer function contains a X variable which needs to be modified in inner local function,  we have to use nonlocal key word.

19.   python function arguments are of following types.   a.  positional argument   b.  keyword   c.  default d.  variable length.   in case of posional arguments parameters are
        assigned by position ( first poistion parameter to first position argument),   in case of keyword assignment,   parameters keys are matched with argument keys and then
        values are assigned.   default arguments are those which have default values assigned and they are optional.  * args are variable length arguments /parameters which
        are optional.  as * means 0 or more values in regular expression

19.   in python *args means slice values of args by postions which can be determined from any sequence (tuple or list)

20.  in python function argument  values are first assigned by position,   then by key words.     this means  def  arg( a, b=2, *c, d).    the parameters can be assigned by position
       till to *c ,   after c the only way you can assign the parameters is by keyworks.      so arg function will be   arg(1,2,,3,4,5,  d=7)    not d is a dictionary element which is being
       represented by d=7 outside the {} braces.  here b and c are optional parameters

21.  to return a value python function must return a value.   if return statement is not given or nothing is return it will be NONE,  which is equal to void in java.

22.  in python ,  we can define inner function,   the technique is called closure.   a closure is a function which has a free variable.    so what is a free variable.   suppose you define a
       function outer  which contain one parameter x =5,   outer function also contains an inner function which accesses outer function.   the outer function returns inner funciton.
       when you call the statement    fn = outer().    python assign inner function to fn.    however,  before assigning inner function to fn,   it creates outer function local scoppe ,  create
        x variable and this variable is being accessed in inner.   once outer function finishes it local scope dies and variable x does not dies as its been accessed from inner function.
        this x varaible is called free variable.
        Closure is used in a replacement of encapsulation.   means closure is used in place of class which may have only one funciton.

23.  A closure function which increases the functionality of a already build function is called decorator.

17.  Please note that in object we have dunder function like __repr__  ,  __getitem__,   if you try to call these function with   object.__repr__ you may get error.   the best way to call them is to
       use function like repr(object).   inside the function they are being called as object.__repr__
18.  please note that __getitem__ =[]  and __call__  = ()
19.
 '''

def divide_by_zero(  func ):
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

#c=divide(5, 0)
#print(c)

divide = divide_by_zero(divide)
print(divide(10,2))