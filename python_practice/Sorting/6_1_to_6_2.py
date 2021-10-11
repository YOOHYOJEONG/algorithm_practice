# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 21:40:22 2021

@author: user
"""

#이것이 코딩테스트다 - 나동빈
#Chapter 06 정렬
#선택 정렬 

#6-1 선택 정렬 소스 코드
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)) : 
    
    #가장 작은 원소의 인덱스
    min_index = i
    
    for j in range(i +1, len(array)) :
        if array[min_index] > array[j] :
            min_index = j
    
    #스와프(swqp)
    array[i], array[min_index] = array[min_index], array[i]
    
print(array)




#6-2 파이썬 스와프 소스코드

#인덱스 0과 인덱스 1 값 교체
array = [3,5]
array[0], array[1] = array[1], array[0]

print(array)