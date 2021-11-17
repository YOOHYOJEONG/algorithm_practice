# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 14:12:56 2021

@author: user
"""

n = 123

def solution(n) :
    answer = []
    
    n = list(str(n))
        
    for i in range(len(n)) :
        answer.append(int(n[i]))
        
    return sum(answer)
    
print(solution(n))