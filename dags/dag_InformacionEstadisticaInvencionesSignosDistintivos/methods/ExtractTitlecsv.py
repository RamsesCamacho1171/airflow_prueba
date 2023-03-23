import re

class ExtractTitleCSV():
    
    __regExp = "([a-zA-Z0-9]+.csv)"
    __regExpSust = '[0-9]+(.csv)'
    
    def __init__(self, link):
        self.__link = link.lower()
        
    def getTitle(self):
        title = self.__setTitleWithCSV()
        title = self.__setTitleOffCSV(title)
        return title
    
    def __setTitleWithCSV(self):
        return re.findall(self.__regExp, self.__link)[0]
    
    def __setTitleOffCSV(self, title):
        return re.sub(self.__regExpSust, "", title)