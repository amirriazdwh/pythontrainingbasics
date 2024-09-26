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
# @print_finish(True)
def example_function():
    print("Function is running")


example_function = print_finish(True)(example_function)
# This is where the decorated function is called
example_function()
