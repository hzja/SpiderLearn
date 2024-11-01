# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field
from scrapy.loader.processors import MapCompose, TakeFirst


def ext(value):
    return "新闻：" + value


class UisdcItem(Item):
    # define the fields for your item here like:
    title = Field(
        input_processor=MapCompose(ext),
        output_processor=TakeFirst()
    )
    author = Field(output_processor=TakeFirst())
    tag = Field(output_processor=TakeFirst())
