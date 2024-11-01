# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class TitlePipeline:
    def process_item(self, item, spider):  # 移除标题中的空格
        if item["title"]:
            item["title"] = item["title"].strip()
            return item
        else:
            return DropItem("异常数据")
