# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 16:50:12 2021

@author: user
"""

#프로그래머스 levle 01
#문자열 다루기 기본

def solution(s):
    answer = ''
    
    if len(s) == 4 or len(s) == 6 :
    
        if s.isnumeric():
            answer = True
        else :
            answer = False
    else :
        answer = False
        
    return answer