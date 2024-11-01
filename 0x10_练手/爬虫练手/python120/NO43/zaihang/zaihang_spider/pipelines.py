# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from itemadapter import ItemAdapter
import pymysql


class ZaihangMySQLPipeline:
    def __init__(self, host, port, user, password, db):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.conn = None
        self.cursor = None

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get('HOST'),
            port=crawler.settings.get('PORT'),
            user=crawler.settings.get('USER'),
            password=crawler.settings.get('PASSWORD'),
            db=crawler.settings.get('DB')
        )

    def open_spider(self, spider):
        self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password, db=self.db)

    def process_item(self, item, spider):
        print(item)
        name = item["name"]
        city = item["city"]

        industry = item["industry"]
        price = item["price"]
        chat_nums = item["chat_nums"]
        score = item["score"]

        sql = "insert into users(name,city,industry,price,chat_nums,score) values ('%s','%s','%s',%.1f,%d,%.1f)" % (
            name, city, industry, float(price), int(chat_nums), float(score))
        print(sql)
        self.cursor = self.conn.cursor()  # 设置游标

        try:
            self.cursor.execute(sql)  # 执行 sql
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
