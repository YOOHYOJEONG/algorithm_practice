# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 23:11:23 2021

@author: user
"""

#프로그래머스
#레벨1
#예산


def solution(d, budget):
    answer = 0
    
    d = sorted(d)
    
    for i in range(len(d)) :
        if budget >= d[i] :
            budget -= d[i]
            answer += 1
    
    return answer