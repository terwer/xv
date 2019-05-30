# -*- coding: utf-8 -*-

import pymysql
from twisted.enterprise import adbapi
from scrapy.utils.project import get_project_settings  # 导入seetings配置
import time


class DBHelper:
    # 这个类也是读取settings中的配置，自行修改代码进行操作
    def __init__(self):
        settings = get_project_settings()  # 获取settings配置，设置需要的信息

        dbparams = dict(
            host=settings['MYSQL_HOST'],  # 读取settings中的配置
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',  # 编码要加上，否则可能出现中文乱码问题
            cursorclass=pymysql.cursors.DictCursor,
            use_unicode=True,
        )
        # **表示将字典扩展为关键字参数,相当于host=xxx,db=yyy....
        dbpool = adbapi.ConnectionPool('pymysql', **dbparams)
        self.dbpool = dbpool
        print("初始化MySQL数据库完成")

    def connect(self):
        return self.dbpool

    # =====================================
    # 保存数据到数据库表t1
    # =====================================
    def insert_t1(self, item):
        sql = "insert into t1(f1,created_at) values(%s,%s)"
        # 调用插入的方法
        query = self.dbpool.runInteraction(self._conditional_insert_t1, sql, item)
        # 调用异常处理方法
        query.addErrback(self._handle_error)
        print("插入数据")
        return item

    # 写入数据库中
    def _conditional_insert_t1(tx, sql, item):
        item['created_at'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        params = (
            item["f1"],
            item['created_at']
        )
        tx.execute(sql, params)
        print("SQL执行完毕")

    # 错误处理方法
    def _handle_error(failue):
        print('--------------database operation exception!!-----------------')
        print(failue)
