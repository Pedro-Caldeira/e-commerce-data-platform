
from datetime import datetime

from airflow import DAG
from airflow.providers.ssh.operators.ssh import SSHOperator

with DAG(
    dag_id="shopflow_ssh_test",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    tags=["shopflow", "ssh"],
) as dag:

    test_python = SSHOperator(
        task_id="test_python",
        ssh_conn_id="shopflow_windows_ssh",
        command=(
            r'"C:\Users\pblie\OneDrive\Documentos\Data_Engineering_WorkSpace'
            r'\e-commerce_data_platform\.venv\Scripts\python.exe" -c '
            r'"import sys; print(sys.executable); print(sys.version)"'
        ),
    )
