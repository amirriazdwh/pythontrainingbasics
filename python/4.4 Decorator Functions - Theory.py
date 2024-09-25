"""
 a decorator can return an object. This is particularly useful when you want to enhance a function’s behavior
 by wrapping it in an object that provides additional methods or properties
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
