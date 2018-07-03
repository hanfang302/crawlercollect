# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

#处理和清洗数据(管道文件)
#数据的保存,持久化
class ScrapytestPipeline(object):
    def process_item(self, item, spider):
        return item
