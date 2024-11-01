import scrapy
from tao.items import TaoItem
from scrapy.linkextractors import LinkExtractor


class TaoDataSpider(scrapy.Spider):
    name = 'tao_data'
    allowed_domains = ['taosj.com']
    start_urls = [f'https://www.taosj.com/articles?pageNo={page}' for page in range(1, 124)]

    def parse(self, response):
        link_extractor = LinkExtractor(allow=r'www\.taosj\.com/articles/\d+', restrict_css='a.report-page-list-title')
        links = link_extractor.extract_links(response)
        for l in links:
            item = {
                "url": l.url,
                "text": l.text
            }
            yield item