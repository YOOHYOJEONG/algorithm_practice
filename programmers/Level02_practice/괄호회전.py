# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 15:54:23 2021

@author: user
"""

#프로그래머스
#레벨2
#괄호 회전하기


def solution(s):
    answer = 0
    for i in range(len(s)):
        stack=[]
        temp=s[i:]+s[0:i]
        for j in range(len(s)):
            bl=True
            if temp[j]=='{' or temp[j]=='[' or temp[j]=='(':
                stack.append(temp[j])
            else:
                if not stack: #빈 스택
                    bl=False
                    break
                elif temp[j]=='}' and stack[-1]=='{':
                    stack.pop()
                elif temp[j]==']' and stack[-1]=='[':
                    stack.pop()
                elif temp[j]==')' and stack[-1]=='(':
                    stack.pop()
                else: #괄호 짝 안 맞을때
                    bl=False
                    break
        if bl and not stack:
            answer+=1

    return answer