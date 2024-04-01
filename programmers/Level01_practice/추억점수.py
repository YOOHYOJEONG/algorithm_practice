# -*- coding: utf-8 -*-

# 프로그래머스
# level01
# 연습문제
# 추억 점수

def solution(name, yearning, photo):
    answer = []
    
    score = {name[i]:yearning[i] for i in range(len(name))}
    
    for pic in photo:
        pic_score = 0
        for n in pic:
            if n in score.keys():
                pic_score += score[n]
        answer.append(pic_score)
    
    return answer