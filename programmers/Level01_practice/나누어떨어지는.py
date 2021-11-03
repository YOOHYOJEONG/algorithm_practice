# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 15:29:07 2021

@author: user
"""

#프로그래머스 level 01
#나누어 떨어지는 숫자 배열


# arr = [5, 9, 7, 10]
# divisor = 5


arr = [3,2,6]
divisor = 10


def solution(arr, divisor):
    answer = []
    
    for num in arr :
        if num % divisor == 0 :
            answer.append(num)
    answer = sorted(answer)
        
    if len(answer) == 0 :
        answer.append(-1)
    
    return answer

print(solution(arr, divisor))