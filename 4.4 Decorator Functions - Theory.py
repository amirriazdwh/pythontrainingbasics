"""
decorate are the function also called high order function which takes a function as argument and return a function or object

high order function has following properties
Accepts Functions as Arguments:
A higher-order function can take one or more functions as input. This allows for dynamic behavior,
where the function’s behavior can be customized based on the functions passed to it.

Returns Functions as Results:
A higher-order function can return a function as its output. This enables the creation of new functions
dynamically based on certain conditions or parameters.

Enhances Code Reusability:
By using higher-order functions, you can write more modular and reusable code.
 Functions like map, filter, and reduce in Python are classic examples of higher-order functions that help in
 processing collections of data efficiently.

Supports Functional Programming Paradigms:
Higher-order functions are a key feature of functional programming,
promoting immutability and pure functions, which can lead to more predictable and maintainable code.

Enables Function Composition:
Higher-order functions allow for the composition of multiple functions to create more
complex operations. This can simplify complex logic by breaking it down into smaller, reusable functions.

 a decorator can return an object. This is particularly useful when you want to enhance a function’s behavior
 by wrapping it in an object that provides additional methods or properties

 A decorate needs a funciton inside decorate or an object inside the decorate function
 which it will return
"""

class Timer:
    def __init__(self, func):
        self.func = func
        self.execution_time = None

    def __call__(self, *args, **kwargs):
        import time
        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()
        self.execution_time = end_time - start_time
        return result

    def get_execution_time(self):
        return self.execution_time

@Timer
def example_function():
    import time
    time.sleep(2)
    print("Function finished")

# Using the decorated function
example_function()
print(f"Execution time: {example_function.get_execution_time()} seconds")

"""
Timer class: This class acts as a decorator. It takes a function as an argument and stores it.
__call__ method: This method allows the Timer instance to be called like a function. It measures the execution time of the wrapped function.
get_execution_time method: This method returns the execution time of the wrapped function.
When you decorate example_function with @Timer, it becomes an instance of the Timer class. You can call example_function as usual, and it will print the execution time using the get_execution_time method.
"""

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} finished")
        return result
    return wrapper

@log_decorator
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")

"""
Without Brackets: The decorator function itself is applied directly to the function.
With Brackets: The outer function (decorator factory) is called first, which returns the actual decorator function.
This decorator function is then applied to the function.
"""
def print_finish(param):
    # This function is called first with the parameter 'True'
    print("print_finish called with param:", param)
    def wrapper(func):
        # This function is returned by print_finish and called with the original function
        print("wrapper called with func:", func.__name__)
        def inner_wrapper(*args, **kwargs):
            # This function is returned by wrapper and replaces the original function
            print("inner_wrapper called")
            result = func(*args, **kwargs)  # Call the original function
            if param:
                print("Finish")
            return result
        return inner_wrapper
    return wrapper


# Example usage
@print_finish(True)
def example_function():
    print("Function is running")


#example_function = print_finish(True)(example_function)
# This is where the decorated function is called
#example_function()

should_print_finish = True  # This can be set dynamically

def print_finish(param):
    print("print_finish called with param:", param)
    def wrapper(func):
        print("wrapper called with func:", func.__name__)
        def inner_wrapper(*args, **kwargs):
            print("inner_wrapper called")
            result = func(*args, **kwargs)
            if param:
                print("Finish")
            return result
        return inner_wrapper
    return wrapper

@print_finish(should_print_finish)
def my_function():
    print("Original function called")

my_function()


"""
Memoization Decorator
Memoization is a technique to cache the results of expensive function calls and reuse them when the same inputs occur
 again. This can significantly improve performance for functions with expensive computations.
"""
def memoize(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@memoize
def fibonacci(n):
    if n in (0, 1):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(35))  # Much faster due to memoization

"""
Logging Decorator
A logging decorator can be used to log the execution of functions, which is useful for debugging and monitoring.
"""
import logging

def log_execution(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Executing {func.__name__} with arguments {args} and {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_execution
def add(x, y):
    return x + y

add(5, 3)

"""
3. Authorization Decorator
This decorator can be used to check if a user has the necessary permissions to execute a function
"""

def requires_permission(permission):
    def decorator(func):
        def wrapper(user, *args, **kwargs):
            if not user.has_permission(permission):
                raise PermissionError(f"User lacks {permission} permission")
            return func(user, *args, **kwargs)
        return wrapper
    return decorator

@requires_permission('admin')
def delete_user(user, user_id):
    print(f"User {user_id} deleted")

# Assuming `current_user` is an object with a `has_permission` method
# delete_user(current_user, 123)
"""
4. Retry Decorator
A retry decorator can automatically retry a function if it raises an exception, which is useful for handling 
transient errors in network calls or other unreliable operations.
"""
import time
import random

def retry(max_attempts, delay):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    print(f"Attempt {attempts} failed: {e}")
                    time.sleep(delay)
            raise Exception(f"Failed after {max_attempts} attempts")
        return wrapper
    return decorator

@retry(max_attempts=3, delay=2)
def unreliable_function():
    if random.random() < 0.7:
        raise ValueError("Random failure")
    return "Success"

print(unreliable_function())
"""
5. Class Decorators
Decorators can also be applied to classes to modify their behavior. For example, you can use a class decorator 
to automatically add methods or properties to a class.

"""

def add_method(cls):
    def new_method(self):
        return "New method added!"
    cls.new_method = new_method
    return cls

@add_method
class MyClass:
    def existing_method(self):
        return "Existing method"

obj = MyClass()
print(obj.existing_method())  # Output: Existing method
print(obj.new_method())       # Output: New method added!


