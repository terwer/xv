import scrapy


class XvSpider(scrapy.Spider):
    name = 'xvspider'
    start_urls = ['https://xvideos.com']

    def parse(self, response):
        res = response.text
        yield {'res': res}
