from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'Pos yo :D',
    'retries': 5,
    'retry_delay': timedelta(minutes=1)
}

with DAG (
    dag_id = 'nuestro primer DAG papu',
    default_args = default_args,
    description = 'Hola mundo vamos a rockear',
    start_date = datetime(2023, 2, 23, 19),
    schedule_interval = '@daily'
) as dag:
    task1 = BashOperator(
        task_id = 'Primera tarea',
        bash_command="echo Hola mundo esta es mi primera tarea"
    )
    task1