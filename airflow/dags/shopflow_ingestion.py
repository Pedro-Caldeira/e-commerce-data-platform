
from datetime import datetime

from airflow import DAG
from airflow.providers.ssh.operators.ssh import SSHOperator

PROJECT = (
    r"C:\Users\pblie\OneDrive\Documentos"
    r"\Data_Engineering_WorkSpace\e-commerce_data_platform"
)

with DAG(
    dag_id="shopflow_ingestion",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    tags=["shopflow", "ingestion"],
) as dag:

    ingest_data = SSHOperator(
        task_id="ingest_data",
        ssh_conn_id="shopflow_windows_ssh",
        command=(
            f'cd /d "{PROJECT}" && '
            r'".venv\Scripts\python.exe" -m src.ingestion'
        ),
        cmd_timeout=3600,
    )
