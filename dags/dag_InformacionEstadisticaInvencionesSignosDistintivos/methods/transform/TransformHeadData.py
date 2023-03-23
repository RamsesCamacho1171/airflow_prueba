import pandas as pd
import re

class TransformHeadData():
    
    __regExp = "[a-zA-Z0-9ñÑáéíóúÁÉÍÓÚ\s]+[^\/\s\n]+"
    
    def __init__(self, df, subTitlesColumns):
        self.__df = df
        self.__subtitlesColumns = subTitlesColumns
        self.__lengthDF = len(df.columns)
        
    def getDF(self):
        self.__transformHeadData()
        return self.__df
    
    def __transformHeadData(self):
        for index in range(self.__subtitlesColumns):
            self.__editHeader(index)
            self.__addDataTitle(index)
            
    def __editHeader(self, column):
        x = 0
        while x < self.__lengthDF:
            if pd.isna(self.__df[x][column]) != True:
                self.__df[x][column] = re.findall(self.__regExp, self.__df[x][column])[0]
            x = x + 1
    
    def __addDataTitle(self, column):
        x = 0
        while x < self.__lengthDF:
            if pd.isna(self.__df[x][column]) == True and x == 0:
                x = x + 1
                continue
            if pd.isna(self.__df[x][column]) == True:
                self.__df[x][column] = self.__df[x - 1][column]
            x = x + 1