# -*- coding: utf-8 -*-
import scrapy
from interesting.items import InterestingItem
from urllib.parse import urljoin

#http://www.u148.net/text/2
class CharacterSpider(scrapy.Spider):
    name = 'character'
    allowed_domains = ['u148.net']
    start_urls = ['http://www.u148.net/text/']

    def parse(self, response):
        print(response.status)
        #print(response.text)
        list = response.xpath('//div[@div="list-content"]/h1/a/@href').extract()
        for nodeurl in list:
            fullurl = urljoin('http://www.u148.net/text/',nodeurl)
            print(fullurl)
            yield scrapy.Request(fullurl,callback=self.detailPage)
        links = response.xpath('//div[@div="pageli"]//a/@href').extract()
        for url in links:
            if 'ues' in url:
                print(url)
                fullurl = urljoin(self.start_urls, url)
                yield scrapy.Request(fullurl, callback=self.parse)


    def detailPage(self,response):
        print(response.status)
        pass

