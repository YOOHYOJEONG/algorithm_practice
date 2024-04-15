# -*- coding: utf-8 -*-

# 프로그래머스
# level02
# 스택/큐
# 프로세스

def solution(priorities, location):
    answer = 0    
    queue = [(idx, p) for idx, p in enumerate(priorities)]

    priorities.sort(reverse=True)
    while True:
        if queue[0][0] == location and queue[0][1] == priorities[0]:
            return answer + 1
        
        elif queue[0][1] != priorities[0]:
            cur = queue.pop(0)
            queue.append(cur)
        else:
            passing = queue.pop(0)
            del priorities[0]
            answer += 1
            
    return answer