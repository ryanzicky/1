import scrapy
from tutorial.items import TutorialItem
import json
import logging

class DmozSpider(scrapy.Spider):
    name = "dmoz" # 设置爬虫名称
    allowed_domains = ["baidu.com"] # 设置域名
    start_urls = [
        "http://tieba.baidu.com/f?kw=%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB&ie=utf-8",
    ] # 设置爬取地址

    # 爬取方法
    def parse(self, response):
        for line in response.xpath('//li[@class="j_thread_list clearfix"]'):
            # 初始化item对象保存爬取的信息
            item = TutorialItem()
            # 解析爬取的内容
            item['title'] = line.xpath('.//div[contains(@class, "threadlist_title pull_left j_th_tit")]/a/text()').extract()
            item['author'] = line.xpath('.//div[contains(@class, "threadlist_author pull_right")]//span[contains(@class, "frs-author-name-wrap")]/a/text()').extract()
            item['reply'] = line.xpath('.//div[contains(@class, "col2_left j_threadlist_li_left")]/span/text()').extract()
            
            self.logger.info('ssssssssssssssssssssssssssssssssssssssssssssssssssssssssss')
            self.logger.info({'title':item['title'],'author':item['author'],'reply':item['reply']})
            self.logger.info('qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq')
            yield item