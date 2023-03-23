import pandas as pd

class AssingDataEntryRange():
    
    def __init__(self, link):
        self.__link = link
        self.__df = pd.read_csv(link, encoding ='utf-8', delimiter=',', header = None)
        self.__lengthDataFlow = len(self.__df.count(axis=1)) - 1
    
    def mostrarLink(self):
        return self.__link
    
    def getDF(self):
        self.__orderDataFrame()
        return self.__df
    
    def showAllData(self):
        return (
            self.__link,
            self.__lengthDataFlow,
            self.__df
        )
    
    def __orderDataFrame(self):
        self.__deleteTrashDataTail()
        self.__deleteTrashDataHeader()
        self.__dropAllDataMissing()
        self.__resetIndexData()
        self.__df.columns = range(self.__df.columns.size)
        self.__lengthDataFlow = len(self.__df.count(axis=1)) - 1
    
    def __dropAllDataMissing(self):
        self.__df.dropna(axis = 1, how = 'all', inplace = True)
        self.__df.dropna(axis = 0, how = 'all', inplace = True)
    
    def __deleteTrashDataTail(self):
        cicloWhile = self.__lengthDataFlow
        while cicloWhile > 0:
            if pd.isna(self.__df[2][cicloWhile]) == True:
                self.__df.drop([cicloWhile], axis=0, inplace = True)
                cicloWhile = cicloWhile - 1
            else:
                break
    
    def __deleteTrashDataHeader(self):
        self.__df.drop([0, 1, 2], axis=0, inplace = True)
    
    def __resetIndexData(self):
        self.__df.reset_index(drop = True, inplace = True)
        
    