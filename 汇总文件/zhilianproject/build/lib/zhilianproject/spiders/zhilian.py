# -*- coding: utf-8 -*-
import scrapy
#LinkExtractor:根据定义的正则规则,匹配链接
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
#from zhilianproject import ZhilianprojectItem

class ZhilianSpider(CrawlSpider):
    #爬虫的名称
    name = 'zhilian'
    #允许爬取的域
    allowed_domains = ['sou.zhaopin.com','jobs.zhaopin.com','company.zhaopin.com']
    #allowed_domains = ['zhaopin.com']
    #起始url
    start_urls = ['https://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=%E6%8A%80%E6%9C%AF&sm=0&p=1']
    #下一页链接
    #<a href="http://sou.zhaopin.com/jobs/searchresult.ashx?
    # jl=%e5%8c%97%e4%ba%ac&amp;kw=%e6%8a%80%e6%9c%af&amp;
    # sm=0&amp;sg=2a95483132f04bea863efbef940e4c2a&amp;p=4">4</a>
    #'http.*?jobs/searchresult'

    #匹配链接
    # < a
    # style = "font-weight: bold"
    # par = "ssidkey=y&amp;ss=201&amp;ff=03&amp;sg=2a95483132f04bea863efbef940e4c2a&amp;so=3"
    # href = "http://jobs.zhaopin.com/130236690250245.htm"
    # target = "_blank" > 高级售前 < b > 技术 < / b > 支持
    # < / a >

    #匹配公司详情链接，进行请求
    #http://company.zhaopin.com/CZ556345420.htm
    rules = (
        Rule(LinkExtractor(allow=('http.*?jobs/searchresult',),
                           restrict_xpaths='//div[@class="pagesDown"]/ul'),
                           callback='parse_item'),
                           #follow=True),

        Rule(LinkExtractor(allow=('http.*?jobs.zhaopin.com/.*?html',),
                           restrict_xpaths='//div[@class="newlist_list_content_table"]'),
             callback='parse_job_detail'),
             #follow=True),

        Rule(LinkExtractor(allow=('http.*?company.zhaopin.com/.*?html',)),
             callback='parse_company_detail'),
        # follow=True),
    )

    def parse_item(self, response):
        print(response.staus)
        print(response.url)


    def parse_job_detail(self, response):
        print(response.staus)
        print(response.url)

        # item = ZhilianprojectItem()
        # item['jobname'] = response.xpath('//div[@class="clone_category"]//h1/text()').extract_first('') # 名称
        # item['salary'] = response.xpath('//div[@class="terminalpage clearfix"]') # 薪资
        # item['time'] = response.xpath('')  # 时间
        # item['desc'] = response.xpath('')  # 描述
        # item['address'] = response.xpath('')  # 地址
        # item['company'] = response.xpath('')  # 公司名称


    def parsee_company_detail(self,response):
        print(response.staus)
        print(response.url)

        #i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        #return i
