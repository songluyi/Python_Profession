# -*- coding: utf-8 -*-
# 2016/9/19 19:36
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
class proxy_spider(object):
    def __init__(self):
        self.row_url={
            '快代理':['http://www.kuaidaili.com/proxylist/'],
            '西刺代理':['http://www.xicidaili.com/nn/','http://www.xicidaili.com/nt/']
        }
        self.header_xici={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                     "Accept-Encoding":"gzip, deflate, sdch",
                     "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
                     "Cache-Control":"max-age=0",
                     "Connection":"keep-alive",
                     "Cookie":"_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJTJlMThkZWYyMGJkOTE2NTM4NzY2OGZkYWJlMzQ2MDZjBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMUhLTWpKZ0Fab3hoY3hJOVpVditRUGNCc2hWUVR3RTFMUVRkWkdKeDlISHM9BjsARg%3D%3D--6585e38227117fb3b07d24c67540857e84beb7af; CNZZDATA1256960793=693292312-1474279779-null%7C1474441899",
                     "DNT":"1",
                     "Host":"www.xicidaili.com",
                     "Referer":"http//www.xicidaili.com/qq/",
                     "Upgrade-Insecure-Requests":"1",
                     "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36"}

        self.header_kuai={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                          "Accept-Encoding":"gzip, deflate, sdch",
                          "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
                          "Cache-Control":"max-age=0","Connection":"keep-alive",
                          "Cookie":"channelid=0; sid=1474442634155791; _ga=GA1.2.1358484058.1466123771; Hm_lvt_7ed65b1cc4b810e9fd37959c9bb51b31=1474275937,1474275941,1474283360,1474443234; Hm_lpvt_7ed65b1cc4b810e9fd37959c9bb51b31=1474443252",
                          "DNT":"1","Host":"www.kuaidaili.com",
                          "Referer":"http//www.kuaidaili.com/proxylist/2/",
                          "Upgrade-Insecure-Requests":"1",
                          "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36"}
    def form_url(self,row_url):
        new_list=[]
        for i in row_url:
            url_list=list(map(lambda x:i+str(x),range(1,11)))
            new_list.extend(url_list)
        return new_list

    def get_source(self,url):
        if 'kuaidaili'in url:
            print('这是快代理的url，正在改用其header')
            html=requests.get(url,header=self.header_kuai).text
            new_html=etree.HTML(html)


        return

    def url_check_valid(self,url,header):
        return



if __name__=='__main__':
    fuck_proxy=proxy_spider()
    new_list=[]
    row_url_0=fuck_proxy.row_url['快代理']
    row_url_1=fuck_proxy.row_url['西刺代理']
    url_list_0=fuck_proxy.form_url(row_url_0)
    url_list_1=fuck_proxy.form_url(row_url_1)
