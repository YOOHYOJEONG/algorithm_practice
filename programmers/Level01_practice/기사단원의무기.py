# -*- coding: utf-8 -*-

# 프로그래머스
# level01
# 연습문제
# 기사 단원의 무기


# 시간초과 답
def solution(number, limit, power):
    divs = []
    for i in range(1, number+1):
        div = 0
        for j in range(1, i+1):
            if i % j == 0:
                div += 1
        if div > limit:
            div = power
        divs.append(div)
    return sum(divs)


# 정답
def solution(num, lim, pow):
    divs = [1]
    for i in range(2, num+1):
        cnt = 0
        for j in range(1, int(i**(1/2)+1)):
            if i % j == 0:
                cnt += 1
                if j**2 != i:
                    cnt+=1
        if cnt > lim:
            cnt = pow
            divs.append(cnt)
        else:    
            divs.append(cnt)
            
    return sum(divs)
