# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

#继承crawlspider,crawlspider有继承之spider
class CrawljobboleSpider(CrawlSpider):
    #爬虫名称
    name = 'crawlJobbole'
    #域，制定可以爬取的url必须在这个域下面，不在的自动忽略
    allowed_domains = ['blog.jobbole.com']
    #同样有一个其实url
    start_urls = ['http://blog.jobbole.com/']
    #
    #LinkExtractor一个类
    #restrict_xpaths：制定了xpath路径，那么allow
    #allow:匹配‘满足’括号中‘正则表达式’的url会被提取，如果为空，这全部匹配
    #deny：匹配‘不满足’括号中‘正则表达式’的url会被提取
    #callback:回调函数
    rules = (
        Rule(LinkExtractor(allow=r'.*?/item/bcjdb',deny=r'.*?/notitem/slcnd',restrict_xpaths='//div[@class=a]'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
