# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.http import Request
from scrapy.pipelines.images import ImagesPipeline

class SougouPipeline:
    def process_item(self, item, spider):
        return item


class SogouImgPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        name = item["name"]
        for index, url in enumerate(item["image_urls"]):
            yield Request(url, meta={'name': name, 'index': index})

    def file_path(self, request, response=None, info=None):
        # 名称
        name = request.meta['name']
        # 索引
        index = request.meta['index']

        filename = u'{0}_{1}.jpg'.format(name, index)
        print(filename)
        return filename
