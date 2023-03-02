class Transform():

    __busqueda = {
        '1' : 'todas',
        '2' : 'peliculas',
        '3' : 'televisión',
        '4' : 'personas',
    }

    def __init__(self, dataRaw):
        self.dataRaw = dataRaw['0']
        self.descripcionBusqueda = self.__busqueda[dataRaw['1']]

    def __seleccionDatos(self):
        dataSelection = {
            'todas': ['id', 'title', 'name', 'release_date', ],
            'peliculas': ['id', 'title', 'vote_average', 'release_date'],
            'televisión': ['id', 'name', 'first_air_date', 'vote_average', 'origin_country'],
            'personas': ['id', 'name', 'known_for_department', 'profile_path']
        }
        array = dataSelection[self.descripcionBusqueda]
        return array

    def transformData(self):
        datos = self.__seleccionDatos()
        dataTransform = self.dataRaw[datos]
        return dataTransform