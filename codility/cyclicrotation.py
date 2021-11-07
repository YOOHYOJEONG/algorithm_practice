# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 08:30:52 2021

@author: user
"""

#코딜리티
#lesson 2
#CyclicRotation


def solution(A, K):
    if len(A) > 1 :
        for i in range(K) :
            a = A.pop()
            A.insert(0, a)
            
    return A