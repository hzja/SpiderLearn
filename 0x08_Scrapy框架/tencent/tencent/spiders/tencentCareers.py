import scrapy
from tencent.items import TencentItem

class TencentcareersSpider(scrapy.Spider):
    name = 'tencentCareers'
    allowed_domains = ['careers.tencent.com']
    base_url = 'https://careers.tencent.com/search.html?index='
    offset = 1
    start_urls = [base_url + str(offset)]

    def parse(self, response):
        job_list = response.xpath('//div[@class="recruit-list"]')
        for job in job_list:
            item = TencentItem()
            jobName = job.xpath('./a/h4/text()').extract()[0]
            company = job.xpath('./a/p/span[1]/text()').extract()[0]
            location = job.xpath('./a/p/span[2]/text()').extract()[0]
            jobType = job.xpath('./a/p/span[3]/text()').extract()[0]
            date = job.xpath('./a/p/span[4]/text').extract()[0]


            print(jobName)
            print(company)
            print(location)
            print(jobType)
            print(date)

