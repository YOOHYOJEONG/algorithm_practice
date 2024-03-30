# -*- coding: utf-8 -*-

# 프로그래머스
# level01
# 연습문제
# 삼총사

import itertools

def solution(number):
    answer = 0
    
    group = itertools.combinations(number, 3)
    
    answer = 0
    for gr in group:
        if sum(gr) == 0:
            answer += 1
            
    return answer