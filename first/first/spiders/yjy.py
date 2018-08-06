# -*- coding: utf-8 -*-
import scrapy

from first.items import FirstItem

class YjySpider(scrapy.Spider):
    name = "yjy"
    allowed_domains = ["baidu.com"]
    start_urls = (
        'http://www.baidu.com/',
    )

    def parse(self, response):
        item=FirstItem()
        item["content"]=response.xpath("/html/head/title/text()").extract()
        yield item
