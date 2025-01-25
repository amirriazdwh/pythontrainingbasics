"""
DAG as a Higher-Order Function:
In functional programming, a higher-order function is a function that takes other functions as arguments or returns them as
results.
In Airflow, a DAG (Directed Acyclic Graph) can be seen as a higher-order function in the sense that it organizes and manages
 tasks
 (which can be thought of as functions) and their dependencies. The DAG itself doesn’t perform any operations but defines the
 structure and order in which tasks should be executed.

"""

from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
}

with DAG('example_dag', default_args=default_args, schedule_interval='@daily') as dag:
    start = DummyOperator(task_id='start')
    end = DummyOperator(task_id='end')

    start >> end

"""
Tasks as Lambda Functions:
In functional programming, lambda functions are small, anonymous functions defined with the lambda keyword.
In Airflow, tasks can be thought of as analogous to lambda functions because they are often small, self-contained units of work. 
However, tasks in Airflow are usually defined using operators (e.g., DummyOperator, PythonOperator) rather than anonymous 
functions.
"""

from airflow.operators.python_operator import PythonOperator

def my_task():
    print("Hello, Airflow!")

with DAG('example_dag', default_args=default_args, schedule_interval='@daily') as dag:
    start = DummyOperator(task_id='start')
    task = PythonOperator(task_id='my_task', python_callable=my_task)
    end = DummyOperator(task_id='end')

    start >> task >> end

"""
While Airflow’s design is not purely functional, it does allow for a modular and composable approach to defining workflows, 
which aligns with some functional programming principles1
"""

"""
Certainly! When you define a DAG using the with statement in Apache Airflow, it acts as a context manager. This means that any 
tasks created within this block are automatically added to the DAG. Here’s a breakdown of what happens under the hood:

Context Manager:
The with DAG(...) as dag: statement sets up a context where any tasks defined inside it are automatically associated 
with the dag object.
This is achieved through the __enter__ and __exit__ methods of the DAG class, which manage the context.

Task Creation:
When you create a task like start = DummyOperator(task_id='start'), the task is instantiated and added to the DAG.
Internally, the DummyOperator (or any other operator) calls the dag.add_task(self) method to add itself to the DAG.
Adding Tasks to DAG:
The add_task method of the DAG class is responsible for adding the task to the DAG’s internal task dictionary.

Here’s a simplified version of what happens
"""

class DAG:
    def __enter__(self):
        # Set the current DAG to this instance
        self._previous_dag = _CURRENT_DAG
        _CURRENT_DAG = self
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Restore the previous DAG
        _CURRENT_DAG = self._previous_dag

    def add_task(self, task):
        # Add the task to the DAG's task dictionary
        self.task_dict[task.task_id] = task
        task.dag = self

class BaseOperator:
    def __init__(self, task_id, dag=None):
        self.task_id = task_id
        if dag is None:
            dag = _CURRENT_DAG
        dag.add_task(self)

"""
Task Dependencies:
When you define dependencies using start >> task >> end, it sets the upstream and downstream relationships between tasks.
This is done using the set_downstream and set_upstream methods of the BaseOperator class.
By using the context manager, you simplify the process of associating tasks with a DAG and managing their dependencies. 
This approach makes the code cleaner and more readable

The methods set_downstream and set_upstream are actually part of the BaseOperator class in Apache Airflow, 
but they might not be immediately visible if you’re looking at a simplified or partial view of the class. 
Let’s take a closer look at how these methods work:

set_downstream Method:
This method sets the downstream dependencies for a task. It means that the current task must be completed before the 
downstream task can start.
Here’s a simplified version of how it might look
"""

from airflow.models.baseoperator import BaseOperator

class BaseOperator:
    # Other methods and attributes

    def set_downstream(self, task_or_task_list):
        if isinstance(task_or_task_list, list):
            for task in task_or_task_list:
                self._set_relatives(task, upstream=False)
        else:
            self._set_relatives(task_or_task_list, upstream=False)

    def _set_relatives(self, task_or_task_list, upstream=True):
        if isinstance(task_or_task_list, list):
            for task in task_or_task_list:
                self._set_relative(task, upstream)
        else:
            self._set_relative(task_or_task_list, upstream)

    def _set_relative(self, task, upstream=True):
        if upstream:
            task.set_downstream(self)
        else:
            self.set_upstream(task)
"""
set_upstream Method:
This method sets the upstream dependencies for a task. It means that the current task cannot start until the 
upstream task is completed.
Here’s a simplified version of how it might look:
"""
from airflow.models.baseoperator import BaseOperator

class BaseOperator:
    # Other methods and attributes

    def set_upstream(self, task_or_task_list):
        if isinstance(task_or_task_list, list):
            for task in task_or_task_list:
                self._set_relatives(task, upstream=True)
        else:
            self._set_relatives(task_or_task_list, upstream=True)

"""
Usage in DAGs:
When you use the >> and << operators to set dependencies, these operators internally call the set_downstream and 
set_upstream methods.
Example
"""
start >> task >> end
# This is equivalent to:
start.set_downstream(task)
task.set_downstream(end)

"""
These methods are crucial for defining the execution order of tasks within a DAG. They ensure that tasks are executed in the 
correct sequence based on their dependencies.
"""