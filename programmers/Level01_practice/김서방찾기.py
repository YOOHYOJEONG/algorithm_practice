# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 16:43:11 2021

@author: user
"""

#프로그래머스 level 01
#서울에서 김서방 찾기


## 풀이 1

seoul = ["Jane", "Kim"]


def solution(seoul):
    
    for i in range(len(seoul)) :
        if seoul[i] == "Kim" :
            answer = i
            
    return('김서방은 ' + str(answer) + '에 있다')

print(solution(seoul))

#%%

## 풀이 2

seoul = ["Jane", "Kim"]

def solution(seoul):
    
    answer = ''
    
    answer = "김서방은 {}에 있다".format(seoul.index('Kim'))
    
    return answer

print(solution(seoul))
