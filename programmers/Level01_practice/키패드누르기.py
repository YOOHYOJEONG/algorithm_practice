# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 17:07:25 2021

@author: user
"""

#프로그래머스 level01
#카카오 인턴쉽 기출
#키패드 누르기

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = 'right'
#result : "LRLLLRLLRRL"

# numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
# hand = 'left'
#result : "LRLLRRLLLRR"

def solution(numbers, hand):
    answer = ''

    pad = {'1':(0,0), '2':(0,1), '3':(0,2),
           '4':(1,0), '5':(1,1), '6':(1,2),
           '7':(2,0), '8':(2,1), '9':(2,2),
           '*':(3,0), '0':(3,1), '#':(3,2)
        }
    
    left = pad['*']
    right = pad['#']
    
    for num in numbers :
        
        if num in [1,4,7] :
            answer += 'L'
            left = pad[str(num)]
        elif num in [3,6,9] :
            answer += 'R'
            right = pad[str(num)]
        else :
            left_dis = abs(left[0] - pad[str(num)][0]) + abs(left[1] - pad[str(num)][1])
            right_dis = abs(right[0] - pad[str(num)][0]) + abs(right[1] - pad[str(num)][1])
            
            if left_dis < right_dis :
                answer += 'L'
                left = pad[str(num)]
                
            elif left_dis > right_dis :
                answer += 'R'
                right = pad[str(num)]
                
            else :
                if hand == 'right' :
                    answer += 'R'
                    right = pad[str(num)]
                else :
                    answer += 'L'
                    left = pad[str(num)]
    
    return answer

print(solution(numbers, hand))