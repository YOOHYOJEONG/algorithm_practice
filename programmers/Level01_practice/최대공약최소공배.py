# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 14:47:55 2021

@author: user
"""

#프로그래머스 level 01
#최대 공약수 최소 공배수 구하기


n= 3
m =12

#최대공약수는 유클리드 호제법 알고리즘을 사용하여 구할 수 있음.
def gcd(n,m) :
    while m > 0 :
        n, m = m, n%m
    return n   #여기서 n이 최대공약수가 됨


#최소공배수는 n,m의 곱을 n,m의 최대 공약수로 나누면 나옴.
def lcm(n,m) :
    return n*m / gcd(n,m)


#이 둘의 함수를 사용해서 answer를 구하면 됨.
def solution(n,m) :
    answer = []
    answer.append(gcd(n,m))
    answer.append(lcm(n,m))
    
    return answer