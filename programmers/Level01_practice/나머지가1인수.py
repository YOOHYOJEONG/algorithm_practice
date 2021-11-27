# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 21:11:13 2021

@author: user
"""

#프로그래머스
#레벨1
#나머지가1인 수 찾기


def solution(n):
    rst = []
    for i in range(1, n+1) :
        if n%i == 1 :
            rst.append(i)
            
    answer = min(rst)
    
    return answer