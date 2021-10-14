# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 23:39:38 2021

@author: user
"""

#이것이 코딩테스트다 - 나동빈
#chaper 06 정렬
#6-5 퀵 정렬 소스 코드 수정 ver

array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array) :
    if len(array) <= 1 :
        return array
    
    pivot = array[0]
    tail = array[1:]
    
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]
    
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))