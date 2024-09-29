# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FalufaguiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    file_name = scrapy.Field()
    file_number = scrapy.Field()
    file_department = scrapy.Field()
    file_date = scrapy.Field()
    file_url = scrapy.Field()

