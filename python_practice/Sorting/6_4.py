# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 20:44:48 2021

@author: user
"""


#이것이 코딩테스트다 - 나동빈
#chaper 06 정렬
#6-4 퀵 정렬 소스 코드

array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end) :
    #원소가 하나이면 종료
    if start >= end : 
        return
    
    #pivot은 첫번재 원소
    pivot = start
    left = start + 1
    right = end
    
    while left <= right :
        
        #pivot보다 큰 데이터 찾을때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        
        #pivot보다 작은 데이터 찾을 때 까지 반복
        while right > start and array[right] >= array[pivot] :
            right -= 1
            
        #엇갈린 경우 작은 데이터와 pivot 교체
        if left > right : 
            array[right], array[pivot] = array[pivot], array[right]
        
        #아니면 작은 데이터와 큰 데이터 교체
        else :
            array[left], array[right] = array[right], array[left]
    
    #왼쪽, 오른쪽에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right+1, end)
    
quick_sort(array, 0, len(array)-1)
print(array)

#시간 면에서는 비효율적이지만 직관적이고 기억하기 쉬움.