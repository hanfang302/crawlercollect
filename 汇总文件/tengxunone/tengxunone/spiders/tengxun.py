import scrapy
import re
from tengxunone.items import TengxunoneItem
from urllib.parse import urljoin


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
        #print(response.body)

        #目标数据：职位名称，职位地点，职位类别，工作职责，工作要求

        #xpath
        #response.xpath('')
        job_even = response.xpath('//tr[@class="even"]/td[@class="l square"]/a/@href').extract()
        job_odd = response.xpath('//tr[@class="odd"]/td[@class="l square"]/a/@href').extract()
        #总职位链接
        jobs = job_even+job_odd

        #完整路径
        for nodeurl in jobs:
            fullurl = urljoin('https://hr.tencent.com/position.php',nodeurl)
            print(fullurl)

            #yield在这里是实现了异步,每当遇到yield就会先返回yeild后面的值.
            #下次在执行的时候,会从上次的执行中段的地方开始
            # 发起请求(自动下载)
            yield scrapy.Request(fullurl,callback=self.parseJobDetail)

        #获取多页链接
        #links = response.xpath('//div[@class="pagenav"]//a/@href')
        # for url in links:
        #     if 'position.php' in url:
        #         print(url)


    #下载完数据进行解析
    def parseJobDetail(self,response):
        print(response.status)
        item = TengxunoneItem()
        #取值
        item['jobname'] = response.xpath('//td[@id="sharetitle"]/text()').extract()[0]
        item['worklocation'] = response.xpath('//tr[@class="c bottomline"]/td[1]/text()').extract()[0]
        item['jobtype'] = response.xpath('//tr[@class="bottomline"]/td[2]/text()').extract()[0]
        item['jobdesc'] = response.xpath('//table[@class="tablelist textl"]/tr[3]//li/text()').extract()
        item['jobinfo'] = response.xpath('//table[@class="tablelist textl"]/tr[4]//li/text()').extract()

        yield item


