from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import sys


default_args = {
    'owner': 'El bichito',
    'retries': 5,
    'retry_delay': timedelta(minutes=1)
}

def funcion(ti, carrera):
    nombre = ti.xcom_pull(task_ids='obtener_datos', key='nombre')
    apellido_p = ti.xcom_pull(task_ids='obtener_datos', key='apellido_p')
    print("#################################")
    print("#################################")
    print("#################################")
    print(sys.path)
    print("#################################")
    print("#################################")
    print("#################################")
    print("Esta es la forma de usar variables pops")
    print(f"\nNombre: {nombre}\nApellido paterno: {apellido_p}\nCarrera: {carrera}\n")

def sacarVariables(ti):
    ## el comando es push para insertarlo en el entorno ti
    ti.xcom_push(key='nombre', value='Hunter')
    ti.xcom_push(key='apellido_p', value='Himura')

with DAG(
    default_args=default_args,
    dag_id='Primer_DAG_con_python_v3',
    description='Primer DAG usando python papu :D',
    start_date=datetime(2023, 2, 23),
    schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id = 'Primer_task_con_python',
        python_callable=funcion,
        op_kwargs={
            'carrera': 'Sistemas', 
        }
    )

    task2 = PythonOperator(
        task_id = 'Segunda_task',
        python_callable=sacarVariables
    )
    task2 >> task1
