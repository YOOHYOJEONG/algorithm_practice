# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 16:28:44 2021

@author: user
"""

#프로그래머스
#레벨1
#콜라츠 추축



num = 6

def solution(num):
    answer = 0
    
    while num != 1 :
        if answer > 500 :
            return -1
        if num % 2 == 0 :
            num = num/2
        elif num % 2 == 1 :
            num = num*3 + 1
        answer += 1
    
    return answer


print(solution(num))