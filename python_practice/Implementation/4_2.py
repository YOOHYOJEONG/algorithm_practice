# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 07:53:31 2021

@author: user
"""

#이것이 코딩테스트다 - 나동빈
#구현 chapter 04
# 4-2 시각


#정수가 입력되면 모든 시각 중 3이 포함되는 경우의 수 구하기

#3중 for문으로 시각을 1씩 증가시키면서 3이 포함되어 있는지 확인하면 됨.

h = int(input())

count = 0
for i in range(h +1) :
    for j in range(60) :
        for k in range(60) :
            if '3' in str(i) + str(j) + str(k) :
                count += 1
                
print(count)