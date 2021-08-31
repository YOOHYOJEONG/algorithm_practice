# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 08:40:21 2021

@author: user
"""

#이것이 코딩테스트다 - 나동빈
# 구현 chapter 04
# 4-3 왕실 나이트


#체스판 이동 경우의 수
#나이트는 2가지 경로로 움직임
#수평으로 두칸 이동 후 수직으로 한칸 이동
#숮딕으로 두칸 이동 후 수평으로 한칸 이동


#현재 나이트 위치 입력받기
input_data = input()

row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1


#나이트가 이동할 수 있는 방향 8가지 지정
steps = [(-2,-1), (-1, -2), (1,-2), (2, -1), (2,1), (1,2), (-1,2), (-2,1)]

#8가지 방향에 대해 각 위치로 이동 가능한지 확인
result = 0 
for step in steps :
    #원하는 이동 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    
    #이동 가능 하면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >=1 and next_column <= 8 :
        result += 1

print(result)