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

# import requests
# import urllib.request
# from lxml import etree
# url='http://www.xicidaili.com/nt/'
# header_kuai={"Host":" www.xicidaili.com","User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0",
#              "Accept":" text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language":" zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3","Accept-Encoding":" gzip, deflate","Upgrade-Insecure-Requests":" 1","Cache-Control":" max-age=0","Referer":" http//www.xicidaili.com/nt/","Cookie":" _free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJTllNjNkYjhlNjZmYzYxYjcxMzI2MDIyZWZkY2MxYTBlBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMUtNRkVaNWlXOFFqODk1TVlxU2VaUjlHWENZTVdUYjdlaXNiTEtyeHdOOGM9BjsARg%3D%3D--0ceab0a393c2f58e32fc36c49fe408db554e175a; CNZZDATA1256960793=986726285-1474512175-%7C1474512175","Connection":" keep-alive"}
# html_1=requests.get(url,headers=header_kuai).text
#
# new_html=etree.HTML(html_1)
#
# new_data=[]
# data=new_html.xpath('//tr[@class=""]')
# # change_data=list(map(lambda x:x.text,data))
# for i in data:
#     s=i.xpath("./td/text()")
#     print(s)
# count=int(len(data) /8)
# for i in range(count):
#     new_data.append(data[i*8:(i+1)*8])
# print(new_data)
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
