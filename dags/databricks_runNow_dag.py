from airflow import DAG
from airflow.providers.databricks.operators.databricks import DatabricksRunNowOperator
from airflow.providers.databricks.operators.databricks import (
    DatabricksSubmitRunOperator,
)
from datetime import datetime

default_args = {"owner": "aairflow-leo"}

with DAG(
    "databricks_runNow_dag",
    start_date=datetime(2023, 11, 7),  # Substitua com a data desejada
    schedule_interval="0 0 * * *",  # Executar diariamente à meia-noite
    default_args=default_args,
) as dag:
    # rodar exemplos para teste
    # rodar um notebook no repositório
    run_existing_repo_job = DatabricksRunNowOperator(
        task_id="run_existing_repo_job",
        databricks_conn_id="databricks_default",
        job_id=827641256663808, #number of the job
        dag=dag,
    )
