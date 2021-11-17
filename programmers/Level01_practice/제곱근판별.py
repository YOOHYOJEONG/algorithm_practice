# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 20:45:15 2021

@author: user
"""

#프로그래머스
#level 01
#정수 제곱근 판별


import math

def solution(n):
    if math.sqrt(n).is_integer() :
        return (math.sqrt(n)+1)**2
    else :
        return -1