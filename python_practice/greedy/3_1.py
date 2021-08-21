# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 21:15:17 2021

@author: user
"""

# 이것이 코딩 테스트다 - 나동빈
# chapter 03 Greedy
# 3-1 거스름돈


n = 1260
count = 0

# 큰 단위 화폐부터 차례대로 확인해야 함.
coins = [500, 100, 50, 10]

for coin in coins :
    #해당 화폐로 거슬러 줄 수 있는 동전 개수 
    count += n // coin 
    n %= coin

print(count)