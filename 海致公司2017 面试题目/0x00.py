# -*- coding: utf-8 -*-
"""
Created on Mon Apr 01 22:20:44 2013
这个是别人写的，我这里照搬，2016-10-9 来研究
@author: zzcwing
"""

class listnode: ##定义一个Node的数据类型，包含data和nextnode
    data=None
    nextnode=None
    def __init__(self,lndata):
        self.data=lndata

class slist: ##定义一个list的数据类型，链表长度(listsize) 头链表（head)和尾链表(tail)
    listsize=0
    head=None
    tail=None
    def __init__(self): ##初始化 将头链表和尾链表及链表长度清空
        self.head=None
        self.tail=None
        self.listsize=0
        
    def insertdata(self,value):  ##插入链表，始终插入到链表尾部
        newnode=listnode(value) ##建立一个插入链表的对象
        if self.head is None:   ##如果链表头为空，既链表本身为空,head和tail均为插入链表
            self.head=newnode  
            self.tail=newnode
            self.tail.nextnode=None  ##链表尾部指向None
            self.listsize=self.listsize+1 ##链表长度加1
        else:
            wnode=self.head  ##如果head不为空
            while wnode.nextnode is not None: ##遍历链表直到找到尾链表
                wnode=wnode.nextnode
            wnode.nextnode=newnode ##插入到链表尾部
            self.tail=newnode  ##插入链表作为尾链表
            self.tail.nextnode=None ##尾链表指向None
            self.listsize=self.listsize+1 ##链表长度加1
    def deldata(self,value):##删除链表，始终插入到链表尾部
        if self.head is None: ##如果链表为空，即头链表为空，pass
            pass
        elif self.head.data==value: ##如果头链表即为所要删除的值
            tmpnode=self.head  ##将头链表赋值给一个临时Node
            self.head=self.head.nextnode  ##头链表指向原头链表的下一个node
            tmpnode=None  ##清空临时Node
            self.listsize=self.listsize-1   ##链表长度-1      
        else: #如果链表不为空，且头链表不为空，链表长度至少>=1
            wnode=self.head.nextnode ##定义一个Node，从头链表开始遍历，寻找要删除值所在的node
            while (wnode is not None) and (wnode.data!=value):
                pnode=wnode ## 存储遍历过程中的前一个node
                wnode=wnode.nextnode
                
            if wnode!=None: ##如果Node此时不为空，意味着链表中存在我们要删除的Node
                if wnode.nextnode is None: ##如果node是尾链表
                    self.tail=pnode ##将尾链表指向pnode（要删除值所在node的前一个node）
                tmpnode=wnode ##将头链表赋值给一个临时Node
                pnode.nextnode=wnode.nextnode #将pnode指向node原本指向的下一个Node
                tmpnode=None ##清空临时Node
                self.listsize=self.listsize-1 ##链表长度-1  
    def listpint(self):
        if self.listsize==0: #如果链表长度为0 显示无链表
            print("no data in list")
        else:
            ##将node重置到头链表开始遍历
            wnode=self.head
            while (wnode is not None):
                print("--->",wnode.data) ##打印所有Node
                wnode=wnode.nextnode
if __name__=='__main__':
    link=slist()
    link.insertdata(1)
    link.insertdata(2)
    link.insertdata(3)
    link.insertdata(4)
    link.listpint()
    print("the size of list is",link.listsize)
    print("the head of list is ",link.head.data,"the tail of the list is",link.tail.data)
    print("")
    link.deldata(4)