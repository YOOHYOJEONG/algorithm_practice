# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 11:10:10 2021

@author: user
"""

#프로그래머스 level 01
#연습문제
#두 정수 사이의 합

#a, b = 3,5
a, b = 5,3

def solution(a, b):
    answer = 0
    
    if a == b :
        answer = a
    
    else :
        if a < b :
            for i in range(a, b+1) :
                answer += i
        elif a > b :
            for i in range(b, a+1):
                answer += i
    
    return answer


print(solution(a,b))