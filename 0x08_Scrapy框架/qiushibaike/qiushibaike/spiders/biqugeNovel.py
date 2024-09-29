import scrapy
from qiushibaike.items import QiushibaikeItem

class BiqugenovelSpider(scrapy.Spider):
    name = 'biqugeNovel'
    allowed_domains = ['http://www.biquge5200.net/']
    start_urls = ['http://www.biquge5200.net//']

    def parse(self, response):
        novel_list = response.xpath('//div[@class="content "]/ul//li  |  //div[@class="content border"]/ul//li | //div[@class="content "]/div[@class="top"]/dl/dt |  //div[@class="content border"]/div[@class="top"]/dl/dt')

        for novel in novel_list:
            # #创建item字段用于存取item信息
            # item = QiushibaikeItem()
            # #extract()函数将xpath对象转化为Unicode字符串
            # name = novel.xpath('./a/text()').extract()#返回的是一个列表
            href = novel.xpath('./a/@href').extract()[0]
            #
            # item['name'] = name[0]
            # item['href'] = href[0]

            # yield item

            yield scrapy.Request(href,callback=self.crawl_novel,dont_filter=True)

    def crawl_novel(self,response):
        page_list = response.xpath('//div[@id="list"]/dl//dd')
        for page in page_list:
            href = page.xpath('./a/@href').extract()[0]

            yield scrapy.Request(href,callback=self.crawl_page,dont_filter=True)

    def crawl_page(self,response):
        item = NovelcontentItem()
        item['page'] = response.xpath('//div[@class="bookname"]/h1/text()').extract()[0]
        item['content'] = response.xpath('//div[@id="content"]//text()').extract()

        print( item['page'])
        print(item['content'])
        yield item