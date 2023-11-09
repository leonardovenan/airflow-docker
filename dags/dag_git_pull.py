from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'airflow',
    'tag': 'github',
    'start_date': datetime(2023, 1, 1),
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'git_pull_dag',
    default_args=default_args,
    schedule_interval=timedelta(minutes=5),  # Agendar conforme necessário
)

git_pull_task = BashOperator(
    task_id='git_pull',
    bash_command='python3  r"D:\Backup PC\Code\airflow-docker\git_pull.py',  # Altere o caminho conforme necessário
    dag=dag,
)
