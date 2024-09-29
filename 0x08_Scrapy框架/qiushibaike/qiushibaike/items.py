# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QiushibaikeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    photo = scrapy.Field()
    name = scrapy.Field()
    gender = scrapy.Field()
    age = scrapy.Field()
    content = scrapy.Field()
    fun = scrapy.Field()
    comment = scrapy.Field()

