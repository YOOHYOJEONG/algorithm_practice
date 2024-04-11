# -*- coding: utf-8 -*-

# 프로그래머스
# level02
# 연습문제
# 다음 큰 숫자


def solution(n):
    answer = n+1
    
    while True:
        if bin(answer).count('1') == bin(n).count('1'):
            break
        answer += 1
    
    return answer