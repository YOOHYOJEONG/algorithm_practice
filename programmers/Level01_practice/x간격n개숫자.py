# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 20:47:57 2021

@author: user
"""

#프로그래머스
#레벨1
#x만큼 간격이 있는 n개의 숫자

def solution(x, n):
    answer = []
    for i in range(0,n) :
        answer.append(x+i*x)
    return answer