from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule, Spider
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from bs4 import BeautifulSoup as soup
from scrapy.crawler import CrawlerProcess


class Tabla(Item):
    number=Field()
    ticker=Field()
    company=Field()
    sector=Field()
    industry=Field()
    country=Field()
    market_cap=Field()
    sales=Field()
    income=Field()
    debt_eq=Field()
    gross_m=Field()
    oper_m=Field()
    profit_m=Field()
    

class Tablas(CrawlSpider):
    name="frinviz_general"
    custom_settings={
        "USER-AGENT":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36",
        'FEED_EXPORT_ENCODING': 'utf-8',
    }

    allowed_domains=["finviz.com"]

    start_urls=["https://finviz.com/screener.ashx?v=152&o=-marketcap&c=0,1,2,3,4,5,6,82,78,38,39,40,41"]

    count=21
    while(count<=8281):
        start_urls.append('https://finviz.com/screener.ashx?v=152&o=-marketcap&r='+str(count)+'&c=0,1,2,3,4,5,6,82,78,38,39,40,41')
        count=count+20

    download_delay=1

    # rules=(
    #     Rule(
    #         LinkExtractor(
    #             allow=r'&r=\d+',
    #             restrict_xpaths=['//a[@class="screener-pages"]'],
    #             tags=['a']
    #         ),follow=True , callback='parse'
    #     ),
    # )

    def parse_start_url(self, response):
        sp=soup(response.body)
        tabla=sp.find("table",class_="table-light")
        celdas=tabla.find_all("tr",{"valign":"top"})
        valores= ['','number','ticker','company','sector','industry','country','market_cap','sales','income','debt_eq','gross_m','oper_m','profit_m']
        for celda in celdas:
            item=ItemLoader(Tabla(),response.body)
            count=0
            for valor in celda:
                if(count!=0):
                    item.add_value(valores[count],valor.text)
                count=count+1
            yield item.load_item()

    # def parse(self, response):
    #     sp=soup(response.body)
    #     tabla=sp.find("table",class_="table-light")
    #     celdas=tabla.find_all("tr",{"valign":"top"})
    #     valores= ['','number','ticker','market_cap','dividend','roa','roe','roi','curr_r','quick_r','ltdeb','debt','gross','oper','profit','earnings','price','change','volume']
    #     for celda in celdas:
    #         item=ItemLoader(Tabla(),response.body)
    #         count=0
    #         print(len(celda))
    #         for valor in celda:
    #             if(count!=0):
    #                 item.add_value(valores[count],valor.text)
    #             count=count+1
    #         yield item.load_item()



process=CrawlerProcess({
    'FEED_FORMAT':'json',
    'FEED_URI':'finviz_Capitalización.json'
})

process.crawl(Tablas)
process.start()