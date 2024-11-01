import scrapy
from chebiao.items import ChebiaoItem
from urllib.parse import urlparse


class CbSpider(scrapy.Spider):
    name = 'cb'
    allowed_domains = ['chebiao.net']
    start_urls = ['http://www.chebiao.net/domestic.php', 'http://www.chebiao.net/es.php',
                  'http://www.chebiao.net/jsk.php', 'http://www.chebiao.net/other.php',
                  'http://www.chebiao.net/famous.php']

    def parse(self, response):
        down_url = "http://www.chebiao.net/download.php"
        dds = response.xpath("//div[@class='box2']/dl/dd")
        for dd in dds:
            item = ChebiaoItem()
            name = dd.xpath('./a/text()').extract()[0]
            url = dd.xpath('./a/@href').extract()[0]
            url = down_url + "?" + urlparse(url).query
            item['file_name'] = name
            item['file_url'] = url

            yield item
