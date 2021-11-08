# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 08:21:03 2021

@author: user
"""

#코딜리티 
#lesson 02
#A odd occurrences


A = [9,3,9,3,7]

from collections import Counter

def solution(A):

    if len(A) == 1 :
        return A[0]
        
    else :
        counted = Counter(A)

        for key, val in counted.items() :
            if val % 2 != 0 :
                return key

