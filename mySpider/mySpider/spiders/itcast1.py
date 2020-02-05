# -*- coding: utf-8 -*-
import scrapy
import logging

class Itcast1Spider(scrapy.Spider):
    name = 'itcast1'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://itcast.cn/']

    def parse(self, response):
        # pass
        logging.warning('111111')
