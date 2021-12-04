# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 14:36:46 2021

@author: user
"""

#프로그래머스
#레벨1
#최소직사각형


import copy
def solution(sizes):
    answer = 0
    sizes_list = copy.deepcopy(sizes)
    
    w_list = []
    h_list = []
    for i in range(len(sizes_list)) :
        if sizes_list[i][0] < sizes_list[i][1] :
            sizes_list[i][0] = sizes[i][1]
            sizes_list[i][1] = sizes[i][0]
        w_list.append(sizes_list[i][0])
        h_list.append(sizes_list[i][1])
    
    answer = max(w_list) * max(h_list)
    
    return answer