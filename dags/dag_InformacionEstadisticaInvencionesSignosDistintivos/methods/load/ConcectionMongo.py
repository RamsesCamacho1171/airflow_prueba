import pymongo

class ConexionMongoDB():

    __c = pymongo.MongoClient("mongodb+srv://AlanJaramillo:EiqkqPYrlSSy2Hjl@cluster0.mu7koxd.mongodb.net/?retryWrites=true&w=majority")
    __db=__c['Data']
    __collections = __db['DATA']

    def __init__(self):
        pass

    def cerrarConexión(self):
        self.__c.close()

    def subirData(self, data):
        try:
            self.__collections.insert_many(data)
            print(f'Conjunto de datos subido.')
        except:
            self.__collections.insert_many([data])
            print(f'Conjunto de datos subido.') 
