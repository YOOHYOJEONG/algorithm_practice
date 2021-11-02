# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 12:04:17 2021

@author: user
"""

#프로그래머스 level 01 
#카카오 기출 
#신규 아이디 추천


new_id = "...!@BaT#*..y.abcdefghijklm"

def solution(new_id):
    answer = ''
    
    #1
    new_id = new_id.lower()
    #2
    for s in new_id :
        if s.isalnum() or s in "-_." :
            answer += s
            
    
    #3
    while '..' in answer :
        answer = answer.replace('..', '.')

    #4
    if len(answer) >=1 :
        for i in range(len(answer)) :
            if answer[0] == '.' :
                answer = answer [1:]
            elif answer[-1] == '.' :
                answer = answer[:-1]
    
    #5
    if len(answer) == 0 :
        answer += 'a'
        
    #6
    elif len(answer) > 15 :
        answer = answer[:15]
        if answer[-1] == '.' :
            answer = answer[:-1]
        
    #7
    if len(answer) >0 and len(answer) < 3 :
        while len(answer) < 3:
            answer += answer[-1]
    
 
    return answer

print(solution(new_id))