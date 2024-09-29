# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os
import json
"""还有很多bug，暂未完全成功"""
class DoutulaPipeline:
    def process_item(self, item, spider):
        path = 'G:\编程\爬虫\python 爬虫\图片爬取\斗图网' + '\\' + item['name']
        os.mkdir(path)
        # for i in range(1,10):
        with open(path+'\\'+'result.json','w') as f:
            content = json.dumps(dict(item),ensure_ascii=False) + '\n'
            f.write(content)
        f.close()


