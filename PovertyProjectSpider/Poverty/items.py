# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field, Item


class PovertyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()           #商品名称
    size = scrapy.Field()           #规格
    unit = scrapy.Field()           #单位
    price = scrapy.Field()          #价格
    manufacturer = scrapy.Field()   #发布单位
    time = scrapy.Field()           #发布时间
    pricechange = scrapy.Field()    #价格涨跌
