# -*- coding: utf-8 -*-
import scrapy
import re
from boles.items import BolesItem

class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    #起始URL
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
        # filename = 'jobbole.html'
        # open(filename,'wb').write(response.body)
        post_nodes = response.css("#archive .floated-thumb .post-thumb a")
        for post_node in post_nodes:
            image_url = post_node.css("img::attr(src)").extract_first("")
            post_url = post_node.css("::attr(href)").extract_first("")

            yield scrapy.Request(url=parse.urljoin(response.url, post_url), meta={"front_image_url": image_url},callback=self.parse_detail)

    def parse_detail(self, response):
        title = response.xpath('//div[@class="entry-header"]/h1/text()').extract_frist("")
        create_date = response.xpath("//p[@class='entry-meta-hide-on-mobile']/text()").extract_first(
            "").strip().replace("·", "").strip()
        url = response.url
        # http://blog.jobbole.com/113949/
        object_id = re.match(".*?(\d+).*", url).group(1)
        praise_nums = response.xpath("//span[contains(@class,'vote-post-up')]/h10/text()").extract_first("")

        bookmark_nums = response.xpath("//span[contains(@class,'bookmark-btn')]/text()").extract_first("")
        match_bookmark_nums = re.match(".*?(\d+).*", bookmark_nums)
        if match_bookmark_nums:
            bookmark_nums = int(match_bookmark_nums.group(1))
        else:
            bookmark_nums = 0
        comment_nums = response.xpath("//a[@href='#article-comment']/span/text()").extract_first("")
        match_comment_nums = re.match(".*?(\d+).*", comment_nums)
        if match_comment_nums:
            comment_nums = int(match_comment_nums.group(1))
        else:
            comment_nums = 0
        content = response.xpath("//div[@class='entry']").extract_first("")
        # 过滤评论标签
        tag_list = response.xpath("//p[@class='entry-meta-hide-on-mobile']//a/text()").extract()
        tag_list = [element for element in tag_list if not element.strip().endswith("评论")]
        tags = ",".join(tag_list)

        item = BolesItem()
        item['title'] = title
        item['create_date'] = create_date
        item['url'] = url
        item['url_object_id'] = object_id
        item['front_image_url'] = response.meta.get("front_image_url", "")
        item['praise_nums'] = praise_nums
        item['bookmark_nums'] = bookmark_nums
        item['comment_nums'] = comment_nums
        item['content'] = content
        item['tags'] = tags

        print(item)
        return item
