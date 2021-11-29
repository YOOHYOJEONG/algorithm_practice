# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 15:33:52 2021

@author: user
"""

#프로그래머스
#레벨1
#폰켓몬



### 1차 시도 - 시간초과 실패


from itertools import combinations as cb

def solution(nums):
    answer = 0
    
    result = []
    for numb in cb(nums, int(len(nums)/2)) :
        result.append(len(set(numb)))
    
    answer = max(result)

    return answer  

#%%


#### 2차 시도 - 성공

def solution(nums):
    answer = 0
    
    num_len = len(set(nums))
    result = int(len(nums)/2)
    
    if result < num_len :
        answer = result
    else :
        answer = num_len
    
    return answer  