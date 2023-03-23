import pandas as pd

class SetSubtitlesColumns():
    
    def __init__(self, df):
        self.__df = df
        self.__subtitlesColumns = 0
    
    def getSubtitlesColumns(self):
        self.__setSubTitlesColumns()
        return self.__subtitlesColumns
    
    def __setSubTitlesColumns(self):
        nanValue = self.__checkNaNvalue()
        if nanValue == True:
            self.__nanTitlePrincipal()
        else:
            self.__notNanTitlePrincipal()
        
    def __checkNaNvalue(self):
        if pd.isna(self.__df[0][self.__subtitlesColumns]) == True:  
            self.__subtitlesColumns = self.__subtitlesColumns + 1
            return True
        if self.__subtitlesColumns == 0:
            self.__subtitlesColumns = self.__subtitlesColumns + 1
        return False
    
    def __nanTitlePrincipal(self):
        nanValue = self.__checkNaNvalue()
        while nanValue == True:
            nanValue = self.__checkNaNvalue()
            
    def __notNanTitlePrincipal(self):
        nanValue = self.__checkNaNvalue()
        if nanValue == False:
            self.__subtitlesColumns = 1
            return
        while nanValue == True:
            nanValue = self.__checkNaNvalue()