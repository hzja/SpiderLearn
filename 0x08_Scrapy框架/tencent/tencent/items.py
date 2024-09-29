# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    jobName = scrapy.Field()
    company = scrapy.Field()
    location = scrapy.Field()
    jobType = scrapy.Field()
    date = scrapy.Field()
    jobResponsibility = scrapy.Field()
    jobRequest = scrapy.Field()

    pass
