# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 08:10:55 2021

@author: user
"""

#이것이 코딩테스트다 - 나동빈
#BFS chapter 05

#5-10 예제
#DFS로 해결할 수 있음.


#N, M 공백으로 구분하여 입력받기
n,m = map(int, input().split())

#2차원 리스트 맵 정보 입력
graph = []
for i in range(n) :
    graph.append(list(map(int, input())))
    
#DFS로 특정 노드 방문 후 연결된 모든 노드 방문
def dfs(x, y) :
    #범위 벗어나면 종료
    if x <= -1 or x >= n or y <= -1 or y >= m :
        return False
    
    #현재 노드 방문 안했을 때
    if graph[x][y] == 0 :
        #방문처리
        graph[x][y] = 1
        
        #상,하,좌,우 위치 모두 재귀적으로 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        
        return True
    
    return False

#모든 노드(위치)에 대해 음료수 채우기
result = 0
for i in range(n) :
    for j in range(m) :
        #현재 위치에서 DFS 수행
        if dfs(i, j) == True :
            result += 1

#정답 출력
print(result)