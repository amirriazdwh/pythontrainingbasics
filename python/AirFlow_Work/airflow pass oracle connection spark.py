from airflow import DAG
from airflow.providers.oracle.hooks.oracle import OracleHook
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('oracle_to_spark_dag', default_args=default_args, schedule_interval='@daily')

def get_oracle_conn_details():
    oracle_hook = OracleHook(oracle_conn_id='my_oracle_conn')
    conn = oracle_hook.get_connection()
    return {
        'host': conn.host,
        'login': conn.login,
        'password': conn.password,
        'schema': conn.schema
    }

get_conn_details_task = PythonOperator(
    task_id='get_oracle_conn_details',
    python_callable=get_oracle_conn_details,
    dag=dag
)

spark_task = SparkSubmitOperator(
    task_id='run_spark_job',
    application='/path/to/your/spark/application.py',
    application_args=[
        '--oracle-host', "{{ task_instance.xcom_pull(task_ids='get_oracle_conn_details')['host'] }}",
        '--oracle-login', "{{ task_instance.xcom_pull(task_ids='get_oracle_conn_details')['login'] }}",
        '--oracle-password', "{{ task_instance.xcom_pull(task_ids='get_oracle_conn_details')['password'] }}",
        '--oracle-schema', "{{ task_instance.xcom_pull(task_ids='get_oracle_conn_details')['schema'] }}"
    ],
    dag=dag
)

get_conn_details_task >> spark_task



from pyspark.sql import SparkSession
import argparse

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument('--oracle-host', required=True)
parser.add_argument('--oracle-login', required=True)
parser.add_argument('--oracle-password', required=True)
parser.add_argument('--oracle-schema', required=True)
args = parser.parse_args()

# Initialize Spark session
spark = SparkSession.builder \
    .appName("OracleToSpark") \
    .getOrCreate()

# JDBC URL for Oracle
jdbc_url = f"jdbc:oracle:thin:@{args.oracle_host}:1521/{args.oracle_schema}"

# Read data from Oracle
df = spark.read \
    .format("jdbc") \
    .option("url", jdbc_url) \
    .option("dbtable", "your_table_name") \
    .option("user", args.oracle_login) \
    .option("password", args.oracle_password) \
    .load()

# Perform your transformations and actions
df.show()
