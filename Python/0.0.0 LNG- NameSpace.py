"""
############################################################################
Key Points to Remember- Namespace
############################################################################
1. Modules are objects that Python uses to group related code together (like variables, functions, and classes).
2. Internally, Python represents the contents of a module using a dictionary (__dict__). This dictionary serves as the module’s namespace.
3. The __dict__ attribute of a module provides direct access to all its attributes in the form of key-value pairs.  in short,
Every Python module has an attribute called __dict__ that contains a dictionary of all the functions, global variables and their values defined
in that module
4. a dictionary is a key value pair,   which stores,  variable and its object references. so a module contains dictionary,  which
stores variable and function objects in key value form.
5. The sys.modules dictionary acts as a registry of all imported modules, mapping module names to module objects.
6. when you issue python statement.   python start.py.   interpreter assign start.py module as __main__.  this module build global namespace
for other module.  file name is module name.
7.  global variables of main modules can be viewed with globals() function.  for imported modules use module.__dict__

python has 4 types of namespace.

##########################
1. Built-in Namespace:
#########################
When the Python interpreter starts, it initializes its built-in environment, which includes loading a special module called builtins.py
along with other essential modules. This process is what provides access to built-in functions like print(), len(), input(), and many
others. These built-in functions are available globally in Python programs without the need for importing any module.

The builtins module includes not only functions but also built-in types (like int, str, list, etc.) and exceptions
(like TypeError, ValueError, etc.). This is why you can use these features directly in your code without needing to
explicitly import them. Essentially, when the Python interpreter is launched, it sets up this built-in environment to ensure
that commonly used functionality is readily available throughout your program.

########################
2. Global Namespace:
######################
This is the namespace of the main program that is executed.
It includes all the variables, functions, and classes defined at the top level of your script.
When you run a script or start an interactive Python session, the global namespace is the primary namespace where your code executes.
The global namespace is specific to the main module (i.e., the script you run directly).

When you run a script directly, Python treats it as the main module and assigns it the special name __main__.
This is why the global namespace of the script you run is often referred to as the global namespace.

Note that all the variable created during the load process are global variables and they are global to main module only or
to module in which they are defined.  to access the variables in another module.  the module needs to be imported

 If you import a module in your script and then use the del statement to delete it, you can remove the reference to
 that module from the global namespace. However, deleting the module reference does not unload the module from Python’s
 memory if it has already been loaded.

you cannot delete the __main__ module.  however,  you are delete the variables from __main__ module.  this variables are
called global variables.

#############################
How import module is loaded.
#############################

When you import a module in Python, the interpreter goes through a series of steps to load and initialize the module. Here's how it works:

Finding the Module:
When you use import my_module, Python looks for my_module.py in the directories listed in sys.path.
The search order includes the current directory, installed packages, and standard library locations.

Compiling the Module:
If the module is written in Python, the source code (my_module.py) is compiled into bytecode (my_module.pyc) if it
 hasn't been compiled already or if the source code has changed.
This compilation step transforms Python code into bytecode, which the Python Virtual Machine (PVM) can execute.

Creating a Module Object:
Once the code is compiled, Python creates a module object of type module. This object is essentially a namespace that
 contains all the functions, variables, and classes defined in the module.
The module object is an instance of Python's built-in types.ModuleType.

Executing the Module Code:
Python then executes the compiled bytecode in the context of the newly created module object. This means that any top-level
statements (like variable assignments, function definitions, etc.) in the module are executed at this point.
The result is that all variables, functions, and classes defined in the module become attributes of the module object.
Registering the Module in sys.modules:

Once the module is successfully loaded and its code executed, Python registers it in the sys.modules dictionary.
sys.modules is a cache that stores references to all modules that have been imported. This prevents Python from reloading
 the same module multiple times within a single program.

If you import the same module again, Python will simply retrieve it from sys.modules instead of reloading and re-executing it.

Note: Module functions and variables are defined in the module’s global namespace.
      Within a Module: Global variables are accessible only within the module they are defined in.
      Across Modules: You can share global variables across modules by defining them in a separate module and importing
      that module wherever needed.

3. Local Namespace:
Created dynamically when a function is called. each function has its own local namespace
Local Namespace: Contains variables and inner functions defined within a function.
Creation and Destruction: Created when the function is called and destroyed when the function returns.
Scope: Variables in the local namespace are only accessible within the function.

4. Enclosing Namespace:
Created dynamically when a nested function is called.
a good way to think about enclosing namespace . The enclosing namespace can be seen as having a reference or name of the
local namespace of the outer function.
This reference allows the inner function to access and potentially modify variables from the outer function’s scope.



"""

