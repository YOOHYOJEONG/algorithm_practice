# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 07:53:31 2021

@author: user
"""

#이것이 코딩테스트다 - 나동빈
#chapter 03
#3-4 1이 될 때 까지


n, k = map(int, input().split())

result = 0

while n >= k :
    while n % k != 0 :
        n =+ 1
        result += 1
    
    n //= k
    result += 1
    
while n > 1 :
    n -= 1
    result += 1
    

print(result)