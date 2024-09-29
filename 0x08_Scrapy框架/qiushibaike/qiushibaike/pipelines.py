# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

class QiushibaikePipeline(object):
    def __init__(self):#初始化时调用函数
        self.f = open("qsbk_para.json",'wb')

    def process_item(self, item, spider):#用于处理item
        content = json.dumps(dict(item),ensure_ascii=False) + ",\n"
        self.f.write(content.encode("utf-8"))
        return item

    def close_spider(self,spider):#爬虫关闭时调用
        self.f.close()