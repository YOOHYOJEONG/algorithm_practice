# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 21:43:11 2021

@author: user
"""

#프로그래머스 level 01
#문자열 내림차순

def solution(s):
    answer = ''
    
    string = sorted(s)
    string = string[::-1]
    
    for s in string :
        answer += s
    
    return answer


#%%
### 다른 풀이 ###

def solution(s):
    answer = ''
    
    string = sorted(s)
    
    for s in string :
        answer += s
    
    return ''.join(reversed(answer))