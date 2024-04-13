# -*- coding: utf-8 -*-

# 프로그래머스
# level02
# 연습문제
# 피보나치 수

def solution(n):
    f1 = 0
    f2 = 1
    
    F = [0]
    for i in range(n):
        f1, f2 = f2, f1 + f2    
        F.append(f1)
        
    return F[n]%1234567