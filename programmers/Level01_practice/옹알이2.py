# -*- coding: utf-8 -*-

# 프로그래머스
# level01
# 연습문제
# 옹알이(2)

def solution(babbling):
    answer = 0
    keyword = ["aya", "ye", "woo", "ma"]
        
    for bab in babbling:
        for key in keyword:
            if key*2 not in bab:
                bab = bab.replace(key, ' ')
    
        if bab.isspace():
            answer += 1
            
    return answer