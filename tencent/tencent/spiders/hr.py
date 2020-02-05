# -*- coding: utf-8 -*-
import scrapy
import logging

class HrSpider(scrapy.Spider):
    name = 'hr'
    allowed_domains = ['tencent.com']
    start_urls = ['https://careers.tencent.com/search.html']

    def parse(self, response):
        logging.warning(response)
        tr_list = response.xpath("//div[@class='recruit-wrap recruit-margin']")
        logging.warning(tr_list)

        for tr in tr_list:
            item = {}
            item["title"] = tr.xpath("./td[1]/a/text()").extract_first()
            item["position"] = tr.xpath("./td[2]/text()").extract_first()
            item["publish_date"] = tr.xpath("./td[5]/text()").extract_first()
            logging.warning(item)
            yield item
        # 找到下一页url地址
        # next_url = response.xpath("//a[@id='nect']/@href").extract_first()
        # if next_url != "javascript:;":
        #     next_url = "http://hr.tencent.com/" + next_url
        #     yield scrapy.Request(
        #         next_url,
        #         callback=self.parse
        #     )
