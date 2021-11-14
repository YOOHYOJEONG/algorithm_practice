# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 08:07:50 2021

@author: user
"""

#프로그래머스
#level 01
#시저암호

s = "a B z"
n = 4

def solution(s, n):
    s = list(s)
    
    for i in range(len(s)) :
        if s[i].isupper() :
            s[i] = chr((ord(s[i]) - ord('A') + n) % 26 + ord('A'))
        elif s[i].islower() :
            s[i] = chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))
        else :
            continue
            
    return ''.join(s)
    

print(solution(s,n))