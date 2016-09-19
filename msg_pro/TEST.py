# -*- coding: utf-8 -*-
# 2016/9/1 22:37


import requests,random
from lxml import etree
url = 'http://www.qiushibaike.com/hot/page/2/'#直接选择一页的笑话list随机选择一个比较好~
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
request = requests.get(url,headers = headers)
content = request.content.decode('utf-8')
html=etree.HTML(content)
result=html.xpath('//*[@class="content"]/text()')
random_number=random.randint(1,10)
choice_joke=result[random_number]
for i in result:
    print(i.replace('\n',''))