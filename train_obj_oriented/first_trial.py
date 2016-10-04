# -*- coding: utf-8 -*-
# 2016/10/1 23:27
"""
-------------------------------------------------------------------------------
Function:
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""

class Card:
    def __init__(self, rank, suit):
        self.suit= suit
        self.rank= rank
        self.hard, self.soft =self._points()
    def _points(self):
        print('基类已经被调用，谢谢！')
        return 0,0

class NumberCard(Card):
    def _points(self):
        return int(self.rank), int(self.rank)
class Acecard(Card):
    def _points(self):
        return 1,11

class FaceCard(Card):
    def _points(self):
        return 10,10


Cards=[Acecard('A','黑桃'),NumberCard('2','黑桃'),NumberCard('3','黑桃')]
print(Cards)

#太有意思了！！！！

