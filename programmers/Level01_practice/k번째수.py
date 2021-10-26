# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 19:28:59 2021

@author: user
"""

#프로그래머스 레벨1
#정렬 
#k번째 수

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

def solution(array, commands):
    answer = []
    
    for i in range(len(commands)) :
        a = commands[i][0]
        b = commands[i][1]
        c = commands[i][2]
        
        sorted_answer= sorted(array[a-1:b])
        answer.append(sorted_answer[c-1])
    
    return answer


print(solution(array, commands))