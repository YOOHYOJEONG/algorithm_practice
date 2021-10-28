# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 11:03:59 2021

@author: user
"""

#프로그래머스 level 01
#연습문제
#가운데 글자 가져오기

#s = "abcde"
s = "qwer"

def solution(s):
    answer = ''
    if len(s) % 2 != 0 :
        idx = int(len(s) / 2)
        answer = s[idx]
    
    else :
        idx = int(len(s)/2)
        answer = s[idx-1:idx+1]
        
    return answer


print(solution(s))