import scrapy
from qiushibaike.items import QiushibaikeItem
#用于爬取糗事百科所有的段子，成功
class QsbkParaSpider(scrapy.Spider):
    name = 'qsbk_para'#爬虫名
    allowed_domains = ['qiushibaike.com']#允许爬虫爬取的域名
    start_urls = ['https://www.qiushibaike.com/text/']#爬虫爬取网页的起始网址

    def parse(self, response):
        para_list = response.xpath('//div[@class="col1 old-style-col1"]/div')#定位到段子列表
        for para in para_list:#存储数据
            item = QiushibaikeItem()#定义item为QiushibaikeItem()对象
            item['photo'] = para.xpath('./div[@class="author clearfix"]/a[1]/img/@href').extract_first()#extract_first()函数将xpath对象转变为字符串并且返回列表的第一个值
            item['name'] = para.xpath('./div[@class="author clearfix"]/a[2]/h2/text()').extract_first()
            item['gender'] = para.xpath('./div[@class="author clearfix"]/div/@class').extract_first()
            if item['gender'] == 'articleGender manIcon':
                item['gender'] = 'man'
            elif item['gender'] == 'articleGender womenIcon':
                item['gender'] = 'woman'
            item['content'] = para.xpath('./a/div[@class="content"]/span//text()').extract()#extract()将xpath对象转变为字符串
            item['fun'] = para.xpath('./div[@class="stats"]/span[@class="stats-vote"]//text()').extract()
            item['comment'] = para.xpath('./div[@class="stats"]/span[@class="stats-comments"]/a//text()').extract()

            print(item['photo'])
            print(item['name'])
            print(item['gender'])
            print(item['content'])
            print(item['fun'])
            print(item['comment'])

            yield item#yield 返回数据给引擎，并暂停在这里
        try:
            next_page = response.xpath('//ul[@class="pagination"]/li[last()]/a/@href').extract()[0]#找到下一页的连接
            next_page = "https://www.qiushibaike.com" + str(next_page)
            yield scrapy.Request(next_page,callback=self.parse)#返回请求对象给引擎，继续爬取网页，并将回调函数设置为parse()函数
        except:
            pass

