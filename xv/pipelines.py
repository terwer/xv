# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from xv.db import DBHelper


class XvPipeline(object):
    # 连接数据库
    def __init__(self):
        self.db = DBHelper()

    def process_item(self, item, spider):
        # 插入数据库
        print('开始处理数据..')
        print(item)
        item["f1"] = '测试数据啊'
        self.db.insert_t1(item)
        print('数据处理完成.')
        return item
