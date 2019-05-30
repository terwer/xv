import scrapy


class QuotesSpider(scrapy.Spider):
    name = "xv"

    def start_requests(self):
        urls = [
            'http://www.terwergreen.com'
            # 'https://www.xvideos.com/c/Teen-13'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # filename = "xvideos.html"
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)
        #
        # item = dict['dfddf':'df']
        item = response.meta
        yield item

        # def start_requests(self):
        #     urls = [
        #         'http://quotes.toscrape.com/page/1/',
        #         'http://quotes.toscrape.com/page/2/',
        #     ]
        #     for url in urls:
        #         yield scrapy.Request(url=url, callback=self.parse)
        #
        # def parse(self, response):
        #     page = response.url.split("/")[-2]
        #     filename = 'quotes-%s.html' % page
        #     with open(filename, 'wb') as f:
        #         f.write(response.body)
        #     self.log('Saved file %s' % filename)
