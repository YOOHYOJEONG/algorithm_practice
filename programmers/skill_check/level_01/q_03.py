# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 14:55:49 2021

@author: user
"""

#programers skill check
#level1
#3진법을 10진법으로


def solution(n):
    
    result = []
    
    while n > 0:
        n, r = divmod(n, 3)
        result.append(r)
      
    result = ''.join(map(str, reversed(result)))
                     
    rst = result[::-1]     

    return int(rst, 3)         

solution(127)
    