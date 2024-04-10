# -*- coding: utf-8 -*-

# 프로그래머스
# level01
# 연습문제
# 가장 가까운 같은 글자

def solution(s):
    answer = []
    dict = {}
    
    for index, word in enumerate(s):
        if word not in dict:
            answer.append(-1)
            dict[word] = index
    
        else:
            answer.append(index - dict[word])
            dict[word] = index
        
    return answer