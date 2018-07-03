# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
import json
class BaiduliuyouPipeline(object):
    def __init__(self):
        self.file = open('hf.json','a+')
        self.client = pymongo.MongoClient('localhost', 27017)
        self.db = self.client.tencent
        self.jobs = self.db.jobs

    def open_spider(self,spider):
        print('启动')

    def process_item(self, item, spider):
        json_str = json.dumps(dict(item),ensure_ascii=False) + '\n'
        self.file.write(json_str)
        return item

    def close_spider(self,spider):
        self.client.close()
        print('结束')

        pass

