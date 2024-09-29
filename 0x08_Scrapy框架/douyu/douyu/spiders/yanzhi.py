import scrapy
import json
from douyu.items import DouyuItem

class YanzhiSpider(scrapy.Spider):
    name = 'yanzhi'
    allowed_domains = ['douyucdn.cn']
    Base_url = 'http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset='
    offset = 0
    start_urls = [Base_url + str(offset)]

    def parse(self, response):
        data_list = json.loads(response.body)['data']
        if data_list == 0:
            return

        for data in data_list:
            item = DouyuItem()
            item["nickname"] = data['nickname']
            item["image"] = data['avatar_mid']
            yield item

            self.offset += 20
            self.url = self.Base_url + str(self.offset)
            yield scrapy.Request(self.url,callback=self.parse)
