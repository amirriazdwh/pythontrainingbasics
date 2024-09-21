"""
Python’s exception handling syntax is designed to be clear, concise, and easy to use. It allows you to manage errors
 gracefully and maintain the flow of your program. Here’s a breakdown of the key components and why they are structured
 the way they are:

Key Components
1. try Block:
The try block contains the code that might raise an exception.
If an exception occurs, the rest of the code in the try block is skipped.

2.except Block:
The except block catches and handles the exception.
You can specify the type of exception to catch, allowing for specific handling of different errors.

3. else Block (Optional):
The else block contains code that runs if no exceptions were raised in the try block.
This is useful for code that should only run if the try block succeeds.

4. finally Block (Optional):
The finally block contains code that runs regardless of whether an exception was raised or not.
This is typically used for cleanup actions, such as closing files or releasing resources.

try:
    # Code that might raise an exception
    result = 10 / 0
except ZeroDivisionError as e:
    # Handle the specific exception
    print(f"Caught an exception: {e}")
else:
    # Code to run if no exceptions were raised
    print("No exceptions occurred")
finally:
    # Code that runs regardless of whether an exception occurred
    print("This will always run")

"""

"""
Creating a custom exception in Python involves defining a new class that inherits from the built-in Exception class. T
his allows you to create exceptions that are specific to your application’s needs. Here’s a step-by-step guide with 
an example:

Step-by-Step Guide
Define the Custom Exception Class:
Inherit from the Exception class.
Optionally, override the __init__ method to accept custom arguments.
Optionally, override the __str__ method to provide a custom string representation.
Raise the Custom Exception:
Use the raise statement to raise the custom exception when needed.
Handle the Custom Exception:
Use a try-except block to catch and handle the custom exception.

class InvalidAgeException(Exception):
    '''Exception raised for errors in the input age.

    Attributes:
        age -- input age which caused the error
        message -- explanation of the error
    '''

    def __init__(self, age, message="Age must be at least 18"):
        self.age = age
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.age} -> {self.message}'
        
#main.py    
from custom_exceptions import InvalidAgeException

def check_age(age):
    if age < 18:
        raise InvalidAgeException(age)
    else:
        print("Age is valid")

def main():
    try:
        age = int(input("Enter your age: "))
        check_age(age)
    except InvalidAgeException as e:
        print(f"Caught an exception: {e}")

if __name__ == "__main__":
    main()


"""