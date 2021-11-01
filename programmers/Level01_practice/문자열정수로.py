# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 16:05:07 2021

@author: user
"""

#프로그래머스 level 01
#문자열을 정수로 바꾸기

def solution(s):
    answer = 0
    if s[0] == '+' :
        answer = int(s[1:])
    else :
        answer = int(s)
    return answer