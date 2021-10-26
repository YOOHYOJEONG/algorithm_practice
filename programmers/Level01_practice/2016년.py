# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 08:13:33 2021

@author: user
"""

#프로그래머스
#level 01 연슴문제
#2016년


#datetime 모듈 사용하는 방법

a =5
b = 24

import datetime 

def solution(a, b):
    dic = {0:'MON', 1:'TUE', 2:'WED', 3:'THU', 4:'FRI', 5:'SAT', 6:'SUN'}
    
    date = datetime.datetime(2016,a,b).weekday()
        
    return dic[date]


print(solution(a,b))


#%%

#datetime 모듈 사용하지 않은 방법

a =5
b = 24


def solution(a, b):
    answer = ''
    
    dic = {
        1 : 31, 2 : 29, 3 : 31, 4 : 30, 5 : 31, 6 : 30, 7 : 31, 8 : 31, 9 : 30, 10 : 31, 11 : 30, 12: 31
    }
    
    day = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    
    count = 0

    #1월일 때 
    if a == 1 :
        count = b -1
        answer = day[count&7]
        
    #1월 아닐 때
    else :
        for i in range(1, a) :
            count += dic[i]
            
        count = count + b -1
        answer = day[count%7]
        
    return answer


print(solution(a,b))