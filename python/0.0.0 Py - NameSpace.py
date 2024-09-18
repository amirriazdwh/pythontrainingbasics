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