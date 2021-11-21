# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 17:00:50 2021

@author: user
"""

#프로그래머스 레벨1
#내적

def solution(a, b):
    
    answer = 0
    
    for i in range(len(a)) :
        answer += a[i]*b[i]
    
    return answer