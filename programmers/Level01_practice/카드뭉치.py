# -*- coding: utf-8 -*-

# 프로그래머스
# level01
# 연습문제
# 카드 뭉치


def solution(cards1, cards2, goal):
    answer = "Yes"
    for g in goal:
        if len(cards1) > 0 and g == cards1[0]:
            cards1.pop(0)
        elif len(cards2) > 0 and g == cards2[0]:
            cards2.pop(0)
        else:
            answer = "No"
    return answer