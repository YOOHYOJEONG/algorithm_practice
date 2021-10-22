# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 14:05:01 2021

@author: user
"""

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

def solution(board, moves):
    answer = 0
    
    stack = list()
    
    for i in moves :
        for j in range(len(board)) :
            dolls = board[j][i-1]
            
            if dolls != 0 :
                stack.append(dolls)
                board[j][i-1] = 0
                break
            
        if len(stack) >= 2 and stack[-1] == stack[-2] :
            stack.pop()
            stack.pop()
            answer += 2
                
    
    return answer


print(solution(board, moves))