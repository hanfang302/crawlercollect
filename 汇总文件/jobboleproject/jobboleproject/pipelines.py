# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
import scrapy
from scrapy.utils.project import get_project_settings

class jobboleArticleImagePipleline(ImagesPipeline):
    IMAGE_STORE = get_project_settings().get('IMAGE_STORE6')


    #根据图片链接构造一个request请求，给调度器，放在队伍列队里
    def get_media_requests(self, item, info):
        image_url = item('coverImage')

        yield scrapy.Request(image_url)

    #图片任务下载完成之后会执行这个方法
    def item_completed(self, results, item, info):
        #item[self.images_result_field] = [x for ok, x in results if ok]
        print(results)
        for status, value in results:
            if status:
               #return value
               #获取本地存储路径
                image_path = value('path')
                item['coverImageLocalpath'] = image_path
                return item


class JobboleprojectPipeline(object):
    def process_item(self, item, spider):
        return item
