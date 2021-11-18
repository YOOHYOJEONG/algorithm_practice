# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 21:05:47 2021

@author: user
"""

#프로그래머스
#level02
#정렬
#가장 큰 수 


def solution(numbers):
    answer = ''
    
    num = list(map(str, numbers))
    num = sorted(num, key = lambda x: x*3, reverse = True)
    
    return str(int(''.join(num)))