# -*- coding: utf-8 -*-
"""
Spyder Editor

Created on Wed Aug 25 08:24:40 2021

@author: user
"""

# 이것이 코딩 테스트다 - 나동빈
# chapter 03 Greedy

# 숫자카드게임
# 여러 개의 숫자 카드 중 가장 높은 숫자가 쓰인 카드 한 장 뾥기
# N은 행의 개수 M은 열의 개수, 카드들은 N X M 형태로 놓여있음.
# 뽑고자하는 행 선택, 선택된 행에 포함된 카드 중 가장 숫자가 낮은 카드를 뽑아야 함.
# 최종적으로 가장 높은 숬자의 카드를 뽑을 수 있도록 전략을 세워야 함.


### min()사용

n,m = map(int,input().split())

result = 0

# 한줄씩 입력받음.
for i in range(n) :
    
    data = list(map(int, input().split()))
    
    #입력 받은 줄에서 가장 작은 수
    min_value = min(data)
    
    #가장 작은 수 중 가장 큰 수 찾
    result = max(result, min_value)
    
print(result)



