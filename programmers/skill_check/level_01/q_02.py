# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 14:41:03 2021

@author: user
"""

#programers skill check
#level1
#직사각형 * 만들기

a, b = map(int, input().strip().split(' '))

for i in range(b) :
    for j in range(a) :
        print('*', end = '')
    print()