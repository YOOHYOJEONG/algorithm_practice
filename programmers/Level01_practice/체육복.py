# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 16:05:19 2021

@author: user
"""

#프로그래머스 level 01
#greedy
#체육복

n = 10
lost = [2, 4,6,8]
reserve = [1, 3, 5,8]


#첫 시도 - 3개 케이스 실패
def solution(n, lost, reserve):
    answer = 0
    
    lost_len = len(lost)
    
    for i in lost :
        if i in reserve :
            reserve.remove(i)
            lost.remove(i)
            lost_len -= 1

    for i in lost :
        if (i-1) in reserve :
            reserve.remove(i-1)
            lost_len -= 1
            
        elif (i+1) in reserve :
            reserve.remove(i+1)
            lost_len -= 1
     
    answer = n - lost_len
               
    return answer

print(solution(n, lost, reserve))

#%%

#두번째 시도 - 2개 케이스 실패
def solution(n, lost, reserve):
    answer = 0
    
    lost_len = len(lost)
    lost_copy = lost[:]
    
    for i in lost_copy :
        if i in reserve :
            reserve.remove(i)
            lost.remove(i)
            lost_len -= 1
        
    
    for i in reserve :
        if (i-1) in lost :
            lost.remove(i-1)
            lost_len -= 1
            
        elif (i+1) in lost :
            lost.remove(i+1)
            lost_len -= 1
    
    answer = n - lost_len
            
    return answer

#%%

#다른 사람 풀이
def solution(n, lost, reserve): 
    answer = 0 
    
    reserve_del = set(reserve)-set(lost) 
    lost_del = set(lost)-set(reserve) 
    
    for i in reserve_del: 
        if i-1 in lost_del: 
            lost_del.remove(i-1) 
            
        elif i+1 in lost_del: 
            lost_del.remove(i+1) 
            
    answer = n - len(lost_del)
    
    return answer