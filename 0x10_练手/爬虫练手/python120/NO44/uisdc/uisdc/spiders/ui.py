import scrapy

from scrapy.loader import ItemLoader
from uisdc.items import UisdcItem


class UiSpider(scrapy.Spider):
    name = 'ui'
    allowed_domains = ['www.uisdc.com']
    start_urls = ['https://www.uisdc.com/archives']
    custom_settings = {
        "ROBOTSTXT_OBEY": False
    }

    def parse(self, response):
        items = response.xpath('//div[@id="archive_list"]/div/div[1]/div[1]/div[contains(@class,"item-article")]')
        for i in items:
            l = ItemLoader(item=UisdcItem(), selector=i)
            l.add_xpath('title', ".//h2[@class='item-title']/a/text()")
            l.add_xpath('author', ".//h3[@class='meta-name']/text()")
            l.add_xpath('tag', ".//div[@class='meta-tag']/a/text()")
            ret = l.load_item()
            # print(ret)
            yield ret
