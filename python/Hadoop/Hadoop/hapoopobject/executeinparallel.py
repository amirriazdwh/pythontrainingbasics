import concurrent.futures
import time

# Example function to simulate work
def example_function(duration):
    time.sleep(duration)  # Simulate work with sleep
    return f"Completed in {duration} seconds"

def submit_tasks_in_parallel(tasks):
    # Dictionary to store the task and its future
    task_status = {}

    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit tasks and store their future objects
        futures = {executor.submit(task, duration): task for task, duration in tasks}

        for future in concurrent.futures.as_completed(futures):
            task = futures[future]
            try:
                result = future.result()
                print(f"{task.__name__} - Status: Success, Result: {result}")
            except Exception as exc:
                print(f"{task.__name__} - Status: Failed, Error: {exc}")

    return task_status

if __name__ == "__main__":
    # Define tasks as a list of tuples (function, duration)
    tasks = [(example_function, 2), (example_function, 4), (example_function, 1)]

    submit_tasks_in_parallel(tasks)
