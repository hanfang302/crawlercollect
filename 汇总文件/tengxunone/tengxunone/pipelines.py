# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
import json
#数据管道，负责存储数据和清洗数据
class TengxunonePipeline(object):


    def __init__(self):
        self.file = open('job.json','a+')
        self.client = pymongo.MongoClient('localhost', 27017)
        self.db = self.client.tencent# db = client['tencent']
        # 集合
        self.jobs = self.db.jobs# jobs = db.['jobs']


    def open_spider(self,spider):
        print('spider启动了')

    def process_item(self, item, spider):
        json_str = json.dumps(dict(item),ensure_ascii=False) + '\n'
        self.file.write(json_str)
        # self.jobs.insert(dict(item))
        # print(type(item))
        return item

    def close_spider(self,spider):
        self.client.close()
        print('spider执行结束')

        pass
