import scrapy
from my_project.items import ArticleItem


class PmSpider(scrapy.Spider):
    name = 'pm'
    allowed_domains = ['www.imspm.com']
    start_urls = ['http://www.imspm.com/chanpin/']

    def parse(self, response):
        # print(response.text)
        list_item = response.css('.list-item-default')
        # print(list_item)
        for i in list_item:
            item = ArticleItem()
            title = i.css('.title::text').extract_first()  # 直接获取文本
            url = i.css('.a_block::attr(href)').extract_first()  # 获取属性值
            author = i.css('.author::text').extract_first()  # 直接获取文本
            # print(title, url, author)
            # 对 item 进行赋值
            item['title'] = title
            item['url'] = url
            item['author'] = author
            yield item
        next = response.css('.nav a:nth-last-child(2)::attr(href)').extract_first()  # 获取下一页链接
        # print(next)
        # 再次生成一个请求
        yield scrapy.Request(url=next, callback=self.parse)
