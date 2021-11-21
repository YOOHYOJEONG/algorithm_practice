# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 16:30:23 2021

@author: user
"""

#프로그래머스 레벨1
#음양 더하기

def solution(absolutes, signs):

    for i in range(len(absolutes)) :
        if signs[i] == True :
            absolutes[i] = absolutes[i]
        else :
            absolutes[i] = absolutes[i] - (absolutes[i]*2) 
    
    answer = sum(absolutes)
    
    return answer