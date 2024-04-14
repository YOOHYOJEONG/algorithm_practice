# -*- coding: utf-8 -*-

# 프로그래머스
# level01
# 연습문제
# 콜라 문제


def solution(a, b, n):
    answer = 0

    while n >= a:
        answer += b
        n = n - a + b

    return answer
