# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 22:09:43 2021

@author: user
"""

#이것이 코딩테스트다 - 나동빈
#chaper05
#5-11 미로 탈출

from collections import deque

n,m = map(int, input().split())

graph = []
for i in range(n) :
    graph.append(list(map(int, input())))

#이동할 네 방향 정의(상,하,좌,우)
dx = [-1,1, 0, 0]
dy = [0,0,-1,1]

#BFS 소스코드 구현
def bfs(x, y) :
    queue = deque()
    queue.append((x,y))
    
    #큐 빌 때까지 반복
    while queue :
        x,y = queue.popleft()
        
        #현재 위치에서 네 방향으로의 위치 확인
        for i  in range(4) :
            nx = x + dy[i]
            ny = y + dy[i]
            
            #공간 벗어난 경우에는 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m :
                continue
            #벽인 경우도 무시
            if graph[nx][ny] == 0 :
                continue
            #해당 노드 처음 방문했을 때만 최단 거리 기록
            if graph[nx][ny] == 1 :
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    
    #가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n-1][m-1]

#BFS 수행 결과
print(bfs(0,0))
