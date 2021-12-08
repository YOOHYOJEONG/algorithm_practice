# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 16:17:50 2021

@author: user
"""

#프로그래머스 레벨1
#비밀지도


def solution(n, arr1, arr2):
    answer = []

    for i,j in zip(arr1, arr2) :
        ans12 = str(bin(i|j)[2:])  
        ans12 = ans12.zfill(n)
        ans12 = ans12.replace('0', ' ')
        ans12 = ans12.replace('1', '#')
        answer.append(ans12)
    return answer