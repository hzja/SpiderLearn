import scrapy
from cncn.items import CncnItem
from urllib import parse
import json


class CnSpider(scrapy.Spider):
    name = 'cn'
    allowed_domains = ['cncn.org.cn']
    start_urls = ['http://www.cncn.org.cn/map/']

    def parse(self, response):
        lis = response.css('ul.sub_maps li')
        for p in lis:
            p_name = p.css('a::text').get()
            p_url_id = p.css('a::attr(href)').re_first('pid=(\d+)')

            yield scrapy.Request(url=f'http://cms.cncn.org.cn/api/map_province_index.php?pid={p_url_id}&callback=',
                                 meta={'p_name': p_name},
                                 callback=self.parse_c)

    def parse_c(self, response):
        p_name = response.meta['p_name']

        map_list = json.loads(response.text)
        cs = map_list["map_list"][0]["province_items"]

        for c in cs.values():
            c_name = c["city_name"]
            c_id = c["city_id"]
            yield scrapy.Request(url=f'http://cms.cncn.org.cn/api/map_city_index.php?cid={c_id}&callback=',
                                 meta={'p_name': p_name, 'c_name': c_name},
                                 callback=self.parse_s)

    def parse_s(self, response):
        p_name = response.meta['p_name']
        c_name = response.meta['c_name']
        map_list = json.loads(response.text)
        map_list = map_list["map_list"][0]
        city_items = None
        if "city_items" in map_list:
            city_items = map_list["city_items"]

        if city_items is not None:
            # 迭代城市
            for d in city_items.values():
                # 如果区下面有街道，获取街道数据
                if "district_items" in d and len(d["district_items"]) > 0:
                    for sub_d in d["district_items"]:
                        d_name = sub_d["community_name"]
                        # 存储数据
                        item = CncnItem()
                        item["p_name"] = p_name
                        item["c_name"] = c_name
                        item["d_name"] = d_name
                        print(item)
                        yield item

        else:
            return None
