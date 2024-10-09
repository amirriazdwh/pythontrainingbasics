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

