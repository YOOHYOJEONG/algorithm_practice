# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 19:54:09 2021

@author: user
"""

#프로그래머스
#레벨1
#하샤드 수

x = 10

def solution(x):
    X = list(map(int, str(x)))
    Sum = sum(X)
    
    if x % Sum == 0 :
        return True
    else :
        return False
    
    
    
print(solution(x))