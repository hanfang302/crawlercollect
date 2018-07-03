# -*- coding: utf-8 -*-
import scrapy
from baiduliuyou.items import BaiduliuyouItem
from urllib.parse import urljoin

class LiuyousSpider(scrapy.Spider):
    name = 'liuyous'
    allowed_domains = ['lvyou.baidu.com']
    start_urls = ['https://lvyou.baidu.com/zhongguo/']

    def parse(self, response):
        print(response.status)
        item = BaiduliuyouItem()
        #print(response.text)
        item['titlepanel'] = response.xpath('//span[@class="main-name clearfix"]/a[class="clearfix"]/text()').extract_first()
        item['pingfen'] = response.xpath('//div[@class="main-score"]/span(2)/text()').extract_first('')
        item['imglink'] = response.xpath('//span[@class="pic-count"]/a/@href').extract()
        item['content'] = response.xpath('//div[@class="main-desc"]/p[@class="main-desc-p"]/text()').extract_first()
        item['tuijian'] = response.xpath('//div[@class="main-intro"]/text()').extract_first('')
        item['xingcheng'] = response.xpath('//div[@class="title-ul"]/a/@href').extract()

        yield item

        list = response.xpath('//div[@class="main-info-wrap').extract()
        for nodeurl in list:
            fullurl = urljoin('http://lvyou.baidu.com/',nodeurl)
            print(fullurl)
            yield scrapy.Request(fullurl,callback=self.detailPage)
        links = response.xpath('').extract()
        for url in links:
            if 'ly' in url:
                print(url)
                fullurl = urljoin(self.start_urls, url)
                yield scrapy.Request(fullurl, callback=self.parse)


    def detailPage(self,response):
        print(response.status)
        pass
