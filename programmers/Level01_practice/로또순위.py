# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 17:30:33 2021

@author: user
"""

#프로그래머스
#level 01
#로또 최저 순위 최고 순위


def solution(lottos, win_nums):
    
    low_num = len(set(lottos) & set(win_nums))
    hight_num = low_num + lottos.count(0)
    
    win = [6,6,5,4,3,2,1]
    answer = [win[hight_num], win[low_num]]
    return answer