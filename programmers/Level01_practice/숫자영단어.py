# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 08:04:40 2021

@author: user
"""

#프로그래머스 level 01
#숫자 문자열과 영단어

s = "one4seveneight"
#s = "2three45sixseven"
#s = '1234'


def solution(s):
    answer = 0
    
    string = {'zero' : '0', 'one' : '1', 'two' :'2', 'three' :'3', 'four' : '4', 'five' :'5',
              'six' :'6', 'seven' : '7' , 'eight' : '8', 'nine' : '9'
        }
    
    for i, j in string.items() :
        s = s.replace(i,j)
    answer = int(s)

    
    return answer


print(solution(s))