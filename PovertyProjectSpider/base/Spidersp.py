# -*- coding: utf-8 -*-
import requests
import sys
from lxml import etree
import pandas as pd
from multiprocessing.dummy import Pool as ThreadPool

reload(sys)
sys.setdefaultencoding("utf-8")

name = []       # 商品名称
size = []       # 规格
unit = []       # 单位
price = []      # 价格
manufacturer = []   # 发布单位
time = []           # 发布时间
pricechange = []    # 价格涨跌

def spider(url):
    html = requests.get(url).text
    html = html.encode("utf-8")
    selector = etree.HTML(html)
    field = selector.xpath('//table[@class="table table-striped table-bordered"]')[0]
    content = field.xpath('tr')
    for each in content:
        list=each.xpath('td')
        name=list[0][0]
        name=name.xpath('string(.)').replace('\t','').replace(' ','')
        money=list[1].xpath('string(.)').replace('\t','').encode("utf-8")
        money=money.split()[0]
        project=list[2][0]
        project=project.xpath('string(.)').replace('\t','').replace(' ','')
        date=list[3][0]
        date=date.xpath('string(.)').replace('\t','').replace(' ','')
        style=list[4][0]
        style=style.xpath('string(.)').replace('\t','').replace(' ','')
        user_type=list[5][0]
        user_type=user_type.xpath('string(.)').replace('\t','').replace(' ','')
        Name.append(name)
        Money.append(money)
        Project.append(project)
        Date.append(date)
        Style.append(style)
        User_type.append(user_type)
for i in range(1,101):
    newpage='http://alumni.xjtu.edu.cn/donation/namelist?pageNo='+str(i)+'&pageSize=10&billnum=&donateUserName=&orderWay=&donationid=0'
    page.append(newpage)
pool = ThreadPool(2)
pool.map(spider,page)

data={'Name':Name,'Money':Money,'Project':Project,'Date':Date,'Style':Style,'User_type':User_type}
data=pd.DataFrame(data)
data.to_csv('donation.csv',encoding='gbk')