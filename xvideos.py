import scrapy


class XvSpider(scrapy.Spider):
    name = 'xvspider'
    start_urls = ['https://www.xvideos.com/c/Teen-13']

    def parse(self, response):
        res = response.text
        yield {'res': res}
