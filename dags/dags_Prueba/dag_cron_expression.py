from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'El michote',
    'retries': 5,
    'retry_delay': timedelta(minutes=1)
}

# https://crontab.guru/ Página para editar cron expression

with DAG(
    default_args=default_args,
    dag_id='DAG_con_expresion_cron_v1',
    start_date=datetime(2023,2,26),
    schedule_interval='0 23 7,14,21,28 3,6,9,12 *'
) as dag:
    task1 = BashOperator(
        task_id = 'task1',
        bash_command='echo Expresiones cron asignan el intervalo Dags'
    )
    task1

