# -*- coding: utf-8 -*-

# 프로그래머스
# level01
# 연습문제
# 덧칠하기


def solution(n, m, section):
    answer = 0
    color = 0
    
    for s in section:
        if s >= color:
            color = s+m
            answer += 1
    
    return answer