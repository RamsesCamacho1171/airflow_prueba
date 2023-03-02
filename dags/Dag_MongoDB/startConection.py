from datetime import datetime, timedelta
from airflow.decorators import dag, task
import pymongo

from Dag_MongoDB.methods.Prueba_conexion import ConexionMongoDB
from Dag_MongoDB.methods.extract_data_webLinks import ExtractDataWebLinks

default_args = {
    'owner': 'El bichito',
    'retries': 5,
    'retry_delay': timedelta(minutes=1)
}

@dag(
    dag_id = 'Prueba_Connection_Mongo_v01',
    description='Este DAG se encarga de conectar con la base de mongo',
    start_date=datetime(2023, 2, 26),
    schedule_interval='0 15 * * 5'
)
def iniciarConexion():
    
    @task()
    def extractDataPage():
        pagina = ExtractDataWebLinks("https://datos.gob.mx/busca/dataset/informacion-estadistica-de-invenciones-signos-distintivos-y-proteccion-a-la-propiedad-intelectu")
        links = pagina.iniciarExtracciónLinks()
        print(f"\nLos links extraidos son: \n\n{links}\n")
        return links

    @task()
    def subirLink(link):
        con = ConexionMongoDB('testData')
        jsonStructure = 'link'
        con.subirData(jsonStructure, link)

    links = extractDataPage()
    subirLink(links)

con = iniciarConexion()