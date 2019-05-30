import scrapy


class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['http://www.terwergreen.com']

    def parse(self, response):
        res = response.text
        yield {'res': res}
