# -*- coding: utf-8 -*-
import scrapy

#爬虫文件
class TengxunSpider(scrapy.Spider):
    #爬虫的名称,作用:启动爬虫的时候会根据名称找对应的文件
    name = 'tengxun'
    #允许爬取的域,要爬取的链接
    allowed_domains = ['hr.tencent.com']
    #起始的url，也可以是多个
    start_urls = ['https://hr.tencent.com/position.php']

    #解析,response请求返回响应的结果
    def parse(self, response):
        print(response.status)
        #负责解析返回的网页数据
        #是一个二进制文件
        print(response.body)

        #xpath
        #response.xpath()
        #pass
