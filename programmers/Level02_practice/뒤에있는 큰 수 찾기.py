# -*- coding: utf-8 -*-

# 프로그래머스
# level02
# 연습문제
# 뒤에 있는 큰 수 찾기


def solution(numbers):
    answer = [-1] * len(numbers)
    
    idx = []
    for i, num in enumerate(numbers):
        while idx and numbers[idx[-1]] < num:
            answer[idx.pop()] = num
        
        idx.append(i)
    
    return answer

