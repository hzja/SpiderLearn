import json
import scrapy

from lq.items import LqItem


class LanqiaoSpider(scrapy.Spider):
    name = 'lanqiao'
    allowed_domains = ['lanqiao.cn']

    def start_requests(self):
        url_format = 'https://www.lanqiao.cn/api/v2/courses/?page_size=20&page={}&include=html_url,name,description,students_count,fee_type,picture_url,id,label,online_type,purchase_seconds_info,level'
        for page in range(1, 34):
            url = url_format.format(page)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        json_data = json.loads(response.text)
        for ret_item in json_data["results"]:
            item = LqItem(**ret_item)
            yield item
