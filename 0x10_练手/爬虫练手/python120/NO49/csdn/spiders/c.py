import scrapy
from scrapy.selector import Selector
from scrapy.http import HtmlResponse


class CSpider(scrapy.Spider):
    name = 'c'
    allowed_domains = ['csdn.net']
    start_urls = ['https://blog.csdn.net/rank/list/column']

    def parse(self, response):
        response = HtmlResponse(url=self.start_urls[0])

        ret = Selector(response=response).xpath("//title").get()
        print(ret)
