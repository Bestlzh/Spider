# -*- coding: utf-8 -*-
import scrapy
from dongqiudi.items import StarItem


def filter(html):
    return html.replace('\t','').replace('\r\n','')

class StarSpider(scrapy.Spider):
    name = 'star'
    allowed_domains = ['www.dongqiudi.com']
    start_urls = ['http://www.dongqiudi.com/']

    def __init__(self, max_num=0):
        super(StarSpider, self).__init__()
        # self.logger.info('max crawl pages set is %s' % max_num)
        self.max_num = int(max_num)


    def parse(self, response):

        links = response.xpath('//*[@id="rank_list"]/table/tr/td[2]/a/@href').extract()

        for i, link in enumerate(links):
            if self.max_num and self.max_num <= i:
                print('结束.....................................................')
                break
            request = scrapy.Request(link, callback=self.parse_team)
            yield request

    def parse_team(self, response):
        response = response.replace(body=filter(response.text))
        # self.logger.info(response.url)

        # team_name = response.xpath('//*[@id="con"]/div/div[1]/div[1]/div[2]/div/div/h1/text()').extract()
        # star_name = response.xpath('//*[@id="con"]/div/div[1]/div[3]/table/tbody/tr/td[3]/a/span/text()').extract()
        star_links = response.xpath('//*[@id="con"]/div/div[1]/div[3]/table/tbody/tr/td[3]/a/@href').extract()
        for j,star_link in enumerate(star_links):
            # if self.max_num and self.max_num <= j:
            #     print('球员结束............')
            #     break
            # print(star_link)
            request = scrapy.Request(star_link, callback=self.parse_star)
            print('w我我 我我我欧文o。。。。。。。。。。。。。。。。。。。。。')
            yield request

    def parse_star(self,response):
        response = response.replace(body = filter(response.text))
        star_info_key = response.xpath('//*[@id="con"]/div[1]/div[1]/div[1]/div/ul/li/span[1]/text()').extract()
        star_info_values = response.xpath('//*[@id="con"]/div[1]/div[1]/div[1]/div/ul/li/span[2]/text()').extract()
        item = StarItem(name=response.xpath('//*[@id="con"]/div[1]/div[1]/div[1]/div/div/div/h1/text()').extract_first(),
                    )
        data = dict(zip(star_info_key,star_info_values))
        # 国籍, 身高, 年龄, 俱乐部, 位置, 体重, 姓名, 号码, 生日, 惯用脚
        item['country'] = data.get('国籍','')
        item['club'] = data.get('俱乐部','')
        item['age'] = int(data.get('年龄','')[0:2])
        item['position'] = data.get('位置','')
        item['birth'] = data.get('生日','')
        item['height'] = data.get('身高','')
        item['weight'] = data.get('体重','')
        item['sid'] = int(data.get('号码','')[0:2])
        item['foot'] = data.get('惯用脚','')
        self.logger.info('item %s scraped ' % item['name'])
        print(item)
        yield item
