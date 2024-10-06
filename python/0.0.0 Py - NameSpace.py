"""
############################################################################
Key Points to Remember- Namespace
############################################################################
python has 4 types of namespace.
1. Built-in Namespace:
Initialized when the Python interpreter starts. it loads the buildin module of python builtin.py and other modules to provide access
to builtin function for example print functions etc

2. Global Namespace:
When a module or Python file is loaded, it is initialized into module and registered in sys.modules. This registration helps the program find modules that
have already been loaded. A global namespace is created for each module that is loaded and registered in sys.modules. This global namespace
contains the module’s variables, classes, and functions. Each module has its own namespace.
When mymodule is imported, it creates its own global namespace containing global_var and greet. If you create a global variable
inside a function using the global keyword, it gets created in the module’s global namespace.
Using del mymodule deletes the reference to the module, effectively removing its global namespace and the global variables within the module.
After deletion, attempting to access mymodule raises a NameError because the module is no longer defined.
so a global variable has its global scope inside module only

Note: Module functions and variables are defined in the module’s global namespace.
      Within a Module: Global variables are accessible only within the module they are defined in.
      Across Modules: You can share global variables across modules by defining them in a separate module and importing that module wherever needed.

3. Enclosing Namespace:
Created dynamically when a nested function is called.
a good way to think about enclosing namespace . The enclosing namespace can be seen as having a reference or name of the local namespace of the outer function.
This reference allows the inner function to access and potentially modify variables from the outer function’s scope.

4. Local Namespace:
Created dynamically when a function is called. each function has its own local namespace
Local Namespace: Contains variables and inner functions defined within a function.
Creation and Destruction: Created when the function is called and destroyed when the function returns.
Scope: Variables in the local namespace are only accessible within the function.

"""

"""
When a subclass is instantiated in Python, the base class’s __init__ method is called first, initializing the base 
class part of the instance. This means that the attributes and methods defined in the base class are available in the
 subclass instance.

However, the attributes and methods are not stored in separate dictionaries for the base class and subclass. Instead, 
they are all part of the same instance dictionary (__dict__). The subclass instance will have access to all attributes 
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

why 
"""