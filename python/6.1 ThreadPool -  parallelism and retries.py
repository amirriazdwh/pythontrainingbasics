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
When a task raises an exception, it’s caught and stored in the future object. Once you try to access the result via 
future.result(), it raises the exception that was thrown inside the task function. The exception isn’t raised
 immediately when the task fails—it's deferred until you ask for the result.

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




"""
as_completed() will only provide the status of completed (whether successful or failed) tasks, and it doesn't immediately 
handle tasks that are still running.

Key Behavior of as_completed():
Completed tasks (whether successful or failed) are immediately yielded by as_completed().
Running tasks are not yielded until they either complete successfully or fail.
Failed tasks are also considered "completed" from as_completed()'s perspective, as the task has finished its execution, 
albeit unsuccessfully.

Scenario Breakdown:
Given the situation you mentioned (5 tasks: 2 completed, 1 running, 2 failed), here’s what happens:

Tasks 1 and 2:
These tasks are completed (successfully).
They will be yielded first by as_completed() when their execution ends.
Task 3:
Still running.
as_completed() will not yield this task until it finishes running (either successfully or with failure).
Tasks 4 and 5:
Failed during their execution.
as_completed() treats failed tasks as completed because they are no longer running.
When you call future.result() for these failed tasks, an exception is raised, which is caught in the try-except block.
How the Code Handles the Tasks:
Tasks 1 and 2 (Successful Completion):

as_completed() yields the future for these tasks.
Inside the try block, you successfully retrieve the result using future.result():
python
Copy code
result = future.result()  # Success
The status for these tasks will be marked as "Success".
Tasks 4 and 5 (Failure):

as_completed() yields the future for these tasks, even though they failed.
When you attempt future.result(), an exception is raised, and the code enters the except block:
python
Copy code
except Exception as exc:
    logging.error(f"{task.__name__} failed with error: {exc}")
The status for these tasks will be marked as "Failed", and retries will be attempted (if enabled).
Task 3 (Still Running):

as_completed() will not yield Task 3's future until it finishes (either successfully or with failure).
When Task 3 finishes, as_completed() will yield it, and the result or failure will be handled accordingly.
Conclusion:
as_completed() only deals with tasks that have completed, whether they succeeded or failed.
For tasks still running (like Task 3 in your case), as_completed() will only yield their future after they finish execution.
It doesn't differentiate between success and failure directly; that's handled in the logic where you call future.result() 
and catch exceptions.
"""

"""
as_completed(futures)
concurrent.futures.as_completed(futures) is an iterator that yields futures as they complete—whether they succeed or fail. This means the loop will process each task in the order in which they finish (not necessarily in the order they were submitted).

It doesn't wait for all tasks to complete before starting to process each result.
As soon as any task (submitted as a future) finishes, as_completed() yields it, and your code can handle the result or failure.
The Retry Loop Explained
Now, let’s go over the retry logic:

Initial Setup:

The futures dictionary is set up by submitting each task to the ThreadPoolExecutor.
Each task is a function paired with a duration argument, and the future (a placeholder for the result) is mapped to the task and its duration.
python
Copy code
futures = {executor.submit(task, duration): (task, duration) for task, duration in tasks}
Processing Completed Futures: Inside the for loop, each future that finishes (either successfully or with an error) is processed as yielded by as_completed(futures).

The Retry Loop:

python
Copy code
attempt = 0
success = False
while attempt < max_retries:
attempt = 0 initializes the number of attempts.
The while loop ensures that the task will be retried until it either succeeds or the maximum number of retries (max_retries) is reached.
Future Handling (try block):

python
Copy code
result = future.result()  # Try getting the result of the future
logging.info(f"{task.__name__} - Status: Success, Result: {result}")
task_status[task.__name__] = 'Success'
success = True
break  # Exit loop if successful
result = future.result(): Attempts to get the result of the completed task. If the task ran successfully, it will return the result, and the status is logged as "Success".
task_status[task.__name__] = 'Success': The task's status is updated to "Success" in the task_status dictionary.
break: The loop breaks because the task succeeded on this attempt.
Error Handling (except block): If the future raised an exception (i.e., the task failed), it enters the except block:

python
Copy code
attempt += 1
logging.error(f"{task.__name__} - Attempt {attempt} failed with error: {exc}")
The attempt counter is incremented, and the failure is logged.
Retry Mechanism:

python
Copy code
if attempt < max_retries:
    logging.info(f"Retrying {task.__name__} (Attempt {attempt + 1}/{max_retries})")
    future = executor.submit(task, duration)  # Resubmit the task
else:
    logging.error(f"{task.__name__} - Status: Failed after {max_retries} attempts")
    task_status[task.__name__] = 'Failed'
If the number of attempts is still less than max_retries, the task is resubmitted for another attempt using executor.
submit(task, duration). This creates a new future.
If attempt reaches max_retries, the loop stops retrying, and the task is marked as "Failed" in task_status.
Post-Retry Check:

python
Copy code
if not success:
    task_status[task.__name__] = 'Failed'
If, after exhausting all retries, the task has still not succeeded (success remains False), it ensures the task is marked 
as "Failed".

How as_completed() Works with This Loop:
When as_completed(futures) yields a future, the code immediately checks whether that particular future has completed 
successfully or failed.
If the future raises an exception, the task will be retried up to max_retries times.
If all retries fail, it moves on to the next task yielded by as_completed().
This setup ensures that as soon as a task finishes (whether successful or not), the code attempts to handle the result 
and retry it if needed—without waiting for all tasks to complete first. This is efficient and takes advantage of
 parallel execution.
"""