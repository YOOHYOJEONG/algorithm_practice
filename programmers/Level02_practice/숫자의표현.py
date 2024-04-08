# -*- coding: utf-8 -*-

# 프로그래머스
# level02
# 연습문제
# 숫자의 표현

def solution(n):
    answer = 0
    
    for i in range(1, n+1):
        sum = 0
        for j in range(i, n+2):
            if sum > n :
                break
            elif sum == n:
                answer += 1
                break
            elif sum < n:
                sum += j
    
    return answer