# -*- coding: utf-8 -*-
# 2016/8/30 10:29
"""
-------------------------------------------------------------------------------
Function:   用于爬取内容，本脚本可以扩展
Version:    1.1
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""
class crawl_spider(object):
    #抓取天气数据的爬虫
    def crawl_weather(self,place):
        from urllib.request import urlopen
        import json
        url = 'https://api.heweather.com/x3/weather?city='+place
        from msg_pro.sms import sms_send
        config=sms_send().load_setting()
        my_key=config[2]#和风天气的API key 填入就好
        full_url=url+'&key='+my_key
        print(full_url)
        req = urlopen(full_url)
        content = str(req.read(),'utf-8')
        content=str(content).replace("b'",'').replace("'",'')
        new_content=json.loads(content)
        return new_content

    def select_weather_info(self,row_weather_info):
         print(row_weather_info["HeWeather data service 3.0"][0])#目前还不清楚这个接口是否只能获取一个城市的信息
         if row_weather_info["HeWeather data service 3.0"][0]["status"] =='ok':
            print('success')
            #因为是妹子，所以早上发消息要求：当日天气基本信息 出行穿着 紫外线的信息
            #短信字数为70多字，所以尽量要精练一点。
            need_info={}
            need_info['basic_data']=row_weather_info["HeWeather data service 3.0"][0]["aqi"]['city']
            need_info["today_weather"]=row_weather_info["HeWeather data service 3.0"][0]['daily_forecast'][0]
            need_info["suggestion"]=row_weather_info["HeWeather data service 3.0"][0]['suggestion']
            need_info['today_temp']=row_weather_info["HeWeather data service 3.0"][0]['now']
            return need_info
         else:
             print('错误信息如下:')
             print(row_weather_info["HeWeather data service 3.0"][0]["status"])
             return False
    def make_need_weather_info(self,row_weather_data):
        from msg_pro.sms import sms_send
        config=sms_send().load_setting()
        sms_header=config[3]
        today_weather='今天白天天气为:'+row_weather_data['today_weather']['cond']['txt_d']+' '+'夜间天气为:'+\
        row_weather_data['today_weather']['cond']['txt_n']+' '+'今日有'+row_weather_data['today_weather']['wind']['sc']\
        +' '+'整体温度为'+row_weather_data['today_temp']['tmp']+' '+'因此汪汪建议:1.'+row_weather_data['suggestion']['comf']['txt']+'2.'+row_weather_data['suggestion']['uv']['txt']\
        +'3.'+row_weather_data['suggestion']['drsg']['txt']
        row_sms=sms_header+today_weather
        return row_sms
    #下面是一个非常简单的抓取joke小函数大家可以自己发挥
    def crawl_jokes(self):
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
        return choice_joke.replace('\n','')

    #微博艾特短信提示功能,待完成
    def get_weibo_at(self):
        from selenium import webdriver
        driver=webdriver.Firefox()
        driver.get('http://weibo.com/1822822705/profile?rightmod=1&wvr=6&mod=personnumber&is_all=1#_loginLayer_1472635119486')
        return

    def main(self):
        info=crawl_spider().crawl_weather('yuanan')
        print(info)
        row_weather_data=crawl_spider().select_weather_info(info)
        if row_weather_data:
            row_sms=crawl_spider().make_need_weather_info(row_weather_data)
            print(row_sms)
            return row_sms
        else:
            print('error')



