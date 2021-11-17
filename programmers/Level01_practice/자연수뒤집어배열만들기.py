# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 20:23:13 2021

@author: user
"""

#프로그래머스
#level 01
#자연수 뒤집어서 배열 만들기

n = 12345

def solution(n) :
    answer = []
    
    n = list(str(n))
    
    for i in range(len(n)) :
        answer.append(int(n[len(n) -1 -i]))
        
    return answer
    
    
print(solution(n))