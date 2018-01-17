# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


<<<<<<< HEAD
class DongqiudiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
=======
def convert_int(s):
    if isinstance(s,int):
        return s
    if not s:
        return 0
    return int(s.strip().replace(',',''))


# 中国,183CM,22岁,广州恒大淘宝,守门员,67KG,赵天赐(U23),39号,1995-03-20,右脚
class StarItem(scrapy.Item):
    name = scrapy.Field()
    country = scrapy.Field()
    club = scrapy.Field()
    age = scrapy.Field()
    position = scrapy.Field()
    birth = scrapy.Field()
    height = scrapy.Field()
    weight = scrapy.Field()
    sid = scrapy.Field()
    foot = scrapy.Field()



>>>>>>> defaf6a73cc03eeb17362791485a9c754889df31
