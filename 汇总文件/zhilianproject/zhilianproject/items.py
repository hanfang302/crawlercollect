# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhilianprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    jobname = scrapy.Field()#名称
    salary = scrapy.Field()#薪资
    time = scrapy.Field()#时间
    desc = scrapy.Field()#描述
    address = scrapy.Field()#地址
    company = scrapy.Field()#公司名称

