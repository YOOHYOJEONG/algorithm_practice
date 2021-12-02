# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 21:13:43 2021

@author: user
"""

#프로그래머스
#레벨1
#3진수 뒤집기

def solution(n):
    answer = 0
    
    three_str = ''
    while n >= 1 : 
        n,b = divmod(n,3)
        three_str += str(b)
    answer = int(three_str, 3)
    return answer