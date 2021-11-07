# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 15:36:14 2021

@author: user
"""

#코딜리티 
#lesson 01 
#이진수


#N = 1041
#N = 32
N = 15

def solution(N):
    
    answer = ''
    
    bin_N = bin(N)
    bin_N = bin_N[2:]
    
    
    idx_ls = []    
    for idx, i in enumerate(bin_N) :
        if i == '1' :
            idx_ls.append(idx)

    if len(idx_ls) < 2 :
        return 0
        
    else :        
        grap = []
        for i in range(len(idx_ls)-1) :
            grap.append(idx_ls[i+1] - idx_ls[i] -1)
        
        answer = max(grap)
        
        return answer


print(solution(N))