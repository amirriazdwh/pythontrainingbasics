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


"""
The purpose of this code block:

python
Copy code
# Optionally join the threads (to ensure all worker threads have finished)
for thread in threads:
    thread.join()
is to ensure that all worker threads have fully finished their execution before the main program proceeds.

Detailed Explanation:
Thread Management:

When you start a thread with thread.start(), the thread runs concurrently (in parallel with the main thread and other threads). 
The main program doesn't wait for the worker threads to finish unless you explicitly tell it to.
Purpose of thread.join():

The thread.join() method is used to block the main thread (or the thread that calls join()) until the specific worker thread 
has finished executing.
By calling join() on each thread, you ensure that the main program will wait for all worker threads to complete their tasks 
before continuing further execution.
Why is this Important?

Synchronization: If you do not call thread.join(), the main thread might finish its execution (and potentially terminate 
the entire program) while the worker threads are still running. This can lead to incomplete task processing or program 
termination before the background threads complete their work.
Resource Management: Joining the threads ensures that all resources used by those threads (e.g., memory, open files, etc.) 
are properly cleaned up before the program exits.
Clean Program Exit: By using join(), you guarantee that all threads have finished their work and there are no lingering 
background threads when the program exits.
Example Without thread.join():
python
Copy code
import threading
import time

def worker():
    print("Worker started")
    time.sleep(2)
    print("Worker finished")

threads = []
for i in range(3):
    thread = threading.Thread(target=worker)
    thread.start()
    threads.append(thread)

# Without thread.join(), the main thread won't wait for the worker threads
print("Main thread finished")
In this example:

The main thread will print "Main thread finished" before the worker threads have finished.
If the program terminates after the main thread finishes, the worker threads may get terminated abruptly before completing 
their tasks.
Example With thread.join():
python
Copy code
import threading
import time

def worker():
    print("Worker started")
    time.sleep(2)
    print("Worker finished")

threads = []
for i in range(3):
    thread = threading.Thread(target=worker)
    thread.start()
    threads.append(thread)

# Now we join the threads, waiting for them to finish
for thread in threads:
    thread.join()

print("Main thread finished after all worker threads")
In this example:

The thread.join() ensures that the main thread waits for all worker threads to finish before printing "Main thread finished."
This guarantees that all worker threads have completed their tasks, and the program exits cleanly.
In the Context of Your Code:
In your queue-based multi-threaded program:

The main thread waits for all tasks in the queue to be processed using task_queue.join(). This ensures all tasks are done.

The for thread in threads: thread.join() ensures that all worker threads (not just the queue) have finished executing completely 
before the program ends. This includes any cleanup or final tasks that threads may be performing after marking their tasks as 
complete in the queue.

Summary:
thread.join() is used to ensure that the main thread (or any calling thread) waits for each worker thread to finish its work.
It's important for ensuring clean, synchronized execution, where all background threads have completed their tasks before the 
main program proceeds to exit or move to the next steps.
"""