# -*- coding: utf-8 -*-
"""
Spyder Editor

"""

# 이것이 코딩 테스트다 - 나동빈
# chapter 03 Greedy

# 더하기 혹은 곱하기
# 연산은 왼쪽에서부터, +,x를 사용하여 가장 큰 값의 결과 구하기

data = list(map(int, input().split()))

result = data[0]

for i in range(1, len(data)) :
    
    if result <= 1 or data[i] <= 1 :
        result += data[i]
        
    else :
        result *= data[i]
        
print(result)
        

#%%

# 모험가 길드
# 본인의 공포도보다 많은 인원으로 그룹을 이루어야 함.
# 모든 사람이 그룹을 이룰 필요는 없음. 
# 만들 수 있는 그룹 수의 최대값 구하기

n = int(input())
data = list(map(int, input().split()))

# 만들어지는 총 그룹의 수
result = 0 

# 그룹 내에 포함된 모험가의 수
count = 0 


for i in data :
    # 현재 그룹에 모험가 한 명 추가하기
    count += 1
    
    if count >= i :
        # 모험가 수가 공포도보다 크다면 그룹 결성
        result += 1
        #그룹 결성 후 그룹 내 모험가 수 초기화
        count = 0
    
print(result)
