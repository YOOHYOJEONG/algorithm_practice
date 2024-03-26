# -*- coding: utf-8 -*-

#프로그래머스
#level02
#완전탐색
#피로도

# 순열
from itertools import permutations

def solution1(k, dungeons):
    answer = -1
    
    dungeon_nums = len(dungeons)
    
    for permute in permutations(dungeons, dungeon_nums):
        limit_k = k
        cnt = 0
        
        for pm in permute:
            if limit_k >= pm[0]:
                limit_k -= pm[1]
                cnt += 1
        if cnt > answer:
            answer = cnt
    
    return answer


# dfs
from collections import deque

def solution2(k, dungeons):
    answer = -1
    
    queue = deque()
    queue.append((k, []))
    
    while queue:
        k, route = queue.popleft()
        for i in range(len(dungeons)):
            a, b = dungeons[i]
            if k >= a and i not in route:
                temp = route + [i]
                queue.append((k-b, temp))
            else:
                answer = max(answer, len(route))
    
    return answer

