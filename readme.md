
#一：目的

**方便大家，防止重复造轮**

#二：项目内容

 **1.msg_pro 项目**

功能：定时发送天气消息 和笑话 到指定手机上

**需求点**

a. 女票原先需要，我觉得每天提醒挺麻烦的就写了一个，后来。。。她觉得我敷衍。。。然后。。。我就被一顿胖揍。。。大家以我为戒。。。

**实现方式**

a. 短信接口用的V2EX推荐的XX收费接口，天气调用的API 笑话自己爬的，随机取一条

**如何使用**


![](http://www.songluyi.com/wp-content/uploads/2016/10/QQ图片20161006173357-e1475746767130.png)

**2.ChangeHeaderToDict项目** 

功能：web端将浏览器header转换为json格式 目前已经完成

**需求点**

a. 每次写爬虫，看到chrome或者firefox里面的调试header request 并不是我们想要的list格式，咋办，自己写一个py转换吧，有这时间还不如手动加大括号 竖行编辑呢。而现在我写成一个html，只需要把header格式扔进页面，就出来你想要的json格式啦。放在自己博客上，利己利人~


a. bootstrap 前端搭建，js完成转换逻辑==

如图：
![](http://www.songluyi.com/wp-content/uploads/2016/09/QQ%E6%88%AA%E5%9B%BE20160920194200.png)

**3.Get_My_Proxy项目** 

功能：获取代理 并将有效代理输出

项目思路：
![](http://www.songluyi.com/wp-content/uploads/2016/10/QQ截图20161006182302.png)

**需求点**
a. 爬虫老喜欢被封，咋办捏，当然是用代理。网上优质的要钱，免费的不知道靠不靠谱，还要测试，可以尝试一下这个傻吊轮子

**实现方式**

a. Python将各个网站获得的代理获取后，插入到VPS的mysql数据库上，然后用拍簧片（html_package) 调用数据库数据显 （为啥要用PHP呢，因为js菜 其次是wordpress用php 放上去可以直接用）
如图：

![](http://www.songluyi.com/wp-content/uploads/2016/10/QQ截图20161006170524.png)

如果你希望有API，可以fork这个项目增加，目前校招中。。较忙~

**4.pytesser3**

功能：使pytesser支持3.x并且增加简单的验证码测试
**需求点

a.pytesser不支持3.x 并且我想测一下这个google的ocr到底咋样还得找一个合适的验证码 或者写一套自己的识别方法

**实现方法**

a.按照网上一步一步改写，然后去除垃圾功能，打包至pypi

**如何使用**

pip install pytesser3

剩下的就见md文档
[pytesser的说明](https://github.com/songluyi/pytesser3)


三：后续：

我真的好想做IT啊==
系里的老湿说了，十月中旬拿不到IT的offer就给我去做外贸去，哎。。。
大四狗，自学的Python，现在在凯捷做项目助理实习快半年了，求一个好心的企业收留==感激不尽


