import concurrent.futures
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Example function to simulate work
def example_function(duration):
    time.sleep(duration)  # Simulate work with sleep
    return f"Completed in {duration} seconds"

def submit_tasks_in_parallel(tasks, max_workers=5, max_retries=3):
    # Dictionary to store the task and its future
    task_status = {}

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit tasks and store their future objects
        futures = {executor.submit(task, duration): (task, duration) for task, duration in tasks}

        for future in concurrent.futures.as_completed(futures):
            task, duration = futures[future]
            attempt = 0
            while attempt < max_retries:
                try:
                    result = future.result()
                    logging.info(f"{task.__name__} - Status: Success, Result: {result}")
                    break
                except Exception as exc:
                    attempt += 1
                    logging.error(f"{task.__name__} - Attempt {attempt} failed with error: {exc}")
                    if attempt < max_retries:
                        logging.info(f"Retrying {task.__name__} (Attempt {attempt + 1}/{max_retries})")
                        future = executor.submit(task, duration)
                        futures[future] = (task, duration)
                    else:
                        logging.error(f"{task.__name__} - Status: Failed after {max_retries} attempts")

    return task_status

if __name__ == "__main__":
    # Define tasks as a list of tuples (function, duration)
    tasks = [(example_function, 2), (example_function, 4), (example_function, 1)]

    submit_tasks_in_parallel(tasks, max_workers=3, max_retries=3)

import concurrent.futures
import logging

"""
Method #2
"""

def submit_tasks_in_parallel(tasks, max_workers=5, max_retries=3):
    # Dictionary to store the task and its status (Success/Failed)
    task_status = {}

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit tasks and store their future objects
        futures = {executor.submit(task, duration): (task, duration) for task, duration in tasks}

        for future in concurrent.futures.as_completed(futures):
            task, duration = futures[future]
            attempt = 0
            success = False
            while attempt < max_retries:
                try:
                    result = future.result()  # Try getting the result of the future
                    logging.info(f"{task.__name__} - Status: Success, Result: {result}")
                    task_status[task.__name__] = 'Success'
                    success = True
                    break  # Exit loop if successful
                except Exception as exc:
                    attempt += 1
                    logging.error(f"{task.__name__} - Attempt {attempt} failed with error: {exc}")
                    if attempt < max_retries:
                        logging.info(f"Retrying {task.__name__} (Attempt {attempt + 1}/{max_retries})")
                        future = executor.submit(task, duration)  # Resubmit the task
                    else:
                        logging.error(f"{task.__name__} - Status: Failed after {max_retries} attempts")
                        task_status[task.__name__] = 'Failed'

            # Update task status to failed if it exhausted all retries and didn't succeed
            if not success:
                task_status[task.__name__] = 'Failed'

    return task_status

"""
The task will be marked as failed only if the task function raises an exception while executing. However, as_completed() itself does not capture exceptions. Instead, exceptions are raised when you call future.result() to get the result of a task. Let me explain how this works under the hood.

How it Works Under the Hood:
Submitting Tasks to Executor: When you submit a task to the ThreadPoolExecutor (or ProcessPoolExecutor), it creates a future object. A future is a placeholder that represents a task that is being executed concurrently. Whether the task succeeds or fails, the future holds the outcome.

python
Copy code
future = executor.submit(task, duration)
Here, future is like a "promise" that will eventually either:

Contain the result of the task (if it succeeds).
Contain an exception (if it fails).
Task Execution: While the task is running, the future object is in a pending state, meaning it is not yet completed.

If the task completes successfully (i.e., it returns a value or finishes without an exception), the future’s state is set to finished, and it stores the result.
If the task raises an exception, the future's state is still set to finished, but it stores the exception instead of the result.
as_completed(): The as_completed() function iterates over the futures you submitted and yields them as soon as they complete, regardless of whether they succeeded or failed. It doesn't inspect the outcome (success or failure); it simply provides the completed future.

python
Copy code
for future in concurrent.futures.as_completed(futures):
    # This yields futures as they complete, regardless of success or failure.
Accessing the Result with future.result(): Once as_completed() yields a future, you need to check its result using the future.result() method. This is where the exception handling comes into play:

If the task succeeded, future.result() will return the result of the task.
If the task raised an exception during execution, future.result() will raise that same exception when you call it.
python
Copy code
try:
    result = future.result()  # This will raise an exception if the task failed.
except Exception as exc:
    logging.error(f"Task failed with exception: {exc}")
So, future.result() is responsible for:

Returning the result (in case of success).
Raising the exception (in case of failure).
How Exceptions Are Handled:
When a task raises an exception, it’s caught and stored in the future object. Once you try to access the result via future.result(), it raises the exception that was thrown inside the task function. The exception isn’t raised immediately when the task fails—it's deferred until you ask for the result.

Example Scenario:
Let’s say task4() raises an exception (like a ValueError):

python
Copy code
def task4(duration):
    raise ValueError("Something went wrong!")
When you submit task4 to the executor, the future corresponding to task4 will store this exception once the task fails.

as_completed() will yield this future once task4 has finished (even though it failed).
When you call future.result(), it will raise the ValueError that was thrown by task4.
python
Copy code
for future in concurrent.futures.as_completed(futures):
    try:
        result = future.result()  # Raises ValueError for task4
    except Exception as exc:
        logging.error(f"Task failed with exception: {exc}")  # Logs the exception.
Summary:
The task will only fail if an exception is raised inside the task function.
as_completed() yields completed futures (tasks) but doesn’t raise exceptions. It simply passes on completed tasks.
future.result() is where the exception is raised, allowing you to handle it in a try-except block.
If a task succeeded, future.result() returns the result. If it failed, it raises the stored exception
"""

