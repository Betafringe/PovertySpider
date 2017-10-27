from lxml import etree
import requests


#
# row = response.xpath('//table/tbody/tr')
# # for col in row:
# # for i in range(0, len(row)):
# #     tmp.append(row[i].xpath('./td[1]/a/text()').extract()[0])
# #     tmp.extend(row[i].xpath('./td/text()').extract())
# #     data.append(tmp)

start_urls = []
for i in range(1, 100):
    item = "http://price.scnjw.gov.cn/pas/price.do?method=priceInfoList&pageNo=" + str(i)
    start_urls.append(item)