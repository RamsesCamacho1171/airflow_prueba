import pymongo

class ConexionMongoDB():

    __c = pymongo.MongoClient("mongodb+srv://AlanJaramillo:EiqkqPYrlSSy2Hjl@cluster0.mu7koxd.mongodb.net/?retryWrites=true&w=majority")
    __db=__c['PruebasChicosLoop']
    __collections = {
        "productos": __db['productos'],
        "testData": __db['testData']
    }

    def __init__(self, colection):
        self.__colection = self.__collections[colection]

    def cerrarConexión(self):
        self.__c.close()

    def subirData(self, jsonStructure, data):
        for dato in data:
            self.__colection.insert_one({jsonStructure:dato})
            print(f'Dato subido {jsonStructure}: {dato}')

        



# Debo solucionar este pedo

#from airflow.providers.mongo.hooks.mongo import MongoHook

#hook = MongoHook(mongo_conn_id='mongo')
#client = hook.get_conn()

#try:
#    print(client.server_info())
#except Exception as e:
#    print(e, "Unable to connect to the server.")

#from airflow.models.connection import Connection

#c = Connection(uri="mongodb+srv://AlanJaramillo:EiqkqPYrlSSy2Hjl@cluster0.mu7koxd.mongodb.net/?retryWrites=true&w=majority")

#print(c.login)
#print(c.password)
#print(c.log_info)
#print(c.get_hook)