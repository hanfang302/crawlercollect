# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TengxunoneItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    jobname = scrapy.Field()#名称
    worklocation = scrapy.Field()#地点
    jobtype = scrapy.Field()#类型
    jobdesc = scrapy.Field()#职责
    jobinfo = scrapy.Field()#要求

    pass
