import re
import requests
from bs4 import BeautifulSoup

class ExtractWebScrapping():

    __headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
    __re = "[^(Balance Nacional de Energía:)]\D+"

    def __init__(self, link):
        self.__link = link

    def getDataWeb(self):
        html = self.__generateHTMLdata()
        data = self.__extractBalanceEnergy(html)
        return html, data

    def __generateHTMLdata(self):
        html = requests.get(self.__link, headers=self.__headers)
        return BeautifulSoup(html.content, 'html.parser')

    def __extractBalanceEnergy(self, html):
        dataSelected = html.find_all(["h2", "h3"], string = re.compile("Balance Nacional de Energía:\D+"))
        print(dataSelected)
        balanceEnergy = re.findall(self.__re, dataSelected[0].string)
        return balanceEnergy[0]