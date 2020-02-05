# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class EurekaItem(scrapy.Item):
    application_name = scrapy.Field()
    url = scrapy.Field()
    device_name = scrapy.Field()

