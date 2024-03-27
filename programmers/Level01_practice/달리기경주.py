# -*- coding: utf-8 -*-

# 프로그래머스
# level01
# 연습문제
# 달리기 경주


# 시간 초과
def solution1(players, callings):
    answer = []
    
    for i in range(len(callings)):
        call_score = players.index(callings[i])
        print('call score : ', call_score)

        players.pop(call_score)
        print(players)

        if i > 0:
            if callings[i] == callings[i-1]:
                new_score = call_score-1
            else:
                new_score = call_score-1
            
        elif i == 0:
            new_score = call_score-1
        
        print('new_score : ', new_score)

        players.insert(new_score, callings[i])

        print(players)
    
    answer = players
    
    return answer


# 정답 - 통과
def solution(players, callings):
    answer = []
    
    race = {key: i for i, key in enumerate(players)}
    print(race)

    for call in callings:
        score = race[call]
        race[call] -= 1
        
        race[players[score-1]] += 1
        players[score-1], players[score]  = players[score], players[score-1]
    
    print(players)

    answer = players
    
    return answer

answer = solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"])

print(answer)