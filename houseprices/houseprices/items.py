# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HousepricesItem(scrapy.Item):
    city_name = scrapy.Field()
    out_centre = scrapy.Field()
    in_centre = scrapy.Field()
