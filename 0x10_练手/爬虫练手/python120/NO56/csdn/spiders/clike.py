import scrapy


class ClikeSpider(scrapy.Spider):
    name = 'clike'
    allowed_domains = ['csdn.net']
    like_url = 'https://blog.csdn.net/phoenix/web/v1/article/like'

    def start_requests(self):
        data = {
            "articleId": "120845464",
        }
        yield scrapy.FormRequest(url=self.like_url, formdata=data, meta={'cookiejar': 'firefox'})

    def parse(self, response):
        print(response.json())
