# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 13:36:00 2021

@author: user
"""

#프로그래머스 
#level1 연습
#완주하지 못한 선수


#루프 이용한 풀이

def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    completion.append(1)
    
    for i in range(len(participant)):
        if participant[i] != completion[i] :
            answer = participant[i]
            
    return answer

#실행
participant = 	["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

print(solution(participant, completion))

### 이 문제 풀이는 동명이인을 처리하지 못함 ㅠ   ####


#%%

#hash 이용한 풀이

def solution(participant, competion) :
    answer = ''
    temp = 0
    dic = {}
    
    for part in participant :
        dic[hash(part)] = part   #dictionary에 key(hash값)-value(이름) 쌍을 추가, key 값은 중복 허용 안됨.
        temp += int(hash(part))  #hash값 중첩시킴
        
    for com in competion :
        temp -= hash(com)    #value에 대한 hash값을 제거해서 도착 안한 사람의 hash의 key값만 남음
        
    answer = dic[temp]
    
    return answer


#실행
participant = 	["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

print(solution(participant, completion))

