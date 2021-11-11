# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 15:53:59 2021

@author: user
"""

#codility lesson 03
#PermMissingElem


A = [2,3,1,5]


#%%

### 첫시도 - 실패

def solution(A):
    answer = ''

    A = sorted(A)

    for i in range(len(A) -1) :
        if A[i+1] - A[i] != 1 :
            answer = A[i]+1

    return answer


#%%

### 두번재 시도 - 성공

def solution(A) :
    
    Sum = sum(A)
    
    full_sum = sum(range(1, len(A) +2))
    
    answer = full_sum - Sum
    
    return answer