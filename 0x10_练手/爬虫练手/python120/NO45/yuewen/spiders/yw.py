import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class CbSpider(CrawlSpider):
    name = 'yw'
    allowed_domains = ['write.qq.com']
    start_urls = ['https://write.qq.com/portal/article?filterType=0&page=1']
    # URL 提取规则
    rules = (
        Rule(LinkExtractor(allow=r'.*/portal/content\?caid=\d+&feedType=2&lcid=\d+$'), callback="parse_item"),
        # 寻找下一页 url 地址
        Rule(LinkExtractor(restrict_xpaths="//a[@title='下一页']"), follow=True),
    )

    def parse_start_url(self, response):
        print("---process_results---")
        yield scrapy.Request('https://write.qq.com/portal/article?filterType=0&page=1')

    def process_results(self, response, results):
        print("---process_results---")
        print(results)

    def parse_item(self, response):
        print("---parse_item---")
        print(response.url)
        title = response.css('title::text').extract()[0].strip()
        item = {}
        item["title"] = title
        yield item

    def parse(self):
        pass