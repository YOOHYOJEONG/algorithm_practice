# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 17:02:53 2021

@author: user
"""

#프로그래머스
#레벨2
#최댓값과 최솟값

def solution(s):
    answer = ''
    s = list(map(int,s.split()))
    answer += str(min(s))
    answer += ' '
    answer += str(max(s))
    return answer