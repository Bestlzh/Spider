import sys
import json
import logging
from pipelines import MysqlPipleine
import redis

r = redis.Redis()
logging.basicConfig()
logger = logging.getLogger('pipelines')
logger.info('begin to process item.......')

def get_item(spider):
    key = '%s:items' % spider
    item = r.blpop(key)
    if item:
        return json.loads(item[1].decode())

if __name__ == '__main__':
    if len(sys.argv) < 2:
        logger.info('need spider name')
        exit(1)
    spider = sys.argv[1]
    db = MysqlPipleine()
    db.open_spider(spider)
    item = get_item(spider)
    while item:
        db.process_item(item,spider)
        item = get_item(spider)
    db.close_spider(spider)
