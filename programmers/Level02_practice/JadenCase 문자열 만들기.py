# -*- coding: utf-8 -*-

# 프로그래머스
# level02
# 연습문제
# JadenCase 문자열 만들기


# 런타임 에러
def solution1(s):
    answer = []
    
    check = s.split(' ')
    
    for text in check:
        if text[0].isdigit():
            text.lower()
            answer.append(text)
        else:
            answer.append(text[0].upper() + text[1:].lower())
    return ' '.join(answer)


# 통과 
def solution(s):
    
    check = s.split(' ')
    
    for i in range(len(check)):
        check[i] = check[i].capitalize()
        
    return ' '.join(check)
