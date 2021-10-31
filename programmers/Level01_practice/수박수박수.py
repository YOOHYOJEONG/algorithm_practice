# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 16:48:09 2021

@author: user
"""

#프로그래머스 레벨1
#수박수박수

n = 3

def solution(n):
    answer = ''
    string = '수박'
    
    ans = string * int(n/2 + 1)
    
    answer = ans[:n]
    
    return answer

print(solution(n))