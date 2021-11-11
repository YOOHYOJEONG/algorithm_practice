# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 16:36:42 2021

@author: user
"""

#코딜리티 
#lesson 3
#tapeequilibrium

A = [3,1,2,4,3]


#%%
### 첫번째 시도 -53%(전부 시간 초과)

def solution(A):

    
    diff = []
    for p in range(1, len(A)) :
        tape1 = A[:p]
        tape2 = A[p:len(A)]
        print(tape1)
        print(tape2)
        
        sum1 = sum(tape1)
        sum2 = sum(tape2)
        print(sum1)
        print(sum2)
        
        diff.append(abs(sum1 - sum2))
    print(diff)
    
    diff = min(diff)

    return diff


#%%

### 두번째 시도 - 100%

def solution(A) :
    
    tape1 = 0
    tape2 = sum(A)
    
    diff = []
    
    for p in A :
        tape1 += p
        tape2 -= p
        
        diff.append(abs(tape1 - tape2))
    
    return min(diff[:-1])
        