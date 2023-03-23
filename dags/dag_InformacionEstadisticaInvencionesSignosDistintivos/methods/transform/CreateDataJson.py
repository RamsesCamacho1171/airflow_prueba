import json

class CreateJson():
    
    def __init__(self, df, columns, title, aditionalData):
        self.__df = df
        self.__columns = columns
        self.__title = title
        self.__aditionalData = aditionalData
        self.__dic = []
        self.__lengthDFcolumns = len(df.columns)
        
    def getDataLessDF(self):
        return f"columnas: {self.__columns}\nTitle: {self.__title}\nAditional Data: {self.__aditionalData}\n"
    
    def getJsonData(self):
        for index in range (1, self.__lengthDFcolumns):
            self.__dic.append(self.__assignFormatJson(index)) 
        return self.__dic
    
    def __assignFormatJson(self, index):
        data = self.__df.loc[:, [0, index]]
        jsonSubtitles = self.__generateJsonDataTitles(data, index)
        indexTitle = data[0][0]
        diccionary = self.__setJsonData(data, jsonSubtitles, indexTitle, index)
        return diccionary
    
    def __generateJsonDataTitles(self, data, position):
        jsonData = dict()
        for index in range(self.__columns):
            title = f"Titulo {index + 1}"
            jsonData[title] = data[position][index]
        return jsonData
    
    def __setJsonData(self, data, jsonSubtitle, indexTitle, index):
        diccionario = []
        for position in range(self.__columns, len(data)):
            jsonData = dict()
            datos = data.loc[position]
            jsonData[indexTitle] = datos[0]
            jsonData["Datos"] = datos[index]
            jsonData["sector"] = self.__aditionalData['sector']
            jsonData["subSector"] = self.__aditionalData['subSector']
            jsonData["categoria"] = self.__title
            jsonData["Institucion"] = self.__aditionalData['Institucion']
            jsonData.update(jsonSubtitle)
            diccionario.append(jsonData)
        return diccionario