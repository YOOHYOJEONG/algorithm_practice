# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 08:32:47 2021

@author: user
"""

#프로그래머스
#레벨2
#BFS/DFS
#타겟 넘버


def solution(numbers, target):
    answer = 0
    n = len(numbers)
    queue = [[numbers[0],0], [-1*numbers[0], 0]]
    
    while queue :
        temp, idx = queue.pop()
        idx += 1
        if idx < n :
            queue.append([temp + numbers[idx], idx])
            queue.append([temp - numbers[idx], idx])
        else :
            if temp == target:
                answer += 1
    
    return answer