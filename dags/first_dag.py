from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "owner": "aairflow-leo",
}

with DAG(
    dag_id="first_DAG_v0",
    default_args=default_args,
    start_date=datetime(2023, 6, 1),
    schedule="@daily",
    doc_md=__doc__,
):
    start = EmptyOperator(task_id="start")
    hello = BashOperator(task_id="hello", bash_command="echo hello world")
    end = EmptyOperator(task_id="end")

start >> hello >> end
