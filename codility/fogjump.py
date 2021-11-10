# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 23:26:21 2021

@author: user
"""

#codility lesoon03
#frog jump


#첫번재 시도 - 실패

X=10
Y=85
D=30

def solution(X,Y,D) :
    
    count = 0
    
    while X < Y :
        X = X+D
        count+=1
    
    return count


#%%

#두번째 시도

X=10
Y=85
D=30


def solution(X,Y,D):
    
    if X==Y :
        return 0

    dst = Y - X
    div, mod = divmod(dst, D)

    if not mod :
        return div
    else :
        return div+1