# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 21:58:28 2021

@author: user
"""

#프로그래머스 Leveel 01
#두 개 뽑아서 더하기

#numbers = [2,1,3,4,1]
numbers = [5,0,2,7]

def solution(numbers):
    answer = []
    
    for i in range(len(numbers)) :
        for j in range(len(numbers)) :
            if i != j :
                answer.append(numbers[i] + numbers[j])
    answer = sorted(set(answer))
    return answer

print(solution(numbers))