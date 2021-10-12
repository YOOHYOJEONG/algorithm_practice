# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 19:44:08 2021

@author: user
"""

#이것이 코딩테스트다 - 나동빈
#chapter 06 정렬
#6-3
#삽입 정렬 소스코드

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)) :
    
    #i부터 1까지 감소하며 반복
    for j in range(i, 0, -1) :
        
        #한 칸씩 왼쪽으로 이동
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        
        #본인보다 작은 데이터 만나면 멈춤
        else :
            break

print(array)