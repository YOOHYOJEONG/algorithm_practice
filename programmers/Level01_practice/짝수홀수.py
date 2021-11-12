# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 14:34:13 2021

@author: user
"""


#프로그래머스
#level 01 
#짝수홀수

def solution(num):
    answer = ''
    
    if num % 2 == 0 :
        answer = 'Even'
    else :
        answer = 'Odd'
    
    return answer