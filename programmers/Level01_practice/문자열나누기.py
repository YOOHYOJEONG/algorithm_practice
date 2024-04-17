# -*- coding: utf-8 -*-

# 프로그래머스
# level01
# 연습문제
# 문자열 나누기


def solution(s):
    cnt1 = 0
    cnt2 = 0
    answer = 0
    
    cur = ""
    for i in s:
        cur += i
        cnt1 = cur.count(cur[0])
        cnt2 = len(cur) - cnt1

        if cnt1 == cnt2:
            cur = ""
            answer += 1
            
    if len(cur) == 0:
        return answer
    else:
        return answer + 1
        