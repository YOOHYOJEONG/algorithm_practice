# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 14:18:42 2021

@author: user
"""

#프로그래머스 level 01
#p와 y 개수

s = "pPoooyY"

def solution(s):
    answer = ''
    
    s = s.lower()
    
    p_num = 0
    y_num = 0
    
    for i in s :
        if i == 'p' :
            p_num += 1
        elif i == 'y' :
            y_num += 1
    
    if p_num == y_num :
        answer = True
    else :
        answer = False
        
    return answer
        
print(solution(s))