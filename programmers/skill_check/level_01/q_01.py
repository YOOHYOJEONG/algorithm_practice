# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 14:18:53 2021

@author: user
"""

#programers skill check
#level1
#이상한 문자 만들기

def solution(s):
    
    string_s= s.split(" ")

    answer= []

    for word in string_s :
        w = ""
        for i in range(len(word)) :
            if i % 2 :
                w += word[i].lower()
            else :
                w += word[i].upper()
        answer.append(w)
        
    return ' '.join(answer)

print(solution('try hello world'))
