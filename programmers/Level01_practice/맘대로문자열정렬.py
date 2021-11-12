# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 15:45:28 2021

@author: user
"""

#프로그래머스
#level01
#문자열 내 맘대로 정렬하기


def solution(strings, n):

    return sorted(strings, key= lambda strings : (strings[n], strings))