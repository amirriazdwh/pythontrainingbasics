'''
1. Python language is made on the pattern of  yaml.    its a collection of key value pairs.    the keys are on left side and values are on right side.
2. on left side reserve words most acts like key with conditions.
3.  on right side values acts and  define scope,  which can be global,  builtin or local.   in reality value section is store in a dictionary which can be global, builtin or local
4.  just like Yaml ,  its a key : value language,   and if value has more than one field.  its store in next line after indentation.   exmaple

        key :
            value1
            value2.,
    Note:   ":"  is used to separate Key from values.

5.   The philosophy is same as its in other code generating system  for example  cloud formation or terraform.   Programmer wirites Yaml like code
        which Python virtual machine convert to code and run that coe.

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

        builltin scope is python kernal,   which interpretes the yaml like code.   it contains system function coming from Virtual machine.
        Global scope is your python file,   once its been load into memory and its dictionary has been created.   please note that module is first loaded into memory and then run
              during the load phase,  the python file is being search and during during into memory,   its dictionary is being created which is called global dictionary.   since global
              dictionary is created inside the kernal,  its inside the builtin dictionary.
         local scope,   is created once function, classs or any object are loaded into memory.    please note objects are first loaded into memory and then executed.   during the
        class loading phase,   class dictionary is being created  which is a way to create static variables,    as any variable inside class is stored in that dictionary and this dictionary
        is different from object instance dictionary which is being created which the object is being create with __New__ function
9. .    Everything in python is an object.   class,  data types,  functions,  import ,  modules,
10.   class,  var, def at the start of class variable, function defination define the type of dictionary which this object will define.   thats why class dictionary is a bit different  from variable and
         a variable dictionary is a bit different from function.
11.  python objects can be associated with alias.   as keyword is used for that purposes.
12   a function has its own dictionary so a function has its own scope.  in same way global and buildin has their own
        scope and own dictionary.    python compiler first looks for an variable in function in its own scope/dictionary if
        not found,  looks in global dictionary/scope
13.      function default variables are created in static scope and its been created by __default__ dunder method when the function is loaded into memory and its local dictionary is
         being created.
14   since a function is an object,  it can be passed to another function which is also an  object function and can be returned as function.   this means a  function object can be assigned to a variable also.
15.  all objects in python are objects,   its means,   int, float, number,  string ,  functions and classes can be deleted by del.   which calls objects __del__ dunder function which acts like destructor.
16.  a function when assigned to a variable has reference to object function  and its reference counter is incremented by 1.   when two variables are being assigned to same object,   object memory refrence 2 two.   when no
        variable is refrencing any object the object reference counter is 0 and virtual machine garbadage collection system will remove this variable from memory.
        has a mapping is store in high scope dictionary.  since function is a object it can be delete as del function_variable
17.
 '''