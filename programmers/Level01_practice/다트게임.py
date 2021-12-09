# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 22:31:36 2021

@author: user
"""

#프로그래머스
#레벨1
#다트게임


import re

def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    
    p = re.compile("(\d+)([a-zA-Z])(\*|#)?")
    
    dart = p.findall(dartResult)
    
    for i in range(len(dart)):
        
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    
    return answer