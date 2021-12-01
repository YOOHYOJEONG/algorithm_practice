# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 22:15:19 2021

@author: user
"""

#프로그래머스 레벨1
#약수 개수와 덧셈


def solution(left, right):
    answer = 0
    
    nums = range(left, right +1)
    cnt = 0
    
    for num in nums :
        for i in range(1, num+1) :
            if num%i == 0 :
                cnt += 1

        if cnt % 2 == 0 :
            answer += num
            cnt = 0
        else :
            answer -= num
            cnt = 0

    return answer