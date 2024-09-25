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
