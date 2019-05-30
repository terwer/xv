import scrapy


class XVSpider(scrapy.Spider):
    name = 'xvspider'
    start_urls = ['https://www.xvideos.com']

    def parse(self, response):
        res = response.text
        yield {'res': res}
