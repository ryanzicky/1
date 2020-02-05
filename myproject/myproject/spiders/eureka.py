# -*- coding: utf-8 -*-
import scrapy

from myproject.items import EurekaItem


class EurekaSpider(scrapy.Spider):
    name = 'eureka'
    allowed_domains = ['eureka.com']
    start_urls = ['http://172.16.20.89:8001/']

    def parse(self, response):
        application_contents = response.xpath("//tbody/tr").extract()
        # application_name = response.xpath("//tbody/tr/td[1]//b/text()").extract()
        for content in application_contents:
            temp = content.xpath("//tr//td[1]/text()").extract()
            print(temp)
        pass

