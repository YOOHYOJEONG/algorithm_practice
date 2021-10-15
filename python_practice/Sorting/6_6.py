# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 14:01:24 2021

@author: user
"""

#이것이 코딩테스트다 - 나동빈
#chapter 06 정렬
#6-6 계수 정렬 소스코드

#모든 원소의 값이 0보다 크거나 같을 때
array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

#모든 범위를 포함하는 리스트 선언
#모든 값은 0으로 초기화
count = [0] * (max(array)+1)

for i in range(len(array)) :
    count[array[i]] += 1
    

#리스트에 기록된 정렬 정보 확인
for i in range(len(count)) :
    for j in range(count[i]) :
        print(i, end=' ')