from datetime import datetime, timedelta
from airflow.decorators import dag, task

default_args = {
    'owner': 'El michote',
    'retries': 5,
    'retry_delay': timedelta(minutes=1)
}

@dag(
    dag_id = 'dag_TaskFlow_api_v1',
    start_date=datetime(2023, 2, 26),
    schedule_interval='@daily')
def taskFlow_api_etl():

    @task(multiple_outputs=True)
    def getName():
        return {
            'first_name': 'El michote malvado >:v',
            'sur_name': 'Constrictor'
        }
    
    @task()
    def getAge():
        return 25
    
    @task()
    def saludo(first_name, sur_name, age):
        print(f'\nHola, es usted {first_name} {sur_name}, vaya, es un nombre genial!!!!\nMe dijeron que ha cumpido un total de {age} es cierto?\n')

    name = getName()
    age = getAge()
    saludo(name['first_name'], name['sur_name'], age)

dag_saludo = taskFlow_api_etl() 