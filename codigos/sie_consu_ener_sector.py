from scrapy.item import Item, Field
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from scrapy.crawler import CrawlerProcess
from bs4 import BeautifulSoup as soup

class Tabla(Item):
    descripción=Field()
    unidad=Field()
    f_2019=Field()
    f_2020=Field()
    
class TablaSpider(Spider):
    name="extracion de tabla"
    custom_settings={
        "USER-AGENT":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36",
        'FEED_EXPORT_ENCODING': 'utf-8'
    }
    start_urls=["https://sie.energia.gob.mx/bdiController.do?action=cuadro&cvecua=IE7C02"]

    def parse(self,response):
        sel=Selector(response)
        tabla=sel.xpath('//table[@id="cuadroTable"]')
        celdas = tabla.xpath('.//tr[not(@class)]')
        count=0
        valores=['descripción','f_2019','f_2020']
        for celda in celdas:
            item=ItemLoader(Tabla(),celda)
            if((celda.xpath('./td/@class').get())!="vacio"):
                if(count>0 and count<51):
                    des=celda.xpath(".//td[1]/text()").get().strip()
                    
                    item.add_value("descripción",des)
                    item.add_xpath("f_2019",".//td[3]/text()")
                    item.add_xpath("f_2020",".//td[4]/text()")
                    yield item.load_item()
            
            count+=1

            
            

        

process=CrawlerProcess({
    'FEED_FORMAT':'json',
    'FEED_URI':'19_sie_consu_ener_sector.json'
})

process.crawl(TablaSpider)
process.start()