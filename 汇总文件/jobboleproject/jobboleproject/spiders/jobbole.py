# -*- coding: utf-8 -*-
import scrapy
from jobboleproject.items import JobboleprojectItem

class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts']
    #自定义一个setting设置，之运用于当前
    # custom_settings = {
    #     'User-Agent':'...',
    # }

    #自定义一个回调
    def start_requests(self):
        #只会执行一次
        #将其实的url构建成reuest
        for url in self.start_urls:
            yield scrapy.Request(url,callback=self.custom_settings)

    def custom_parse(self):
        print(response.status)

    def parse(self, response):
        #响应状态
        print(response.status)
        #响应体
        print(response.body)
        #scrapy,xpath,css,re
        #用css提取(封面，标题，发布时间，内容，标签，描述,文章详情链接)

        articleList = response.css('#archive .post.floated-thumb')
        for node in articleList:
            item = JobboleprojectItem()
            #选择器对象+.extract_first("没有")获取列表里的第一个值，如果列表没值会显示设置的默认值
            item['coverimage'] = node.css('.post-thumb a img ::attr(href)').extract_first("没有")
            item['title'] = node.css('.archive-title ::text').extract_first("")
            item['time'] = node.css('.post-meta p ::text').re('\d+/\d+/d+')[0]
            item['content'] = node.css('.excerpt p ::text').extract_first("")
            item['tags'] = node.css('.post-meta p a[rel="category tag"] ::text').extract_first("")
            item['url'] = node.css('.archive-title ::attr(href)').extract_first("")

            #交给管道
            yield item



