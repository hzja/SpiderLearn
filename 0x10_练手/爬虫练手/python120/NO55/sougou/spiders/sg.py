import scrapy


class SgSpider(scrapy.Spider):
    name = 'sg'
    allowed_domains = ['pic.sogou.com']
    base_url = "https://pic.sogou.com/napi/pc/recommend?key=homeFeedData&category=feed&start={}&len=10"
    start_urls = [base_url.format(0)]

    def parse(self, response):
        json_data = response.json()
        if json_data is not None:
            img_list = json_data["data"]["list"]
            for img in img_list:
                yield {
                    'name': img[0]['title'],
                    'image_urls': [_["originImage"] for _ in img[0]["picList"]],
                }
        else:
            return None
