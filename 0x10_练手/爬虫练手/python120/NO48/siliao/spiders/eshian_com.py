import scrapy
from scrapy.loader import ItemLoader
from siliao.items import SiliaoItem


class EshianComSpider(scrapy.Spider):
    name = 'eshian_com'
    allowed_domains = ['eshian.com']
    start_urls = ['http://www.eshian.com/sat/feedadditive/index']

    def start_requests(self):
        for page in range(1, 23):
            data = {
                'pageN': str(page),
                'eName': "",
                'feedadditiveindustryId': "-1",
            }
            yield scrapy.FormRequest(url=self.start_urls[0], formdata=data, callback=self.parse)

    def parse(self, response):
        target_trs = response.xpath('//tbody/tr')
        for tr in target_trs:
            l = ItemLoader(item=SiliaoItem(), selector=tr)
            l.add_xpath("name", "./td[1]/text()")
            l.add_xpath("s_type", "./td[2]/text()")
            l.add_xpath("scope", "./td[3]/text()")

            yield l.load_item()
