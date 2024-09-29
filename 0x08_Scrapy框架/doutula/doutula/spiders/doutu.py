import scrapy
from doutula.items import DoutulaItem

class DoutuSpider(scrapy.Spider):
    name = 'doutu'
    allowed_domains = ['https://www.doutula.com/']
    Base_url = 'https://www.doutula.com/article/list/?page='
    offset = 1
    start_urls = [ Base_url + str(offset)]

    def parse(self, response):
        pages_list = response.xpath('//div[@class="col-sm-9 center-wrap"]/a')

        for pages in pages_list:
            item = DoutulaItem()
            item['name'] = pages.xpath('./div[@class="random_title"]/text()').extract()[0]
            item['image_path'] = pages.xpath('./@href').extract()[0]
            yield scrapy.Request(item['image_path'],callback=self.crawl,meta={'item':item},dont_filter=True)
    """
    [scrapy.spidermiddlewares.offsite] DEBUG: Filtered offsite request to 'album.zhenai.com': <GET http://album.zhenai.com/u/109625287>,
    二次解析的域名被过滤掉了;
    解决办法：yield scrapy.Request(url=detail_url, meta={'item': item}, callback=self.parse_info, dont_filter=True)
    
    """

    def crawl(self,response):
        item = response.meta['item']
        images = response.xpath('//div[@class="pic-content"]/div[@class="artile_des"]')

        item['image1'] = images[0].xpath('./table/tbody/tr/td/a/img/@src').extract()[0]
        item['image2'] = images[1].xpath('./table/tbody/tr/td/a/img/@src').extract()[0]
        item['image3'] = images[2].xpath('./table/tbody/tr/td/a/img/@src').extract()[0]
        item['image4'] = images[3].xpath('./table/tbody/tr/td/a/img/@src').extract()[0]
        item['image5'] = images[4].xpath('./table/tbody/tr/td/a/img/@src').extract()[0]
        item['image6'] = images[5].xpath('./table/tbody/tr/td/a/img/@src').extract()[0]
        item['image7'] = images[6].xpath('./table/tbody/tr/td/a/img/@src').extract()[0]
        item['image8'] = images[7].xpath('./table/tbody/tr/td/a/img/@src').extract()[0]
        item['image9'] = images[8].xpath('./table/tbody/tr/td/a/img/@src').extract()[0]

        yield item






