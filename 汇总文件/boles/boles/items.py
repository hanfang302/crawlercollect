# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BolesItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()#标题
    time = scrapy.Field()#时间
    url = scrapy.Field()#地址
    url_object_id = scrapy.Field()#id
    image_url = scrapy.Field()#图片
    image_patch = scrapy.Field()#图片地址
    numbers = scrapy.Field()#点赞数量
    bookmarks = scrapy.Field()#收藏数
    comment = scrapy.Field()#评论量
    content = scrapy.Field()#内容
    tags = scrapy.Field()#标签

    pass
