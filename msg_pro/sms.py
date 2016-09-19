# -*- coding: utf-8 -*-
# 2016/8/29 20:12
"""
-------------------------------------------------------------------------------
Function:
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""
import time
from crawl_info import crawl_spider
class sms_send(object):

    def md5(self,row_str):
        import hashlib
        m2=hashlib.md5()
        m2.update(row_str.encode('utf-8'))
        return m2.hexdigest()

    def form_request(self,content):
        config=sms_send().load_setting()
        username=config[0]#这个定制的不便宜，一毛一条好贵，买五百条才8分一条
        password=config[1]
        phone_number=config[4]
        sms_header=config[3]
        base_url='http://api.smsbao.com/sms?u='+username+'&p='+sms_send().md5(password)+'&m='+phone_number+'&c='+content
        return base_url

    def start_request(self,content):
        import requests
        # content=crawl_spider().main()
        request_link=sms_send().form_request(content)
        print(request_link)
        get_back=requests.get(request_link)
        print(get_back.content)

    def load_setting(self):
        with open('setting.ini','r',errors='ignore') as f:
            data=f.readlines()
        return [data[1].replace('\n','').split('=')[1],data[2].replace('\n','').split('=')[1],
               data[4].replace('\n','').split('=')[1],data[6].replace('\n','').split('=')[1],
               data[7].replace('\n','').split('=')[1]]
if __name__=='__main__':
    while True:
        today_time=time.strftime("%H:%M:%S", time.localtime()).split(':')
        print(today_time)
        time.sleep(1)
        #每天早上7.00发送短信提示
        if today_time[0]=='13' and today_time[1]=='16' and today_time[2]=='00':
            content=crawl_spider().main()
            sms_send().start_request(content)
            print('send weather sms successfully')
        if today_time[0]=='20' and today_time[1]=='00' and today_time[2]=='00':
            content=crawl_spider().crawl_jokes()
            sms_send().start_request(content)
            print('send joke sms successfully')





