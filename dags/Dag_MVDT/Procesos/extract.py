import requests
import pandas as pd

class BusquedaETL():

    __rangoBusqueda = 0
    __descripcionBusqueda = 0
    __datosAdicionales = {}
    __apiKey = "ad5f78bd71962a39f31814a9c34296f3"

    def __init__(self, buscarPor):
        self.buscarPor = buscarPor

    def __seleccionBusqueda(self):
        if self.buscarPor == 1:
            return self.__busquedaActor()
        else:
            return self.__rangoBusqueda()
    
    def __busquedaActor(self):
        self.__descripcionBusqueda = input("Buscas el actor\n1) Más popular.\n2) Detalles de un autor.\n")
        if (self.__descripcionBusqueda) == "s":
            return 'https://api.themoviedb.org/3/person/popular?api_key={0}&language=en-US&page=1'.format(self.__apiKey)
        else:
            return self.__actorDetalles()

    def __actorDetalles(self):
        self.__datosAdicionales['id'] = input("Ingresa un número este pertenece a un actor: ")
        return ' https://api.themoviedb.org/3/person/{0}?api_key={1}&language=en-US'.format(
            self.__datosAdicionales['id'], self.__apiKey
        )
    
    def __busquedaTendencia(self):
        # self.__descripcionBusqueda = input('¿Qué tendencia buscas?\n1) Todas.\n2) Películas,\n3) Televisión.\n4) Personas.\n')
        print('¿Qué tendencia buscas?\n1) Todas.\n2) Películas,\n3) Televisión.\n4) Personas.\n')
        self.__descripcionBusqueda = "2"
        detalleBusquedaTendencia = {
            "1": 'https://api.themoviedb.org/3/trending/all/{0}?api_key={1}'.format(
                self.__rangoBusqueda, self.__apiKey),
            "2": 'https://api.themoviedb.org/3/trending/movie/{0}?api_key={1}'.format(
                self.__rangoBusqueda, self.__apiKey),
            "3": 'https://api.themoviedb.org/3/trending/tv/{0}?api_key={1}'.format(
                self.__rangoBusqueda, self.__apiKey),
            "4": 'https://api.themoviedb.org/3/trending/person/{0}?api_key={1}'.format(
                self.__rangoBusqueda, self.__apiKey)
        }
        return detalleBusquedaTendencia[self.__descripcionBusqueda]

    def __rangoBusqueda(self):
        # busqueda = input("Selecciona el rango de busqueda.\n1) semanal.\n2) día.\n")
        print("Selecciona el rango de busqueda.\n1) semanal.\n2) día.\n")
        busqueda = "1"
        rango = {
            "1": "week",
            "2": "day"
        }
        self.__rangoBusqueda = rango[busqueda]
        return self.__busquedaTendencia()

    def rawData(self):
        url = self.__seleccionBusqueda()
        print(url)
        response = requests.get(url)
        rawData = pd.DataFrame(response.json()['results'])
        return rawData, self.__descripcionBusqueda
    
    def imprimir(self):
        print("Seleccionaste un tipo de Busqueda: {0}".format(self.buscarPor))


#link = "https://api.themoviedb.org/3/trending/all/week?api_key={0}".format(apiKey)
#print(link)

#print("<<<<<---------------------->>>>>")

#response = requests.get(link)

#print("<<<<<---------------------->>>>>")
## Para extraer Datos en específico
#data = pd.DataFrame(response.json()['results'])[['id', 'original_title', 'original_language', 'title', 'popularity', 'genre_ids']]
#print(data)
## Para todos los datos
#dataRaw = pd.DataFrame(response.json()['results'])