# -*- coding: utf-8 -*-

# 프로그래머스
# level02
# 월간 코드 챌린지 시즌1
# 이진 변환 반복하기


def solution(s):

    chg_cnt = 0
    zero_cnt = 0
    
    while True:
        if s == '1':
            break
        
        zero_cnt += s.count('0')
        s = s.replace('0', '')
        s = bin(len(s))[2:]
        
        chg_cnt += 1
    
    answer = [chg_cnt, zero_cnt]
    
    return answer