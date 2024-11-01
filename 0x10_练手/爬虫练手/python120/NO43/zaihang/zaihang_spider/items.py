# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZaihangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()  # 姓名
    city = scrapy.Field()  # 城市
    industry = scrapy.Field()  # 行业
    price = scrapy.Field()  # 价格
    chat_nums = scrapy.Field()  # 聊天人数
    score = scrapy.Field()  # 评分

