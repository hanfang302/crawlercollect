# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

class BcyprojectPipeline(object):
    def process_item(self, item, spider):
        return item

    def __init__(self):
        self.client = pymongo.MongoClient('localhost', 27017)
        self.db = self.client.tencent  # db = client['tencent']
        self.jobs = self.db.jobs  # jobs = db['jobs']

    def open_spider(self, spider):
        print('spider启动了')

    def process_item(self, item, spider):
        #现将数据转换成一个dict类型，然后把数据放入mongodb
        self.jobs.insert(dict(item))
        print(type(item))
        return item

    def close_spider(self,spider):
        self.client.close()
        print('spider执行结束')
