# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class InterestingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()#标题
    author = scrapy.Field()#作者
    content = scrapy.Field()#内容
    time = scrapy.Field()#时间
    texturl = scrapy.Field()#内容链接
    pageview = scrapy.Field()#浏览量
    imagelink = scrapy.Field()#图片链接


