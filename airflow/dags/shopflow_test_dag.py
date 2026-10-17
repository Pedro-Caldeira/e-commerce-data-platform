
import pendulum

from airflow.sdk import dag, task


@dag(
    dag_id="shopflow_test",
    description="Primeiro DAG de teste do projeto ShopFlow",
    schedule=None,
    start_date=pendulum.datetime(2026, 1, 1, tz="UTC"),
    catchup=False,
    tags=["shopflow", "teste"],
)
def shopflow_test():

    @task
    def verificar_inicio():
        print("ShopFlow: o Airflow iniciou o pipeline!")
        return "inicio_ok"

    @task
    def verificar_fim(resultado):
        print(f"Resultado da primeira tarefa: {resultado}")
        print("ShopFlow: teste concluído com sucesso!")

    resultado = verificar_inicio()
    verificar_fim(resultado)


shopflow_test()
