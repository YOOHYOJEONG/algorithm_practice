# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 21:04:57 2021

@author: user
"""

#프로그래머스 레벨2
#전화번호 목록


### 첫번째 시도 - 테케, 효율성 왕창 틀림 
def solution(phone_book):
    answer = True    
    
    sorted(phone_book)
    book_list = phone_book[1:]
    
    for i in range(len(book_list)) :
        if phone_book[0] in book_list[i] :
            phone_book.remove(phone_book[i+1])   
            
    if len(phone_book) != len(book_list) +1 :
        answer = False
        
    return answer

#%%


### 두번째 시도 - 테스트케이스 2개, 효율성 1/4 틀림

def solution(phone_book):
    answer = True    
    
    phone_book = sorted(phone_book)
    
    for i in range(1, len(phone_book)) :
        if phone_book[i].startswith(phone_book[0]) :
            answer = False
            break
        
    return answer


#%%

### 세번째 시도  - 통과

def solution(phone_book):
    answer = True    
    
    phone_book = sorted(phone_book)
    
    for i, j in zip(phone_book, phone_book[1:]) :
        if j.startswith(i) :
            answer = False
        
    return answer