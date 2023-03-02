
from Dag_MVDT.Procesos.extract import BusquedaETL
from Dag_MVDT.Procesos.transform import Transform

from datetime import datetime, timedelta
from airflow.decorators import dag, task

default_args = {
    'owner': 'El bichito',
    'retries': 5,
    'retry_delay': timedelta(minutes=1)
}

@dag(
    dag_id = 'Prueba_ETL_MVDT_v1',
    description='Este DAG se encarga de extraer información de películas',
    start_date=datetime(2023, 2, 26),
    schedule_interval='0 15 * * 5'
)
def iniciarBusqueda(busqueda):
    
    @task(multiple_outputs=True)
    def extract(busqueda):
        print(f'\n{busqueda}\n')
        print("\nInicia la EXTRACCIÓN\n")
        etl = BusquedaETL(buscarPor = busqueda)
        rawData = etl.rawData()
        print(rawData)
        print('FIN')
        return {
            '0': rawData[0],
            '1': rawData[1]
        }

    @task()
    def transform(rawData):
        print("\nInicia la TRANSFORMACIÓN \n")
        transform = Transform(dataRaw = rawData)
        transformacion = transform.transformData()
        return transformacion
        ##ti.xcom_push(key='transformData', value=transformacion)

    @task
    def load(transformData):
        print("Inicia la CARGA")
        print("Los datos transformados son:\n")
        print(transformData)

    rawData = extract(busqueda)
    transforData = transform(rawData)
    load = load(transforData)

busqueda = iniciarBusqueda(busqueda = 2)