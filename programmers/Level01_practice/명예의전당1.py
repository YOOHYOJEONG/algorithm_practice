# -*- coding: utf-8 -*-

# 프로그래머스
# level01
# 연습문제
# 명예의 전당(1)

def solution(k, score):
    answer = []
    first = []
    for num in score:
        if len(first) == k:
            first.sort()
            if first[0] > num:
                answer.append(first[0])
            else:
                del first[0]
                first.append(num)
                answer.append(sorted(first)[0])
        else:
            first.append(num)
            answer.append(sorted(first)[0])
        
    return answer