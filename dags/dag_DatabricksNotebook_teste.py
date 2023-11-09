from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.contrib.operators.databricks_operator import DatabricksRunNowOperator

default_args = {
    'owner': 'airflow',
    'tag': 'Databricks',
    'start_date': datetime(2023, 1, 1),
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    "databricks_notebook_test",
    start_date=datetime(2023, 11, 7),  # Substitua com a data desejada
    schedule_interval="0 0 * * *",  # Executar diariamente à meia-noite
    default_args=default_args,
) as dag:
    # rodar exemplos para teste
    # rodar um notebook no repositório
    run_existing_repo_job = DatabricksRunNowOperator(
        task_id="run_databricks_notebook",
        databricks_conn_id="databricks_default",
        job_id=951540597170272, #number of the job
        dag=dag,
    )