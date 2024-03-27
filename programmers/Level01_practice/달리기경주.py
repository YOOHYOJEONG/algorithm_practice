# -*- coding: utf-8 -*-

# 프로그래머스
# level01
# 연습문제
# 달리기 경주


# 시간 초과
def solution1(players, callings):
    
    for i in range(len(callings)):
        call_score = players.index(callings[i])

        players.pop(call_score)

        new_score = call_score-1

        players.insert(new_score, callings[i])
    
    return players

# 정답 - 통과
def solution(players, callings):

    race = {key: i for i, key in enumerate(players)}

    for call in callings:
        score = race[call]
        race[call] -= 1
        
        race[players[score-1]] += 1
        players[score-1], players[score]  = players[score], players[score-1]
    
    
    return players

answer = solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"])

print(answer)