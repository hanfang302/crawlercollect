# -*- coding: utf-8 -*-
import scrapy
import re
from tengxuntwo.items import *
from urllib.parse import urljoin


# class TengxunsSpider(scrapy.Spider):
#     name = 'tengxuns'
#     allowed_domains = ['hr.tencent.com']
#     start_urls = ['https://hr.tencent.com/position.php']
#
#     #解析每一页的数据，response请求返回的响应结果
#     def parse(self, response):
#         print(response.status)
#         print(response.body)
#         #xpath,css,re(response.xpath(''))
#         job_even = response.xpath('//tr[@class="even"]/td[@class="1 square"]/a/@href').extract()
#         job_odd = response.xpath('//tr[@class="odd"]/td[@class="1 square"]/a/@href').extract()
#         print(job_even,job_odd)
#         #总的职位链接
#         jobs = job_even+job_odd
#
#         for nodeurl in jobs:
#             fullurl = urljoin('https://hr.tencent.com/position.php',nodeurl)
#             print((fullurl))
#
#             yield  scrapy.Request(fullurl,callback=self.parseJobDetail)
#
#
#
#     def parseJobDetail(self,response):
#         print(response.status)
#         item = TengxuntwoItem()
#         #目标数据：职位名称，地点，类别，职责，要求
#         item['jobname'] = response.xpath('//td[@id="sharetitle"]/text()').extract()[0]
#         item['worklocation'] = response.xpath('//tr[@class="c bottomline"]/td[1]/text()').extract()[0]
#         item['jobtype'] = response.xpath('//tr[@class="c bottomline"]/td[2]/text()').extract()[0]
#         item['jobdesc'] = response.xpath('//table[@class="tablelist textl"]/tr[3]//li/text()').extract()
#         item['jobinfo'] = response.xpath('//table[@class="tablelist textl"]/tr[4]//li/text()').extract()
#         #print(jobname,worklocation,jobtype,jobdesc,jobinfo)
#         yield item

class TencentSpider(scrapy.Spider):
    # 爬虫的名称，启动爬虫的时候会根据名称找对应的爬虫文件
    name = 'Tencent'
    # allowed_domains，允许爬取的域，你要爬取的链接必须在这个域下，可以是多个
    allowed_domains = ['hr.tencent.com']
    # 起始的url，可以是多个
    start_urls = ['https://hr.tencent.com/position.php']
    base_url = 'https://hr.tencent.com/position.php'

    # 解析每一页的数据，response请求返回的响应结果
    def parse(self, response):
        print(response.status)
        #是一个二进值文件
        # print(response.body)
        # xpath、css、re
        # response.xpath('')
        job_even = response.xpath('//tr[@class="even"]/td[@class="l square"]/a/@href').extract()
        job_odd = response.xpath('//tr[@class="odd"]/td[@class="l square"]/a/@href').extract()
        # print(job_even, job_odd)
        #总的职位的链接
        jobs = job_even+job_odd

        for nodeurl in jobs:
            fullurl = urljoin('https://hr.tencent.com/position.php',nodeurl)
            # print(fullurl)
            # yield在这里是相当于是实现了异步，每当遇到yeild就会先暂停一下，
            # 然后先返回yeild后面的值，下次再执行的时候，会从上次的执行中断的地方开始
            yield scrapy.Request(fullurl,callback=self.parseJobDetail)

        links = response.xpath('//div[@class="pagenav"]//a/@href').extract()
        for url in links:
            if 'position.php' in url:
                print(url)
                fullurl = urljoin(self.base_url,url)
                yield scrapy.Request(fullurl,callback=self.parse)

    # 解析每一个职位详情
    def parseJobDetail(self,response):
        print(response.status)
        item = TengxuntwoItem()
        # 目标数据：职位名称、工作地点、职位类别、工作职责、工作要求
        item['jobName'] = response.xpath('//td[@id="sharetitle"]/text()').extract()[0]
        item['workLocation'] = response.xpath('//tr[@class="c bottomline"]/td[1]/text()').extract()[0]
        item['jobType'] = response.xpath('//tr[@class="c bottomline"]/td[2]/text()').extract()[0]
        item['jobDesc'] = response.xpath('//table[@class="tablelist textl"]/tr[3]//li/text()').extract()
        item['jobInfo'] = response.xpath('//table[@class="tablelist textl"]/tr[4]//li/text()').extract()
        # print(jobName,workLocation,jobType,jobDesc,jobInfo)
        yield item
