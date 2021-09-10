# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 23:33:14 2021

@author: user
"""

#이것이 코딩테스트다 - 나동빈
#DFS chapter 05
#5-8


#DFS 예제

def dfs(graph, v, visited) :
    
    #현재 노드 방문 처리
    visited[v] = True
    print(v, end = ' ' )
    
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v] :
        if not visited[i] :
            dfs(graph, i, visited) 
            
#각 노드가 연결된 정보를 리스트로 표현
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
    
#각 노드가 방문된 정보를 리스트로 표현
visited = [False]*9
    
#dfs 함수 호출
dfs(graph, 1, visited)