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
class proxy_spider(object):
    def __init__(self):
        self.row_url={
            '快代理':['http://www.kuaidaili.com/proxylist/'],
            '西刺代理':['http://www.xicidaili.com/nn/','http://www.xicidaili.com/nt/',]
        }

    def form_url(self,row_url):
        for i in row_url:
            print(i)
            return list(map(lambda x:print(i+str(x)),range(10)))
    #看可否用lambda改写





if __name__=='__main__':
    fuck_proxy=proxy_spider()
    row_url_1=fuck_proxy.row_url['快代理']
    row_url_2=fuck_proxy.row_url['西刺代理']
    url_1_list=fuck_proxy.form_url(row_url_1)
    url_2_list=fuck_proxy.form_url(row_url_2)
    print(url_1_list)