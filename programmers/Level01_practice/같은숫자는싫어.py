# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 11:21:26 2021

@author: user
"""

#프로그래머스 level 01
#같은 숫자는 싫어

arr = [1,1,3,3,0,1,1]
#arr = [4,4,4,3,3]

def solution(arr):
    answer = []
    
    for i in range(len(arr)) :
        if [arr[i]] != arr[i+1 : i+2]:
            answer.append(arr[i])
            
    return answer


print(solution(arr))