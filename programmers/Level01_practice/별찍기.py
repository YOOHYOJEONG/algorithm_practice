# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 22:23:19 2021

@author: user
"""

#프로그래머스 레벨1
#직사각 별 찍기

a, b = map(int, input().strip().split(' '))
for i in range(0, b) :
    for j in range(0, a) :
        print('*', end = '')
    print()