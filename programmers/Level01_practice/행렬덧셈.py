# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 17:09:44 2021

@author: user
"""

#프로그래머스
#레벨1
#행렬의 덧셈


def solution(arr1, arr2):    
    for i in range(len(arr1)) :
        for j in range(len(arr1[0])) :
            arr1[i][j] += arr2[i][j]
    return arr1