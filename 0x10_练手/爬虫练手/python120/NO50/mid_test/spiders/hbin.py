import scrapy


class HbinSpider(scrapy.Spider):
    name = 'hbin'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/get']

    def parse(self, response):
        print(response.text)
