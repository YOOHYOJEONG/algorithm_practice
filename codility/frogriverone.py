# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 20:43:45 2021

@author: user
"""

#코딜리티
#lesson 4
#frogriverone


def solution(X, A):
    
    cnt = [0]*(X)
    result = 0
    
    for idx, i in enumerate(A):
        
        if cnt[i-1] == 0 :
            cnt[i-1] = 1
            result += 1

            if result == X:
                return idx

    return  -1