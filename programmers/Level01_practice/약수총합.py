# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 14:32:56 2021

@author: user
"""

#프로그래머스
#level 01 
#약수 총 합 구하기

def solution(n):
    answer = 0
    
    for i in range(1, n+1) :
        if n%i == 0 :
            answer += i
    
    return answer