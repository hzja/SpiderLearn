# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst


class SiliaoItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(output_processor=TakeFirst())
    s_type = scrapy.Field(output_processor=TakeFirst())
    scope = scrapy.Field(output_processor=TakeFirst())
