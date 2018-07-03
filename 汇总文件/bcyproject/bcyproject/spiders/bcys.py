# -*- coding: utf-8 -*-
import scrapy
from bcyproject.items import BcyprojectItem
#from urllib.parse import urljoin


class BcysSpider(scrapy.Spider):
    name = 'bcys'
    allowed_domains = ['bcy.net/illust']
    start_urls = ['https://bcy.net/circle/timeline/showtag?since=25101.527&grid_type=flow&sort=hot&tag_id=5798']

    def parse(self, response):
        print(response.status)
        #print(response.body)
        item = BcyprojectItem()
        item['author'] = response.xpath('.//footer[@class="l-clearfix"]/a[@class="name"]/span/text()').extract()[0]
        item['review'] = response.xpath('.//div[@class="post__type_l"]/a/text()').extract()[0]
        item['imgpath'] = response.xpath('//li[@class="cardImage"]/a/@src')
        #print(author,review,imgpath)
        yield item

        pass
