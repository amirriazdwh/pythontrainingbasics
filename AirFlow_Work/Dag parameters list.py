""""""
"""
dag_id: A unique identifier for the DAG.

default_args: 
A dictionary of default arguments to be passed to each task in the DAG. Common keys include owner, start_date, 
retries, and retry_delay.

schedule_interval: 
Defines how often the DAG should run. It can be a cron expression, a timedelta object, or special presets 
like @daily, @hourly, etc.

start_date: 
The date and time when the DAG should start running. This should be set to a past date to ensure the DAG runs 
immediately upon installation.

end_date: 
The date and time when the DAG should stop running.

catchup: 
A boolean that determines whether the DAG should catch up on missed runs. Setting this to False ensures only 
the latest run is triggered.

max_active_runs: 
The maximum number of active DAG runs at any given time.

concurrency: 
The maximum number of task instances that can run concurrently within the DAG.

dagrun_timeout: 
The maximum amount of time a DAG run is allowed to take before it is marked as failed.

params: 
A dictionary of parameters that can be passed to tasks at runtime. These parameters can be used to customize 
task behavior.

description: 
A brief description of the DAG’s purpose.

default_view: 
The default view of the DAG in the Airflow UI (e.g., tree, graph, duration, gantt).

orientation: 
The orientation of the DAG in the Airflow UI (e.g., LR for left-to-right, TB for top-to-bottom).

on_failure_callback: 
A function to be called when a DAG run fails.

on_success_callback: 
A function to be called when a DAG run succeeds.

on_retry_callback:
 A function to be called when a task is retried.

render_template_as_native_obj: 
If set to True, templates are rendered as their native types (e.g., integers, lists) instead of strings.


The presence of the start_date parameter alone doesn’t guarantee that a DAG will run immediately upon deployment. Here are the key factors that influence whether a DAG runs immediately:

start_date:
The start_date should be set to a past date. This ensures that the scheduler recognizes the DAG as ready to run.
However, the DAG will not run immediately if the start_date is set to a future date.
schedule_interval:
The schedule_interval determines how often the DAG runs. If set to None, the DAG will not run on a schedule and must be triggered manually.
If set to a specific interval (e.g., @daily), the DAG will run according to that schedule.
catchup:
By default, Airflow will try to “catch up” on all missed runs since the start_date. Setting catchup=False ensures that only the latest run is triggered, avoiding a backlog of runs.
Manual Trigger:
You can manually trigger the DAG using the Airflow UI or CLI to ensure it runs immediately after deployment.
"""