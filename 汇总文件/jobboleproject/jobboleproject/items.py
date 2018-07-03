# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#目标文件(定义目标数据,理解为一个model)
class JobboleprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    coverimage = scrapy.Field()
    title =scrapy.Field()
    time = scrapy.Field()
    content = scrapy.Field()
    tags = scrapy.Field()
    url = scrapy.Field()
    #图片本地路径
    coverImageLocalpath = scrapy.Field()

    pass
