# -*- coding: UTF-8 -*-


import scrapy
from Poverty.items import PovertyItem
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

class PovertySpider(scrapy.Spider):
    name = "poverty"
    allowed_domains = ["http://price.scnjw.gov.cn/pas/price.do?method=priceInfoList"]
    start_urls = ["http://price.scnjw.gov.cn/pas/price.do?method=priceInfoList&pageNo=1"]
    # rules = [
    #     Rule(SgmlLinkExtractor(allow=
    #                            (r'http://price.scnjw.gov.cn/pas/price.do?method=priceInfoList&pageNo=\d'))),
    #     Rule(SgmlLinkExtractor(allow=
    #                            (r'http://price.scnjw.gov.cn/pas/price.do?method=priceInfoList&pageNo=\d+')), callback="parse_item"),
    # # ]          "//*[@id="box"]/table/tbody"

    def parse(self, response):
        row = response.xpath('//table/tbody/tr')
        for i in range(0, len(row)):
            item = PovertyItem()
            item["name"] = row[i].xpath('./td[1]/a/text()').extract()[0]
            item["size"] = row[i].xpath('./td[2]/text()').extract()[0]
            item["unit"] = row[i].xpath('./td[3]/text()').extract()[0]
            item["price"] = row[i].xpath('./td[4]/text()').extract()[0]
            item["manufacturer"] = row[i].xpath('./td[5]/a/text()').extract()[0]
            yield item
            print item
