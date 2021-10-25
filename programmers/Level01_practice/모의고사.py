# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 15:57:22 2021

@author: user
"""

#프로그래머스 
#level 01 
#완전탐색
#모의고사

#answers = [1,2,3,4,5]
answers = [1,3,2,4,2]

def solution(answers):
    
    answer = []
    score = [0,0,0]
    
    student1 = [1,2,3,4,5]
    student2 = [2,1,2,3,2,4,2,5]
    student3 = [3,3,1,1,2,2,4,4,5,5]
    
    for i in range(len(answers)) :
        if answers[i] == student1[i%5] :
            score[0] += 1
        if answers[i] == student2[i%8] :
            score[1] += 1
        if answers[i] == student3[i%10] :
            score[2] += 1
        
    for idx, num in enumerate(score) :
        if num == max(score) :
            answer.append(idx +1)
    
    return answer


print(solution(answers))