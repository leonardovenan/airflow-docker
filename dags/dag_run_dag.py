from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

with DAG(
    "dag_run_dag",
    description="Task run Dag",
    schedule_interval=None,
    start_date=datetime(2023, 3, 5),
    catchup=False,
) as dag:
    task1 = BashOperator(task_id="tsk1", bash_command="sleep 3")
    task2 = BashOperator(task_id="tsk2", bash_command="sleep 3")

    task1 >> task2
   
