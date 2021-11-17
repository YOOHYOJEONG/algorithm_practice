# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 20:52:39 2021

@author: user
"""

#프로그래머스
#level01
#작은 수 제거하기

def solution(arr):
    
    if len(arr) < 2 : 
        return [-1]
    
    else :
        arr.remove(min(arr))
        
    return arr