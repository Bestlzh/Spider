# -*- coding: utf-8 -*-
<<<<<<< HEAD
=======
from scrapy.exceptions import DropItem
import pymysql
import logging
import redis
logger = logging.getLogger(__name__)
>>>>>>> defaf6a73cc03eeb17362791485a9c754889df31

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
<<<<<<< HEAD
from scrapy.exceptions import DropItem
import redis
import pymysql,pymysql.cursors
import logging

logger = logging.getLogger(__name__)
logger.setLevel('DEBUG')


class CheckPipeline(object):
    def process_item(self, item, spider):
        # 检查本科生人数和研究生人数，二者至少有一个有值
        if item['undergraduate_num'] or item['postgraduate_num']:
            return item
        # 否则将该item丢弃
        raise DropItem('Missing undergraduate_num and postgradudate_num in %s' % item['name'])


# class RedisPipeline(object):
#
#     def __init__(self):
#         self.r = redis.Redis()
#
#     def process_item(self, item, spider):
#         self.r.sadd(spider.name, item['name'])
#         logger.info('redis: add %s to list %s' % (item['name'], spider.name))
#         return item

=======


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
>>>>>>> defaf6a73cc03eeb17362791485a9c754889df31

class MysqlPipeline(object):
    def __init__(self):
        self.conn = None
        self.cur = None

<<<<<<< HEAD
    def open_spider(self, spider):
=======
    def open_spider(self,spider):
>>>>>>> defaf6a73cc03eeb17362791485a9c754889df31
        self.conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            passwd='rock1204',
<<<<<<< HEAD
            db='qianmu',
            charset='utf8')
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        cols = item.keys()
        values = [item[col] for col in cols]
        cols = ['`%s`' % key for key in cols]
        # sql = "INSERT INTO `universities` (" + ','.join(cols) + ")" \
        #                                                         "VALUES  (" + ','.join(['%s'] * 8) + ")"


        sql="INSERT INTO `universities`("+','.join(cols)+")VALUES("+','.join(["%s"]*8)+")"
        logger.info(sql)
        self.cur.execute(sql, values)
        self.conn.commit()
        logger.info(self.cur._last_executed)
        logger.info('mysql: add %s to universities' % item['name'])
        return item

    def close_spider(self, spider):
        """当spider被关闭时，这个方法被调用"""
        self.cur.close()
        self.conn.close()
=======
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

>>>>>>> defaf6a73cc03eeb17362791485a9c754889df31
