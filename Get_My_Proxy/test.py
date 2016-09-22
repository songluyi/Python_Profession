# -*- coding: utf-8 -*-
# 2016/9/20 18:15
"""
-------------------------------------------------------------------------------
Function:
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""
import requests
from lxml import etree
url='http://www.kuaidaili.com/proxylist/'
header_kuai={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                          "Accept-Encoding":"gzip, deflate, sdch",
                          "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
                          "Cache-Control":"max-age=0",
                          "Connection":"keep-alive",
                          "Cookie":"channelid=0; sid=1474442634155791; _ga=GA1.2.1358484058.1466123771; Hm_lvt_7ed65b1cc4b810e9fd37959c9bb51b31=1474275937,1474275941,1474283360,1474443234; Hm_lpvt_7ed65b1cc4b810e9fd37959c9bb51b31=1474443252",
                          "DNT":"1",
                          "Host":"www.kuaidaili.com",
                          "Referer":"http//www.kuaidaili.com/proxylist/2/",
                          "Upgrade-Insecure-Requests":"1",
                          "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36"}
html=requests.get(url,header_kuai).text
new_html=etree.HTML(html)
new_data=[]
data=new_html.xpath('//*[@id="index_free_list"]/table/tbody/tr/td')
print(data)
change_data=list(map(lambda x:x.text,data))
count=int(len(data) /8)
for i in range(count):
    new_data.append(change_data[i*8:(i+1)*8])
print(new_data)

# import pymysql
# from configparser import ConfigParser
#
# cfg = ConfigParser()
# cfg.read('config.ini')
# print(cfg.sections())
# print(cfg.items(cfg.sections()[0]))
# db_setting=cfg.items(cfg.sections()[0])
# db = pymysql.connect(db_setting[0][1],db_setting[1][1],db_setting[2][1],db_setting[3][1],port=int(db_setting[4][1]),charset=db_setting[5][1])


# a=('ip', 'localhost')
# print(a[1])
