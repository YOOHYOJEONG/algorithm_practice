# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 21:39:07 2021

@author: user
"""

#프로그래머스
#레벨 1
#실패율

def solution(N, stages):
    answer = []
    
    all_num = len(stages)
    num = {}
    for i in range(1, N+1) :
        cnt = 0
        for step in stages :
            if step == i:
                cnt += 1
        if cnt == 0 :
            num[i] = 0
        else :
            num[i] = (cnt/all_num)
            
        all_num = all_num - cnt
    
    answer = sorted(num, key = lambda x : num[x], reverse = True)
    return answer