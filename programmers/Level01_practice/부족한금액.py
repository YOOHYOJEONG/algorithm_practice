# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 21:22:59 2021

@author: user
"""

#프로그래머스
#레벨1
#부족한 금액 계산


def solution(price, money, count):
    
    rst = 0
    for i in range(1, count+1) :
        rst += price*i
    if rst > money :
        answer = rst - money
    else :
        answer = 0
    
    return answer