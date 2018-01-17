# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
<<<<<<< HEAD

=======
import pymysql
import logging
from scrapy.exceptions import DropItem
logger = logging.getLogger(__name__)
logger.setLevel('DEBUG')
>>>>>>> defaf6a73cc03eeb17362791485a9c754889df31

class DongqiudiPipeline(object):
    def process_item(self, item, spider):
        return item
<<<<<<< HEAD
=======


class CheckPipeline(object):
    def process_item(self,item,spider):
        if 'age' in item or 'id ' in item:
            return item
        raise DropItem('miss name and id in %s' % item)


class MysqlPipleine(object):
    def __init__(self):
        self.conn = None
        self.cur = None

    def open_spider(self,spider):
        self.conn = pymysql.connect(
            host = '127.0.0.1',
            port = 3306,
            user = 'root',
            password = 'rock1204',
            db = 'dongqiudi',
            charset = 'utf8'
        )
        self.cur = self.conn.cursor()

    def process_item(self,item,spider):
        cols = item.keys()
        values = [item[col] for col in cols]
        cols = ['`%s`' % col for col in cols]
        sql = "INSERT INTO `star` (" + ','.join(cols) + ")" + " VALUES (" + ','.join(['%s'] * 10) + ")"
        self.cur.execute(sql,values)
        logger.info(self.cur._last_executed)
        self.conn.commit()
        return item
    def close_spider(self,spider):
        self.cur.close()
        self.conn.close()

>>>>>>> defaf6a73cc03eeb17362791485a9c754889df31
