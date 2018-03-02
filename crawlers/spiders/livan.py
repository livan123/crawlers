# -*- coding: utf-8 -*-
import scrapy

class LivanSpider(scrapy.Spider):
    name = 'livan'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        pass
