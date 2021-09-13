# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 07:56:36 2021

@author: user
"""

#이것이 코딩테스트다 - 나동빈
#BFS chapter 05

#5-9 BFS 예제

from collections import deque


def bfs(graph, start, visited) :
    queue = deque([start])
    
    #현재 노드 방문 처리
    visited[start] = True
    
    #큐가 빌 때까지 반복
    while queue :
        
        #하나 원소 뽑아서 출력
        v = queue.popleft()
        print(v, end= ' ')
        
        #아직 방문하지 않은 원소들 큐에 삽입
        for i in graph[v] :
            if not visited[i] :
                queue.append(i)
                visited[i] = True
                
#각 노드가 연결된 정보
graph = [
        [], 
        [2,3,8], 
        [1,7], 
        [1,4,5],
        [3,5], 
        [3,4], 
        [7], 
        [2,6,8], 
        [1,7]
        ]

#각 원소가 방문한 정보
visited = [False] * 9

#정의된 BFS 함수 호출
bfs(graph, 1, visited)