
# 이것이 코딩 테스트다 - 나동빈
# chapter 03 Greedy
# 3-2 큰 수 법칙
# 풀이시간 30분, 시간 제한 1초

import time

#n : 자연수 개수
#m : 더할 횟수
#k : 연속해서 더할 수 있는 최대 횟수

#n,m, k 공백으로 구분해서 입력받기 
n, m, k = map(int, input().split())

#n개의 자연수를 공백으로 구분해서 입력받기
data = list(map(int,input().split()))

start = time.time()

#입력받은 데이터 정렬
data.sort()

# 가장 큰 값과 두번째로 큰 값만 저장하면 됨.
data1 = data[n-1]   # 가장 큰 값
data2 = data[n-2]   # 두번째로 큰 값


result = 0

while True :
    if m == 0 : # m이 0이면 반복문 끝남.
        break 
    
    for i in range(k) :
        result += data1
        m -= 1  # 더해질 때 마다 1씩 뺌.
    
    result += data2   # 가장 큰 수가 m번 더해진 후 두번째로 큰 수가 더해짐
    m -= 1   # 더할 때 마다 1씩 뺌. 

print(result)


end = time.time()

print("time : ", end-start)


#%%
### 위의 코드도 맞긴 하지만, M의 크기가 100억 이상처럼 커지면 시간초과될 것.
#반복되는 수열에 대해 파악하여 효율적으로 코드를 짤 수 있어야 함. 

n, m, k = map(int, input().split())

numbers = list(map(int, input().split()))

numbers.sort()

number1 = data[n-1]
number2 = data[n-2]

# 가장 큰 수가 더해지는 횟수에 대한 수열을 파악 후 계산해야 함.
count = int(m / (k+1) *k)
count += m % (k+1)

result = 0 

#가장 큰 수 더하기
result += (count) * number1

#두번재로 큰 수 더하기
result += (m - count) * number2

print(result)