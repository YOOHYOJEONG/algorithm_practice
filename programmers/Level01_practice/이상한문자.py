# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 20:25:58 2021

@author: user
"""


s = "try hello world"

def solution(s):
    answer = []
    
    strings = s.split(" ")
    
    for i in range(len(strings)) :
        strings[i] = list(strings[i])
        for j in range(len(strings[i])) :
            if j % 2 == 0 :
                answer.append(strings[i][j].upper())
            elif j % 2 == 1 :
                answer.append(strings[i][j].lower())
        answer.append(" ")
    
    
    return ''.join(answer[:-1])


print(solution(s))