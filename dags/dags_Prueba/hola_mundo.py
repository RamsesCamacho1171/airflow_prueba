from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'Pos yo',
    'retries': 5,
    'retry_delay': timedelta(minutes=1)
}

with DAG (
    dag_id = 'nuestro_primer_DAG_papu_v5',
    default_args = default_args,
    description = 'Hola mundo vamos a rockear',
    start_date = datetime(2023, 2, 23, 19),
    schedule_interval = '@daily'
) as dag:
    task1 = BashOperator(
        task_id = 'Primera_tarea',
        bash_command="echo Hola mundo esta es mi primera tarea"
    )
    task2 = BashOperator(
        task_id = 'Segunda_tarea',
        bash_command="echo Hola vatos esta es la segunda tarea"
    )
    task3 = BashOperator(
        task_id = 'Tercera_tarea',
        bash_command="echo Hola vatos esta es la tercera tarea"
    )
    # Comando para hacer que una tarea se ejecute despues de otra tarea.
    # task1.set_downstream(task2)
    # ====================================================================
    # Si necesitas que se ejecuten múltiples tareas después de una haces lo siguiente:
    # task1.set_downstream(task2)
    # task1.set_downstream(task3)
    # OTra forma de hacer lo mismo es:
    # task1 >> task2
    # task1 >> task3
    # Otro método es:
    task1 >> [task2, task3]