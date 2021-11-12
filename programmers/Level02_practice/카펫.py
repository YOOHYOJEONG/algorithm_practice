# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 22:17:38 2021

@author: user
"""

#프로그래머스
#level02
#카펫 사이즈 구하기


brown = 10
yellow = 2


#%% 

#첫번째 시도 - 2/3 맞음

def solution(brown, yellow):
    
    answer = []
    
    yellow_x = 0
    yellow_y = 0
    
    for i in range(1, yellow+1) :
        if yellow % i == 0 :
            yellow_x = int(yellow/i)
            yellow_y = i
    
    answer.append(yellow_y+2)
    answer.append(yellow_x+2)
    
    return answer

#%%

#두번째 시

def solution(brown, yellow):
    
    answer = []
    
    yellow_x = 0
    yellow_y = 0
    
    for i in range(1, yellow+1) :
        if yellow % i == 0 :
            yellow_x = int(yellow/i)
            yellow_y = i
            if yellow_x*2 + yellow_y*2 + 4 == brown :            
                answer.append(yellow_x+2)
                answer.append(yellow_y+2)
                
                return sorted(answer, reverse = True)
    
    return answer

print(solution(brown, yellow))