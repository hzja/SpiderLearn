import scrapy
import json
from falufagui.items import FalufaguiItem
"""可以改进的地方：可以把相应文件的连接也爬取下来；现在只能爬取一页文件，应该实现把所有页面的文件全都爬取下来"""

class InfoSpider(scrapy.Spider):
    name = 'info'
    allowed_domains = ['https://neris.csrc.gov.cn/']
    start_urls = ['https://neris.csrc.gov.cn/falvfagui/rdqsHeader/informationController']

    def parse(self, response):
        pageList = json.loads(response.body)['pageUtil']['pageList']
        for page in pageList:
            item = FalufaguiItem()
            item['file_name']=page['secFutrsLawName']
            item['file_number']=page['fileno']
            item['file_department']=page['lawPubOrgName']
            item['file_date']=page['secFutrsLawVersion']

            yield item