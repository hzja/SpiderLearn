import json
import scrapy


class IqySpider(scrapy.Spider):
    name = 'iqy'
    allowed_domains = ['sns-comment.iqiyi.com']
    start_urls = [
        'https://sns-comment.iqiyi.com/v3/comment/get_comments.action?agent_type=118&business_type=17&content_id=6341622380665900&last_id=']

    def parse(self, response):
        html = response.body
        json_data = json.loads(html)
        yield json_data
        if json_data is not None:
            ret = json_data['data']
            comments = ret['comments']
            _id = comments[-1]['id']
            next = self.start_urls[0] + str(_id)
            
            # 下一接口
            yield scrapy.Request(url=next)

        else:
            return None
