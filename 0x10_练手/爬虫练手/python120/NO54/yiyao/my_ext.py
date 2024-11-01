from scrapy.exporters import BaseItemExporter


class TXTItemExporter(BaseItemExporter):

    def __init__(self, file, **kwargs):
        super().__init__(dont_fail=True, **kwargs)
        self.file = file

    def export_item(self, item):
        # _get_serialized_fields 方法可以获得 item 所有字段，并返回迭代器
        print(self._get_serialized_fields(item, default_value=''))
        print(self.file)
        for name, value in self._get_serialized_fields(item, default_value=''):
            self.file.write(bytes("\nname:" + value, encoding="utf-8"))
