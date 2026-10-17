from datetime import datetime

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
    dag_id="shopflow_spark_job",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    tags=["shopflow", "ssh"],
) as dag:

    tasks = []
    for job_name, job_path in JOBS:
        task = SSHOperator(
            task_id=f"transform_{job_name}",
            ssh_conn_id="shopflow_windows_ssh",
            command=(
                f'cd /d "{PROJECT}" && '
                f'"{PYTHON}" "{job_path}"'
            ),
            cmd_timeout=3600,
        )
        tasks.append(task)
    for previous, current in zip(tasks, tasks[1:]):
        previous >> current