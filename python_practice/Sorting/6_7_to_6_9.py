# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 20:13:01 2021

@author: user
"""

#이것이 코딩테스트다 -나동빈
#chapter 06 정렬
#6-7 ~ 6-9

#6-7
#퀵 정렬과 동작 방식이 비슷한 병합 정렬
#리스트, 딕셔너리 자료형 등을 입력받아서 정렬된 결과를 출력.
#반환되는 결과는 리스트 자료형

array = [7,5,9,0,3,1,6,2,4,8]

result = sorted(array)
print(result)


#%%

#6-8
#리스트 변수 하나 있을 때 내부 원소를 바로 정렬.
#별도의 정렬된 리스트가 반환되지 않고 내부 원소가 바로 정렬.
array = [7,5,9,0,3,1,6,2,4,8]

array.sort()
print(array)

#%%

#6-9
#key 매개변수를 입력으로 받을 수 있음.
#key 값으로는 하나의 함수가 들어가야 하며 이는 정렬 기준이 됨.

array = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data) :
    return data[1]
    
result = sorted(array, key=setting)
print(result)