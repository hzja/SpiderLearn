# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv
from itemadapter import ItemAdapter


class SiliaoPipeline:

    def __init__(self):
        self.f = open("./siliao.csv", "a+", newline="")
        self.fieldnames = ["name", "s_type", "scope"]
        self.writer = csv.DictWriter(self.f, fieldnames=self.fieldnames)
        self.writer.writeheader()

    def process_item(self, item, spider):
        self.writer.writerow(item)

        return item

    def close(self, spider):
        self.f.close()
