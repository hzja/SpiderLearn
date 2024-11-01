# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LqItem(scrapy.Item):

    # define the fields for your item here like:
    # name = scrapy.Field()
    html_url = scrapy.Field()
    name = scrapy.Field()
    description = scrapy.Field()
    students_count = scrapy.Field()
    fee_type = scrapy.Field()
    picture_url = scrapy.Field()
    id = scrapy.Field()
    label = scrapy.Field()
    online_type = scrapy.Field()
    purchase_seconds_info = scrapy.Field()
    level = scrapy.Field()

