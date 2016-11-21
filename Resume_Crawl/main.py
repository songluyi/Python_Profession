# -*- coding: utf-8 -*-
# 2016/11/21 9:03
"""
-------------------------------------------------------------------------------
Function:   批量抓取58 简历的demo
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""
class crawl_demo(object):
    def __init__(self):
        self.deal_excel=[]
    #路径寻找方法封装
    def get_path(self,keyword):
        import os
        current_path=os.path.abspath(os.path.join(os.path.dirname('main.py'),os.path.pardir))
        new_path=current_path+'\\'+'note\\'
        FileList = []
        rootdir = new_path

        for root, subFolders, files in os.walk(rootdir):
            #排除特定的子目录,此处无需排出
            # if 'done' in subFolders:
            #     subFolders.remove('done')
            #查找特定扩展名的文件，只要包含'58'但不包含"new"字符串的文件，都会被包含
            for f in files:
                if f.find(keyword) != -1 and f.find('new')==-1:
                    FileList.append(os.path.join(root, f))

        return FileList

    def deal_excel(self):



if __name__=="__main__":
    spider=crawl_demo()
