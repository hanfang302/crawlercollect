# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
import json
import pymysql

# 数据管道，负责存储和清洗数据
class TencentPipeline(object):

    def process_item(self, item, spider):

        return item


    #写入mysql数据库
    def __init__(self):
        # 连接数据库
        self.client = pymysql.Connect('localhost','root','bc123','tencent',3306,charset='utf8')
        #创建游标,执行sql语句
        self.cursor = self.client.cursor()

    def open_spider(self, spider):
        print('spider启动了')

    def process_item(self, item, spider):
        insert_sql = "INSERT INTO jobs(jobname,worklocation,jontype,jobdesc,jobinfo) VALUES (%s,%s,%s,%s,%s)"
        self.cursor.execute(insert_sql,(item['jobname'],item['worklocation'],item['jontype'],item['jobdesc'],item['jobinfo']))
        self.client.commit()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.client.close()
        print('spider执行结束了')

    #写入文件
    def __init__(self):
        # 连接数据库
        self.file = open('job.json','a+')

    def open_spider(self, spider):
        print('spider启动了')

    def process_item(self, item, spider):
        # 现将数据转换成一个dict类型，然后把数据转成json字符串
        json_str = json.dumps(dict(item),ensure_ascii=False) + '\n'
        self.file.write(json_str)
        return item

    def close_spider(self, spider):
        self.file.close()
        print('spider执行结束')

    #写入mongodb数据库
    def __init__(self):
        # 连接数据库
        self.client = pymongo.MongoClient('localhost', 27017)
        self.db = self.client.tencent  # db = client['tencent']
        self.jobs = self.db.jobs  # jobs = db['jobs']

    def open_spider(self,spider):
        print('spider启动了')

    def process_item(self, item, spider):
        #现将数据转换成一个dict类型，然后把数据放入mongodb
        self.jobs.insert(dict(item))
        print(type(item))
        return item

    def close_spider(self,spider):
        self.client.close()
        print('spider执行结束')