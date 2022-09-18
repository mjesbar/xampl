# import the libraries

from datetime import timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

# Defining DAG Arguments

default_args = {
        'owner': 'Ramesh Sannareddy',
        'start_date': days_ago(0),
        'email': ['ramesh@soemail.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=5),
        }

# Defining the DAG

dag = DAG(
        'my-first-dag',
        default_args=default_args,
        description='My first DAG',
        schedule_interval=timedelta(days=1),
        )

# Writing the tasks $

# TASK 1    ~
extract = BashOperator(
        task_id='extract',
        bash_command='cut -d":" -f1,3,6 /etc/passwd > /home/kali/develop/airflow/dags/extracted-data.txt',
        dag=dag,
        )

# TASK 2    ~
transform_and_load = BashOperator(
        task_id='transform',
        bash_command='tr ":" "," < /home/kali/develop/airflow/dags/extracted-data.txt > /home/kali/develop/airflow/dags/transformed-data.csv',
        dag=dag,
        )

# ALL TASKS WRITTEN *

# Task Pipeline $
extract >> transform_and_load
# Task Pipeline created *






