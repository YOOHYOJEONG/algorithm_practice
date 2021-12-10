# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 20:50:59 2021

@author: user
"""

#프로그래머스
#레벨2
#h-index

def solution(citations):

    h_max = 0
    cnt = 0
    for i in range(0,len(citations)+1):
        for j in citations:
            if j >= i:
                cnt += 1
        if cnt >= i:
            h_max = i
    
        cnt = 0
    
    return h_max