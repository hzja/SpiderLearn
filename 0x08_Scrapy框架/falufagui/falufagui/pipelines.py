# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv

class FalufaguiPipeline:
    def __init__(self):
        self.f = open('test.csv','w',newline='')
        self.writer = csv.writer(self.f)
        self.writer.writerow(['文件名','文件号','发文单位','发文日期'])

    def process_item(self, item, spider):
        self.writer.writerow([item['file_name'],item['file_number'],item['file_department'],item['file_date']])


def close_spider(self,spider):
        self.f.close()
