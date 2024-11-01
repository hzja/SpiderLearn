# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ChebiaoItem(scrapy.Item):
    file_url = scrapy.Field()
    file_name = scrapy.Field()
    files = scrapy.Field()
    file_path = scrapy.Field()
