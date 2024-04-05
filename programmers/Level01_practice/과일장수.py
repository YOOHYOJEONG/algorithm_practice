# -*- coding: utf-8 -*-

# 프로그래머스
# level01
# 연습문제
# 과일장수


def solution(k, m, score):
    
    score.sort(reverse=True)

    apples = score[:(len(score)//m)*m]
    
    benefits = 0
    for i in range(0, len(apples), m):
        benefit = score[i:i+m]
        
        benefits += min(benefit) * m
    
    return benefits
