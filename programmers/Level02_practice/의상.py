# -*- coding: utf-8 -*-

#프로그래머스
#level02
#해시
#의상

def solution(clothes):
    answer = 1
    
    closet = {}
    for Kind, Type in clothes:
        if Type not in closet.keys():
            closet[Type] = [Kind]
        else:
            closet[Type] += [Kind]
    
    for key, value in closet.items():
        answer *= (len(value)+1)
    
    return answer -1