# -*- coding: utf-8 -*-

# 프로그래머스
# level01
# 연습문제
# 푸트 파이트 대회


def solution(food):
    
    foods = food[1:]
    food_cnt = []
    for cnt in foods:
        food_cnt.append(cnt//2)
    
    player1 = ''
    for i in range(1, len(foods)+1):
        player1 += str(i)*food_cnt[i-1]
    
    player2 = player1[::-1]

    return player1+'0'+player2