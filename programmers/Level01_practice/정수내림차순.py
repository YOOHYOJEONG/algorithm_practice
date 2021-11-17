# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 20:32:30 2021

@author: user
"""

#프로그래머스
#레벨1
#정수 내림차순 정렬

def solution(n):
    answer = 0
    
    n = sorted(str(n))
    
    return int(''.join(reversed(n)))