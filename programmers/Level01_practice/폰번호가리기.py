# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 14:45:22 2021

@author: user
"""

#프로그래머스
#level 01 
#핸드폰 번호 가리기

phone_number = "01033334444"

def solution(phone_number):
    answer = ''
    
    first = '*' * (len(phone_number)-4)
    
    answer = first + phone_number[-4:]
    
    return answer