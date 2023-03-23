import requests
from bs4 import BeautifulSoup

class ExtractDataWebLinks():

    __headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

    def __init__(self, link):
        self.__link = link

    def iniciarExtracciónLinks(self):
        html = self.__createHTMLdata()
        selectedData = self.__selectHTMLdata(html)
        extractLinkHtml = self.__extractLinks(selectedData)
        return extractLinkHtml

    def __createHTMLdata(self):
        html = requests.get(self.__link, headers=self.__headers)
        return BeautifulSoup(html.content, 'html.parser')
    
    def __selectHTMLdata(self, html):
        htmlDataSelected = html.find_all("a", {"class": "btn btn-primary"})
        return htmlDataSelected
    
    def __extractLinks(self, html):
        links = []
        for link in html:
            if('https' in link['href']):
                links.append(link['href'])
        return links
    

    