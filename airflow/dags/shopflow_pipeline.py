
from datetime import datetime
import pendulum

from airflow import DAG
from airflow.providers.ssh.operators.ssh import SSHOperator

PROJECT = (
    r"C:\Users\pblie\OneDrive\Documentos"
    r"\Data_Engineering_WorkSpace\e-commerce_data_platform"
)

PYTHON = r".venv\Scripts\python.exe"

JOBS = [
    ("customers", r"spark\customers_job.py"),
    ("products", r"spark\products_job.py"),
    ("orders", r"spark\orders_job.py"),
    ("payments", r"spark\payments_job.py"),
]

with DAG(
    dag_id="shopflow_pipeline",
    start_date=pendulum.datetime(2025, 1, 1, tz= "Europe/Lisbon"),
    schedule="30 18 * * *",
    catchup=False,
    tags=["shopflow", "pipeline"],
) as dag:

    ingestion = SSHOperator(
        task_id="ingest_data",
        ssh_conn_id="shopflow_windows_ssh",
        command=(
            f'cd /d "{PROJECT}" && '
            f'"{PYTHON}" -m src.ingestion'
        ),
        cmd_timeout=3600,
    )

    previous_task = ingestion

    for job_name, job_path in JOBS:
        spark_task = SSHOperator(
            task_id=f"transform_{job_name}",
            ssh_conn_id="shopflow_windows_ssh",
            command=(
                f'cd /d "{PROJECT}" && '
                f'"{PYTHON}" "{job_path}"'
            ),
            cmd_timeout=3600,
        )

        previous_task >> spark_task
        previous_task = spark_task
    
    dbt_build = SSHOperator(
        task_id="dbt_build",
        ssh_conn_id="shopflow_windows_ssh",
        command=(
            f'cd /d "{PROJECT}" && '
            f'".venv\Scripts\dbt.exe" build '
            f'--project-dir "dbt\shopflow"'
        ),
        cmd_timeout=3600,
    )

    previous_task >> dbt_build

