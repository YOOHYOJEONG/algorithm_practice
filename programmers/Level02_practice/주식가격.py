# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 19:47:22 2021

@author: user
"""

#프로그래머스 레벨2
#주식가격

from collections import deque

def solution(prices):
    answer = []
    
    prices = deque(prices)
    
    while prices :
        temp = prices.popleft()
        cnt = 0
        
        for i in prices :
            cnt += 1
            if i < temp :
                break
        answer.append(cnt)
    
    return answer