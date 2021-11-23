# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 21:03:34 2021

@author: user
"""

#프로그래머스
#level 2
#기능 개발

progresses = [93, 30, 55]
speeds = [1, 30, 5]


def solution(progresses, speeds):
    answer = []
    day = 1
    cnt = 0
    
    print('p:', progresses)
    print('s:', speeds)
    
    while len(progresses) > 0 :
        if progresses[0] + speeds[0]*day >= 100 :
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
            
            print('if p:', progresses)
            print('if s:', speeds)
            print('if d:', day)
        
        else :
            day += 1
            if cnt > 0 :
                answer.append(cnt)
                cnt = 0
                print('el p:', progresses)
                print('el s:', speeds)
                print('el d:', day)
        print(day)
    answer.append(cnt)
    return answer


print(solution(progresses, speeds))