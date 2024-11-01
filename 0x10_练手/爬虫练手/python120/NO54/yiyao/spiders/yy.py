import scrapy
from yiyao.items import YiyaoItem

class YySpider(scrapy.Spider):
    name = 'yy'
    allowed_domains = ['pharmnet.com.cn']
    start_urls = ['http://www.pharmnet.com.cn/product/1111/1/1.html']

    def parse(self, response):
        all_items = response.css('a.green.fb.f13::text').getall()
        for item in all_items:
            ret = YiyaoItem()
            ret["name"] = item
            yield ret
