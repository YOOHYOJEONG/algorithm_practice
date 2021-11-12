# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 23:19:36 2021

@author: user
"""

#프로그래머스 
#level 01
#소수 찾기

### 소수 찾기는 '에라토스테네스의 체'로 구현할 수 있음!!!! ###

def solution(n) :
    
    a = [False,False] + [True]*(n-1)
    print(a)
    
    primes=[]

    for i in range(2,n+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                a[j] = False
    print(a)
    print(primes)
    return len(primes)