"""
When a subclass is instantiated in Python, the base class’s __init__ method is called first, initializing the base 
class part of the instance. This means that the attributes and methods defined in the base class are available in the
 subclass instance.

However, the attributes and methods are not stored in separate dictionaries for the base class and subclass. Instead, 
they are all part of the same module instance dictionary (__dict__). The subclass instance will have access to all attributes 
and methods from both the base class and the subclass.

class BaseClass:
    def __init__(self):
        self.base_attribute = "I am from the base class"
    
    def base_method(self):
        return "This is a method from the base class"

class SubClass(BaseClass):
    def __init__(self):
        super().__init__()  # Call the base class constructor
        self.sub_attribute = "I am from the subclass"
    
    def sub_method(self):
        return "This is a method from the subclass"

# Instantiate the subclass
sub_instance = SubClass()

# Access attributes and methods
print(sub_instance.base_attribute)  # Output: I am from the base class
print(sub_instance.sub_attribute)   # Output: I am from the subclass
print(sub_instance.base_method())   # Output: This is a method from the base class
print(sub_instance.sub_method())    # Output: This is a method from the subclass

# Check the instance dictionary
print(sub_instance.__dict__)

In this example:

The BaseClass has an attribute base_attribute and a method base_method.
The SubClass inherits from BaseClass and adds its own attribute sub_attribute and method sub_method.
When SubClass is instantiated, the BaseClass constructor is called first (using super().__init__()), initializing base_attribute.
The sub_instance has access to both base_attribute and sub_attribute, as well as base_method and sub_method.
The instance dictionary (__dict__) will contain all attributes from both the base class and the subclass:


{'base_attribute': 'I am from the base class', 'sub_attribute': 'I am from the subclass'}


Conclusion:  this means that variable and methods of both base class and subclass are created in same dictionary.  
             there does not exists a separate dictionary for base and subclass.  that is why object.method() is from
             one dictionary level namespace.  
             
class MyClass:
    def __init__(self, value):
        self.value = value

    def check_memory_address(self):
        # Print the memory address of the instance (self)
        print("Memory address of self:", id(self))

# Create an instance of MyClass
instance = MyClass(42)

# Print the memory address of the instance
print("Memory address of instance:", id(instance))

# Call the method to check the memory address of self
instance.check_memory_address()


Memory address of instance: 140234866534752
Memory address of self: 140234866534752


This output confirms that both instance and self refer to the same object in memory. The id() function shows 
that they have the same memory address, proving that self is indeed a reference to the instance of the class


Python translates this to MyClass.display_value(instance) under the hood. This is how Python passes the instance 
(instance) as the first argument (self) to the method.

Here’s a more detailed breakdown:

Method Call: When you call instance.display_value(), Python looks up the display_value method in the class 
of instance (which is MyClass).
Implicit self: Python implicitly passes the instance (instance) as the first argument to the method.
So, instance.display_value() is equivalent to MyClass.display_value(instance).
Let’s see this in action with an example:

class MyClass:
    def __init__(self, value):
        self.value = value

    def display_value(self):
        return f"The value is {self.value}"

# Create an instance of MyClass
instance = MyClass(42)

# Call the method using the instance
print(instance.display_value())  # Output: The value is 42

# Call the method explicitly using the class and passing the instance
print(MyClass.display_value(instance))  # Output: The value is 42

In this example:

instance.display_value() implicitly passes instance as the first argument to display_value.
MyClass.display_value(instance) explicitly passes instance as the first argument.
Both calls produce the same result, demonstrating that instance.display_value() is indeed equivalent to 
MyClass.display_value(instance) under the hood. This mechanism allows instance methods to access and
 modify the instance’s attributes using self.
"""