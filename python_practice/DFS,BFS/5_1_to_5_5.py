# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#이것이 코딩 테스트다 - 나동빈
#chapter 05 DFS/BFS
#자료구조 기초 5-1 ~ 5-6

#stack is Fisrt In Last Out
#5-1

stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)  #최하단 원수부터 출력
print(stack[::-1])   #최상단 원소부터 출력


#%%

#Queue is First In First Out
#5-2

#큐 구현 위해 deque 라이브러리 사용함.
from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(4)
queue.popleft()

print(queue)   #먼저 들어온 순서대로 출력
queue.reverse()   #다음 출력을 위해 역순으로 변경
print(queue)   #나중에 들어온 원소부터 출력
print(list(queue))


#%%

#재귀함수 : 자기 자신을 다시 호출하는 함수
#5-3

def recursive_function() :
    print('재귀함수')
    recursive_function()
    
recursive_function()

#실행하면 무한히 출력하다 오류 출력 후 멈춤
#재귀 최대 깊이 초과했다는 내용.
#파이썬 인터프리터는 호출 횟수 제한이 있는데 이 한계를 벗어났기 때문
#마치 뫼비우스의 띠 같은


#%%

#재귀함수 종료 조건
#5-4

def recursive_function(i) :
    if i == 100 :
        return
    print(i, '번재 재귀 함수에서', i+1, '번째 지귀 함수를 호출')
    recursive_function(i+1)
    print(i, '번째 재귀 함수 종료')

recursive_function(1)


#%%

#팩토리얼 예제
#5-5

#첫번째 방법
#반복적으로 구현한 n!

def factorial_iterative(n) :
    result = 1
    for i in range(1, n+1) :
        result *= i
    return result


#재귀적으로 구현한 n!

def factorial_recursive(n) :
    if n < 1 :
        return 1
    return n * factorial_recursive(n-1)

print('반복 : ' , factorial_iterative(5))
print('재귀 : ', factorial_recursive(5))