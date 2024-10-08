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