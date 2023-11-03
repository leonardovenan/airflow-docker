from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
import pendulum

local_tz = pendulum.timezone("America/Sao_Paulo")

default_args = {
    'owner': 'aairflow-leo',
    'depends_on_past': False,
    'start_date': datetime(2022, 11, 14, 0, 0, 0, tzinfo=local_tz),
    'email': ['leonardovenancio12@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 3,
    'dagrun_timeout': timedelta(minutes=60),  # using 60 min as default
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'airflow_hello'
    ,default_args=default_args
    ,schedule_interval="*/5 * * * *"
    ,max_active_runs=1
)

#Teste de Dags
t9X01 = BashOperator( 
    task_id='airflow_hello_1',
    bash_command="\"D:/Backup PC/Code/airflow-docker/hello.py\"",
    dag=dag)

t9X02 = BashOperator(
    task_id='airflow_hello_2',
    bash_command="\"D:/Backup PC/Code/airflow-docker/hello2.py\"",
    dag=dag)

t9X01 >> t9X02