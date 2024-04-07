# -*- coding: utf-8 -*-

# 프로그래머스
# level01
# 연습문제
# 크기가 작은 부분 문자열


def solution(t, p):
    answer = 0
    
    for i in range(0, len(t)-len(p)+1):
        if int(t[i:i+len(p)]) <= int(p):
            answer += 1
    
    return answer