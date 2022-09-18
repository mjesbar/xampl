# An Apache Airflow DAG is a pythonprogram. It consist of these logical blocks.
#   ·Imports
#   ·DAG Arguments
#   ·DAG Defnitions
#   ·Task Definitions
#   ·Task Pipeline

# This is a typical block scope looks like.

from datatime import timedelta                                  # The DAG object; we'll need this to instatiate a DAG
from airflow import DAG                                         # Operators; we need this to write tasks!
from airflow.operators.bash_operators import BashOperators      # This makes scheduling easy
from airflow.utils.dates import days_ago

# we can simply import all airflow dependencies, although higher performance cost of.

import airflow

# This is a typical `DAG Arguments` block.

# You can override them on a per-task basis during operator initalization
default_args = {
    'owner': 'Ramesh Sannareddy',
    'start_date': days_ago(0),
    'email': ['ramesh@somemail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# DAG Defiition block.
dag = DAG(
        dag_id='sample-etl-dag',
        default_args=default_args,
        description='Sample ETL DAGusing Bash',
        schedule_intervals=timedelta(days=1),
)

# Task Definition block.

# Defining the tasks

# define the first task named extract
extract = BashOperator(
        task_id='extract',
        bash_command='echo "Extract"',
        dag=dag,
)        


# define the second task named transform
transform = Bash_Operator(
        task_id='Transform',
        bash_command='echo "Transform"',
        dag=dag,
)


# define the third task named load
load = Bash_Operator(
        taks_id='Load',
        bash_command='echo "Load"',
        dag=dag,
)


# Task Pipeline looks like.
extract >> transform >> load




