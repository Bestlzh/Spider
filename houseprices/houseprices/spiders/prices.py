# -*- coding: utf-8 -*-
import scrapy
from houseprices.items import HousepricesItem

def filter(html):
    return html.replace('\t','').replace('\r\n','')


class PricesSpider(scrapy.Spider):
    name = 'prices'
    allowed_domains = ['www.numbeo.com']
    start_urls = ['https://www.numbeo.com/property-investment/rankings_current.jsp']


    def parse(self, response):
        response = response.replace(body=filter(response.text))
        links = response.xpath('//*[@id="t2"]/tbody/tr/td[2]/a/@href').extract()
        for link in links:
            request = scrapy.Request(link+'?displayCurrency=USD', callback=self.parse_price)
            yield request


    def parse_price(self, response):
        response = response.replace(body=filter(response.text))
        city_name = response.xpath('/html/body/div/aside[2]/div/span/span[1]/text()').extract()
        city_centre = response.xpath('/html/body/div/table//tr[7]/td[2]/text()').extract()
        out_centre = response.xpath('/html/body/div/table//tr[8]/td[2]/text()').extract()
        # print(city_name, out_centre, city_centre)
        item = HousepricesItem(
            city_name=city_name[0], in_centre=city_centre[0][:-2], out_centre=out_centre[0][:-2]
            )
        yield item



