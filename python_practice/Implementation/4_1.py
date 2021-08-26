# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 08:05:37 2021

@author: user
"""

# 이것이 코딩 테스트다 - 나동빈
# chapter 04 Implementation(구현)
#4-1 상하좌우

n = int(input())

x, y = 1,1
plans = list(input().split())

dx = [0,0,-1,1]
dy = [-1,1,0,0]

move_types = ['L', 'R', 'U', 'D']

for plan in plans :
    for i in range(len(move_types)) :
        if plan == move_types[i] :
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny <1 or nx > n or ny >n :
        continue
    
    x, y = nx, ny
    
print(nx, ny)


