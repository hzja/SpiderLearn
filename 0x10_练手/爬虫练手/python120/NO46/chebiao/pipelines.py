# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy import Request
from itemadapter import ItemAdapter
from scrapy.pipelines.files import FilesPipeline
from urllib.parse import urlparse
import os
from unrar import rarfile


class ChebiaoPipeline:
    def process_item(self, item, spider):
        path = os.path.join(os.getcwd(), "files", item['file_path'])
        extract_path = os.path.join(os.getcwd(), "files")
        rf = rarfile.RarFile(path, pwd="www.chebiao.net")
        rf.extractall(path=extract_path, pwd="www.chebiao.net")
        return item


class ChebiaoFilePipeline(FilesPipeline):

    def get_media_requests(self, item, info):
        print("--get_media_requests--start-----")
        print("正在下载：", item['file_name'])
        print("--get_media_requests--end-----")
        yield Request(item['file_url'], meta={'title': item['file_name']})

    def file_path(self, request, response=None, info=None):
        print("--file_path--start-----")
        file_name = request.meta.get('title') + ".rar"
        print("--file_path--end-----")
        return file_name

    def item_completed(self, results, item, info):
        print("--item_completed--start-----")
        print(results)
        print("下载完毕")
        file_path = [x['path'] for ok, x in results if ok]
        adapter = ItemAdapter(item)
        adapter['file_path'] = file_path[0]
        print("--item_completed--end--------")
        return item
