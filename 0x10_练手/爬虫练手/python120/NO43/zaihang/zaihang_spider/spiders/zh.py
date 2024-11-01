import scrapy
from zaihang_spider.items import ZaihangItem


class ZhSpider(scrapy.Spider):
    name = 'zh'
    allowed_domains = ['www.zaih.com']
    page = 1  # 起始页码
    url_format = 'https://www.zaih.com/falcon/mentors?first_tag_id=479&first_tag_name=%E5%BF%83%E7%90%86&page={}'  # 模板
    start_urls = [url_format.format(page)]

    def parse(self, response):
        empty = response.css("section.empty")
        if len(empty) > 0:
            return
        mentors = response.css(".mentor-board a")
        for m in mentors:
            item = ZaihangItem()
            name = m.css(".mentor-card__name::text").extract_first()
            city = m.css(".mentor-card__location::text").extract_first()
            industry = m.css(".mentor-card__title::text").extract_first()
            price = self.replace_space(m.css(".mentor-card__price::text").extract_first())
            chat_nums = self.replace_space(m.css(".mentor-card__number::text").extract()[0])
            score = self.replace_space(m.css(".mentor-card__number::text").extract()[1])

            # 格式化数据
            item["name"] = name
            item["city"] = city
            item["industry"] = industry
            item["price"] = price
            item["chat_nums"] = chat_nums
            item["score"] = score

            yield item
        # 再次生成一个请求
        self.page += 1
        next_url = format(self.url_format.format(self.page))

        yield scrapy.Request(url=next_url, callback=self.parse)

    def replace_space(self, in_str):
        in_str = in_str.replace("\n", "").replace("\r", "").replace("￥", "")
        return in_str.strip()
