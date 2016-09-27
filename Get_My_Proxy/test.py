import requests
from PIL import Image
from pytesser3 import image_to_string
header={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8","Accept-Encoding":"gzip, deflate, sdch","Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6","Cache-Control":"max-age=0","Connection":"keep-alive","Cookie":"ASPSESSIONIDSQTSCCDB=LPKDFCOAPPGMEJBGDGLKLGIM; ASPSESSIONIDSABBTDDB=ALFHNFOAKCPCGCIAIPGDHFCN; ASPSESSIONIDQCCBTDDB=PACIODPAACFHFJLLHMABEJFN; ASPSESSIONIDQCDBTCDB=MDANGHPAAMILAMJDEMGPOOBI; ASPSESSIONIDSACBQDDB=ALDAPKPACHHBLNIOCBGLCKFA; ASPSESSIONIDAADBQDDB=ALAIPBABBEAAJLBDCKGKOGBD; ASPSESSIONIDSQTRACDD=LNDNBFCBNKIGGFCKHNOFIECB; AJSTAT_ok_pages=2; AJSTAT_ok_times=6; Hm_lvt_8fd158bb3e69c43ab5dd05882cf0b234=1474939866,1474939872,1474939882,1474940198; Hm_lpvt_8fd158bb3e69c43ab5dd05882cf0b234=1474972769","DNT":"1","Host":"ip.zdaye.com","Referer":"http//ip.zdaye.com/","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36"}
url = 'http://ip.zdaye.com/img/m_c7a886994260fdf2.gif?2016-9-27%2018:50:15'
f=requests.get(url,headers=header)
print(f)
name=url[-39:-21]
path='codepic/'+name
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
img.save('codepic/'+'newcode.gif')
img = Image.open('codepic/'+'newcode.gif')
vcode =image_to_string(img)
print(vcode)
try:#r如果识别失败则默认为8080端口
    int(vcode)
except:
    vcode=8080
print(vcode)
# url='/img/m_410a03361a5abf24.gif?2016-9-27 13:37:40'
# print(url[-39:-19])