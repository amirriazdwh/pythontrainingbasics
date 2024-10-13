"""
DAG as a Higher-Order Function:
In functional programming, a higher-order function is a function that takes other functions as arguments or returns them as results.
In Airflow, a DAG (Directed Acyclic Graph) can be seen as a higher-order function in the sense that it organizes and manages tasks
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
Certainly! When you define a DAG using the with statement in Apache Airflow, it acts as a context manager. This means that any tasks created within this block are automatically added to the DAG. Here’s a breakdown of what happens under the hood:

Context Manager:
The with DAG(...) as dag: statement sets up a context where any tasks defined inside it are automatically associated 
with the dag object.
This is achieved through the __enter__ and __exit__ methods of the DAG class, which manage the context.

Task Creation:
When you create a task like start = DummyOperator(task_id='start'), the task is instantiated and added to the DAG.
Internally, the DummyOperator (or any other operator) calls the dag.add_task(self) method to add itself to the DAG.
Adding Tasks to DAG:
The add_task method of the DAG class is responsible for adding the task to the DAG’s internal task dictionary.
"""