import json
from airflow.models import Variable
from datetime import datetime, timedelta
from airflow.decorators import dag, task

from dag_InformacionEstadisticaInvencionesSignosDistintivos.methods.extract.ExtractLinks import ExtractDataWebLinks
from dag_InformacionEstadisticaInvencionesSignosDistintivos.methods.ExtractTitlecsv import ExtractTitleCSV
from dag_InformacionEstadisticaInvencionesSignosDistintivos.methods.transform.AssignDataEntryRange import AssingDataEntryRange
from dag_InformacionEstadisticaInvencionesSignosDistintivos.methods.SetSubtitlesHeader import SetSubtitlesColumns
from dag_InformacionEstadisticaInvencionesSignosDistintivos.methods.transform.TransformHeadData import TransformHeadData
from dag_InformacionEstadisticaInvencionesSignosDistintivos.methods.transform.CreateDataJson import CreateJson
from dag_InformacionEstadisticaInvencionesSignosDistintivos.methods.load.ConcectionMongo import ConexionMongoDB

default_args = {
    'owner': 'Ulises I. Escobar Díaz',
    'retries': 5,
    'retry_delay': timedelta(minutes=1),
}

aditionalData = {
    "sector": "INNOVACIÓN",
    "subSector": "PATENTES",
    "Institucion": "IMPI",
}

@dag(
    dag_id = 'InformacionEstadisticaSignosDistintivos',
    description='Este DAG se encarga de extraer los datos de esta página web',
    start_date=datetime(2023, 3, 19),
)

def startDag(link):

    @task()
    def extractInformacionEstadisticaInvenciones(link):
        print("=== INICIANDO LA EXTRACCIÓN ===")
        pagina = ExtractDataWebLinks(link)
        links = pagina.iniciarExtracciónLinks()
        print("Los links extraidos son:")
        for link in links:
            print(link)
        print(len(links))
        dataLoad = json.dumps(links)
        order_data_dict = json.loads(dataLoad)
        return order_data_dict
    
    @task()
    def transform(links):
        data = []
        for link in links:
            try:
                print(f"=== INICIAMOS LA TRANSFORMACIÓN DEL LINK {link} ===")
                # Obtenemos la categoria del link
                title = ExtractTitleCSV(link)
                titleCSV = title.getTitle()
                # Empezamos con la manipulación
                orderData = AssingDataEntryRange(link)
                df = orderData.getDF()
                # Comprobamos la cantidad de subtitulos que hay
                subtitlesHead = SetSubtitlesColumns(df)
                columns = subtitlesHead.getSubtitlesColumns()
                # Creamos un Df con la cabecera modificada
                headTransform = TransformHeadData(df, columns)
                dfTransform = headTransform.getDF()
                # Obtenemos los datos extraidos y transformados 
                jsonFormat = CreateJson(dfTransform, columns, titleCSV, aditionalData)
                diccionario= jsonFormat.getJsonData()
                print(f"=== LA TRANSFORMACIÓN DEL LINK {link} HA SIDO EXITOSA ===")
                data.append(diccionario)
            except Exception as e:
                print(f"Error en la extracción de datos\nDel link{link}\n{e}")
        return data
    
    @task()
    def loadData(dataConverted):
        c = ConexionMongoDB()
        for allTransformedData in dataConverted:
            for allData in allTransformedData:
                for data in allData:
                    c.subirData(data)
        c.cerrarConexión()
        print("Operación Exitosa")
    
    
    
    links = extractInformacionEstadisticaInvenciones(link) 
    dataConverted = transform(links)
    loadData(dataConverted)


inciar = startDag("https://datos.gob.mx/busca/dataset/informacion-estadistica-de-invenciones-signos-distintivos-y-proteccion-a-la-propiedad-intelectu")