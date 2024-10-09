""""""
"""
Python offers several techniques for parallel processing, each suited to different types of tasks and scenarios. 
Here’s an overview of the main parallel processing techniques available in Python:

1. Threading
Description: Uses threads to run multiple operations concurrently within the same process.
Best For: I/O-bound tasks (e.g., file I/O, network operations).
Limitations: Limited by the Global Interpreter Lock (GIL) in CPython, which prevents true parallelism for CPU-bound tasks.

Example:
"""

import threading

def print_numbers():
    for i in range(5):
        print(i)

thread = threading.Thread(target=print_numbers)
thread.start()
thread.join()

"""
2. Multiprocessing
Description: Uses separate processes, each with its own Python interpreter and memory space, to achieve true parallelism.
Best For: CPU-bound tasks (e.g., heavy computations).
Limitations: Higher memory usage and more complex inter-process communication (IPC).

Example:
"""

import multiprocessing

def print_numbers():
    for i in range(5):
        print(i)

process = multiprocessing.Process(target=print_numbers)
process.start()
process.join()

"""
3. concurrent.futures.ThreadPoolExecutor
Description: Provides a high-level interface for asynchronously executing callables using a pool of threads.
Best For: Simplifying thread management for I/O-bound tasks.

Example:
"""

import concurrent.futures

def example_function(duration):
    time.sleep(duration)
    return f"Completed in {duration} seconds"

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(example_function, i) for i in range(5)]
    for future in concurrent.futures.as_completed(futures):
        print(future.result())
"""
4. concurrent.futures.ProcessPoolExecutor
Description: Provides a high-level interface for asynchronously executing callables using a pool of processes.
Best For: Simplifying process management for CPU-bound tasks.

Example:
"""

import concurrent.futures

def example_function(duration):
    time.sleep(duration)
    return f"Completed in {duration} seconds"

with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(example_function, i) for i in range(5)]
    for future in concurrent.futures.as_completed(futures):
        print(future.result())
"""
5. Asyncio
Description: Uses an event loop to manage and execute asynchronous tasks, allowing for non-blocking I/O operations.
Best For: I/O-bound tasks that involve waiting (e.g., network requests).
Limitations: Not suitable for CPU-bound tasks as it runs on a single thread.
Example:
Python
"""

import asyncio

async def example_function(duration):
    await asyncio.sleep(duration)
    return f"Completed in {duration} seconds"

async def main():
    tasks = [example_function(i) for i in range(5)]
    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)

asyncio.run(main())

"""
6. Dask
Description: A parallel computing library that scales Python code from multi-core machines to large distributed clusters.
Best For: Handling large datasets and complex computations.

Example:
"""

import dask.array as da

x = da.random.random((10000, 10000), chunks=(1000, 1000))
result = x.mean().compute()
print(result)

"""
7. Ray
Description: A framework for building and running distributed applications, providing simple primitives for parallel and distributed computing.
Best For: Large-scale distributed applications.
Example:
"""

import ray

ray.init()

@ray.remote
def example_function(duration):
    time.sleep(duration)
    return f"Completed in {duration} seconds"

futures = [example_function.remote(i) for i in range(5)]
results = ray.get(futures)
for result in results:
    print(result)

"""
8. Joblib
Description: A library for running Python functions as parallel jobs, often used for machine learning tasks.
Best For: Parallelizing loops and machine learning tasks.
Example:
"""

from joblib import Parallel, delayed

def example_function(i):
    return i * i

results = Parallel(n_jobs=4)(delayed(example_function)(i) for i in range(10))
print(results)

"""
Summary
Threading: Best for I/O-bound tasks with shared memory.
Multiprocessing: Best for CPU-bound tasks with separate memory spaces.
concurrent.futures: Simplifies thread and process management.
Asyncio: Best for non-blocking I/O-bound tasks.
Dask: Scales computations from multi-core to distributed clusters.
Ray: Ideal for large-scale distributed applications.
Joblib: Useful for parallelizing loops and machine learning tasks.
Each technique has its own strengths and is suited to different types of tasks. Choosing the right one depends on the 
specific requirements of your application. If you have any more questions or need further clarification, feel free to ask
"""

"""
The purpose of lock = threading.Lock() in Python is to create a lock object that helps manage access to shared resources 
in a multi-threaded environment. This is crucial for preventing race conditions, which occur when multiple threads try to 
modify shared data simultaneously, leading to unpredictable results.

Here’s a simple example to illustrate:
"""

import threading

# Shared resource
counter = 0
lock = threading.Lock()

def increase(by):
    global counter
    with lock:  # Acquire the lock before modifying the shared resource
        local_counter = counter
        local_counter += by
        counter = local_counter

# Create threads
t1 = threading.Thread(target=increase, args=(10,))
t2 = threading.Thread(target=increase, args=(20,))

# Start threads
t1.start()
t2.start()

# Wait for threads to complete
t1.join()
t2.join()

print(f'The final counter is {counter}')


"""
"""
import queue
import threading
import time

# Function to simulate a worker that processes items from the queue
def worker(q):
    while True:
        item = q.get()  # Get an item from the queue
        if item is None:
            break  # Exit if None is received
        print(f'Processing item: {item}')
        time.sleep(1)  # Simulate work by sleeping for 1 second
        q.task_done()  # Indicate that the task is done

# Create a queue
q = queue.Queue()

# Create and start worker threads
num_worker_threads = 3
threads = []
for i in range(num_worker_threads):
    t = threading.Thread(target=worker, args=(q,))
    t.start()
    threads.append(t)

# Put items into the queue
for item in range(10):
    q.put(item)

# Block until all tasks are done
q.join()

# Stop workers
for i in range(num_worker_threads):
    q.put(None)
for t in threads:
    t.join()

print('All tasks are completed.')
