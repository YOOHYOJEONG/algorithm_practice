# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 18:01:54 2021

@author: user
"""

#프로그래머스
#level 01
#소수 만들기

from itertools import combinations as cb

def solution(nums):
    cnt = 0
    for a in cb(nums, 3) :
        Sum = sum(a)
        for j in range(2, Sum ) :
            if Sum%j == 0 :
                break
        else :
            cnt += 1
            
    return cnt