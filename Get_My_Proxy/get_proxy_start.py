# -*- coding: utf-8 -*-
# 2016/9/19 19:36
"""
-------------------------------------------------------------------------------
Function:   从多家代理网站获取代理并检测
Version:    1.1
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""

import requests
from lxml import etree
import pymysql
from configparser import ConfigParser
from PIL import Image
import pytesser3   #这个是我自己写的一个 已经上传pypi 大家可以下载来试一下
try:
    from pytesser import image_to_string
except:
    from pytesseract import image_to_string
class proxy_spider(object):
    def __init__(self):
        #可以在下方加入自己想要新增的代理IP页面
        self.row_url={
            '快代理':['http://www.kuaidaili.com/proxylist/'],
            '西刺代理':['http://www.xicidaili.com/nn/','http://www.xicidaili.com/nt/',
                    'http://www.xicidaili.com/wn/','http://www.xicidaili.com/wt/'],
            '站大爷':['http://ip.zdaye.com/']#这个比较特殊
        }
        self.db_setting=self.read_config()
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
                          "Cache-Control":"max-age=0",
                          "Connection":"keep-alive",
                          "Cookie":"channelid=0; sid=1474442634155791; _ga=GA1.2.1358484058.1466123771; Hm_lvt_7ed65b1cc4b810e9fd37959c9bb51b31=1474275937,1474275941,1474283360,1474443234; Hm_lpvt_7ed65b1cc4b810e9fd37959c9bb51b31=1474443252",
                          "DNT":"1",
                          "Host":"www.kuaidaili.com",
                          "Referer":"http//www.kuaidaili.com/proxylist/2/",
                          "Upgrade-Insecure-Requests":"1",
                          "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36"}
        self.header_daye={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                          "Accept-Encoding":"gzip, deflate, sdch",
                          "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
                          "Cache-Control":"max-age=0",
                          "Connection":"keep-alive",
                          "Cookie":"ASPSESSIONIDSQTSCCDB=LPKDFCOAPPGMEJBGDGLKLGIM; ASPSESSIONIDSABBTDDB=ALFHNFOAKCPCGCIAIPGDHFCN; ASPSESSIONIDQCCBTDDB=PACIODPAACFHFJLLHMABEJFN; AJSTAT_ok_pages=1; AJSTAT_ok_times=4; Hm_lvt_8fd158bb3e69c43ab5dd05882cf0b234=1474939866,1474939872,1474939882,1474940198; Hm_lpvt_8fd158bb3e69c43ab5dd05882cf0b234=1474948132",
                          "DNT":"1",
                          "Host":"ip.zdaye.com",
                          "Upgrade-Insecure-Requests":"1",
                          "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36"}
    def form_url(self,row_url):
        new_list=[]
        for i in row_url:
            url_list=list(map(lambda x: i+str(x), range(1, 21)))
            new_list.extend(url_list)
        return new_list

    def get_source(self,url):
        if 'kuaidaili'in url:
            print('正在爬取快代理的url:'+url)
            html=requests.get(url,headers=self.header_kuai).text
            new_html=etree.HTML(html)
            new_data=[]
            data=new_html.xpath('//*[@id="index_free_list"]/table/tbody/tr/td')
            change_data=list(map(lambda x:x.text,data))
            count=int(len(data) /8)
            for i in range(count):
                new_data.append(change_data[i*8:(i+1)*8])
            return new_data
        if 'xicidaili' in url:
            print('正在爬取西刺代理的url:'+url)
            html=requests.get(url, headers=self.header_xici).text
            new_html=etree.HTML(html)
            new_data=[]
            data_even=new_html.xpath('//tr[@class=""]')
            data_odd=new_html.xpath('//tr[@class="odd"]')
            for i in data_even:
                detail_data=i.xpath("./td/text()")
                new_data.append([detail_data[0], detail_data[1], detail_data[4], detail_data[5], detail_data[10]])
            for j in data_odd:
                detail_data=j.xpath("./td/text()")
                #分别对应的是IP PORT HIDE TYPE VALID TIME
                new_data.append([detail_data[0], detail_data[1], detail_data[4], detail_data[5], detail_data[10]])
            return new_data
        #如果加入了任何自己的代理可以在下面加入if判断
        if 'zhandaye' in url:#这个很网站很特殊需要特别处理
            print('正在爬取傻吊站大爷代理')
            html = requests.get(url, headers=self.header_daye).text
            new_html = etree.HTML(html)
            new_data = []
            ip_list=new_html.xpath('//*[@id="ipc"]/tbody/tr/td[1]')
            row_code_list=new_html.xpath('//*[@id="ipc"]/tbody/tr/td[3]/img/@src')
            full_code_list=list(map(lambda row_url: 'http://ip.zdaye.com'+row_url, row_code_list))
            code_list_data=list(map(self.get_code, full_code_list))
            type_list_data=new_html.xpath('//*[@id="ipc"]/tbody/tr/td[4]')
            place_list_data=new_html.xpath('//*[@id="ipc"]/tbody/tr/td[5]')
            ping_list_data=new_html.xpath('//*[@id="ipc"]/tbody/tr/td[19]')
            for i in range(1,len(ip_list)):
                new_data.append([ip_list[1],code_list_data[0],type_list_data[1],place_list_data[1],ping_list_data[0]])

            return new_data
    #总结一下：虽然新增一个proxy需要定义一个if 很蠢但是由于每一个代理规则都不一 ，而自适应规则相当麻烦，等有能力在做吧。
    def url_check_valid(self, row_url):
        for proxy_name, proxy_url in row_url.iteritems():
            if 'http' in row_url[proxy_name][0] and row_url[proxy_name][0][-1] == '/':
                try:
                    self.get_source(row_url[proxy_name][0])

                except Exception:
                    print('This url may not be connected, please check your network status or header setting')
                    raise Exception
            else:
                print("url is not a standard one, please check your url contains 'http' and last bytes is '/' ")
        return
        #支持拓展mysql数据的插入
    def check_db_valid(self):
        try:
            db = pymysql.connect(self.db_setting[0][1],self.db_setting[1][1],self.db_setting[2][1],self.db_setting[3][1],port=int(self.db_setting[4][1]),charset=self.db_setting[5][1])
            return 'success'
        except Exception:
            return 'failed'

    def insert_mysql_db(self, data):
        #感觉这样做挺蠢的，不知道有没有状态继承 可以访问成功一次直接进行数据插入==
        db = pymysql.connect(self.db_setting[0][1],self.db_setting[1][1],self.db_setting[2][1],self.db_setting[3][1],port=int(self.db_setting[4][1]),charset=self.db_setting[5][1])
        #建立游标对象
        cursor=db.cursor()
        cursor.excute()
        db.commit()
        return

    def read_config(self):
        cfg = ConfigParser()
        cfg.read('config.ini')
        return cfg.items(cfg.sections()[0])
    #不用lock 唯一标示即可
    def get_code(self, url):
        # url = 'http://www.rongtudai.com/validimg.html'
        f=requests.get(url)
        print(f)
        name=url[-39:-19]
        path='/codepic/'+name
        with open(path, "wb") as code:
            code.write(f.content)
        img = Image.open(path)
        img = img.convert("RGBA")
        pixdata = img.load()
        for y in range(img.size[1]):
             for x in range(img.size[0]):
                if pixdata[x, y][0] < 90:
                    pixdata[x, y] = (0, 0, 0, 255)
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                if pixdata[x, y][1] < 136:
                    pixdata[x, y] = (0, 0, 0, 255)
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                if pixdata[x, y][2] > 0:
                    pixdata[x, y] = (255, 255, 255, 255)
        img.save('/codepic/'+'newcode.gif')
        img = Image.open('/codepic/'+'newcode.gif')
        vcode =image_to_string(img)
        try:#r如果识别失败则默认为8080端口
            int(vcode)
        except:
            vcode=8080
        return vcode


    def isAlive(self, ip, port, header):
        proxy={'http': 'http://'+ip+':'+port, 'https:': 'https://'+ip+':'+port}
        print(proxy)
        #使用这个方式是全局方法。
        #使用代理访问百度网站，进行验证代理是否有效
        test_url = "http://www.baidu.com"
        try:
            #timeout 设置为10，如果你不能忍受你的代理延时超过10，就修改timeout的数字
            req=requests.get(test_url, headers=header, proxies=proxy, timeout=10)
            if req.status_code == 200:
                print("work")
                return True
            else:
                print("not work")
                return False
        except Exception :
            print("Not work")
            return False
if __name__=='__main__':
    fuck_proxy=proxy_spider()
    new_list=[]
    row_url_0=fuck_proxy.row_url['快代理']
    row_url_1=fuck_proxy.row_url['西刺代理']
    url_list_0=fuck_proxy.form_url(row_url_0)
    url_list_1=fuck_proxy.form_url(row_url_1)
    kuai_proxy_list=list(map(fuck_proxy.get_source,url_list_0))
    huaci_proxy_list=list(map(fuck_proxy.get_source,url_list_1))
