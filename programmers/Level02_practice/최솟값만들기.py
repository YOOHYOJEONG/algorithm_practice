# -*- coding: utf-8 -*-

# 프로그래머스
# level02
# 
# 최솟값 만들기

def solution(A,B):
    answer = 0
    
    A.sort()
    B.sort(reverse=True)
    
    answer = 0
    for a, b in zip(A,B):
        answer += a*b

    return answer