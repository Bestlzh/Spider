# -*- coding: utf-8 -*-
from scrapy.exceptions import DropItem
import pymysql
import logging
import redis
logger = logging.getLogger(__name__)

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class QianmuPipeline(object):
    def process_item(self, item, spider):
        return item


class CheckPipeline(object):
    def process_item(self,item,spider):
        if 'undergrate_num' in item or 'postgrate_num' in item:
            return item
        raise DropItem('miss undergrate_num and postgrate_num in %s ' %item)

class RedisPipeline(object):
    def __init__(self):
        self.r = redis.Redis()
    def process_item(self,item,spider):
        self.r.sadd(spider.name,item['name'])
        logger.info('redis: add %s to list %s' % (item['name'], spider.name))
        return item

class MysqlPipeline(object):
    def __init__(self):
        self.conn = None
        self.cur = None

    def open_spider(self,spider):
        self.conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            passwd='rock1204',
            db = 'qianmu',
            charset='utf8')
        self.cur = self.conn.cursor()

    def process_item(self,item,spider):
        cols = item.keys()
        values = [item[col] for col in cols]
        cols = ['`%s`' % col for col in cols]
        sql = "INSERT INTO `universities` (" + ','.join(cols) + ")" +\
                " VALUES (" + ','.join(['%s'] * 8) + ")"
        logger.info(sql)
        self.cur.execute(sql,values)
        logger.info(self.cur._last_executed)
        self.conn.commit()
        return item

    def close_spider(self,spider):
        self.cur.close()
        self.conn.close()

