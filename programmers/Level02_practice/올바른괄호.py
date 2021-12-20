# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 19:01:31 2021

@author: user
"""

#프로그래머스
#레벨2
#올바른 괄호


def solution(s):
    stack=[]

    for i in s:
        if i=='(':
            stack.append(1)
        else:
            if stack :
                stack.pop()
            else :
                return False
    if stack :
        return False
    else :
        return True