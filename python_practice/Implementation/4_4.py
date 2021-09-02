# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 08:08:46 2021

@author: user
"""

#이것이 코딩 테스트다 - 나동빈
#구현 chapter 04
#4-3 게임 개발
#전형적인 시뮬레이션 문제. 


#각각의 칸은 육지(0) 또는 바다(1)
#캐릭터는 동서남북 중 한 곳을 바라봄.
#A는 북쪽으로부터 떨어진 칸의 개수 
#B는 서쪽으로부터 떨어진 칸의 개수
#캐릭터는 상화좌우로 움직이고 바다로 된 공간은 갈 수 없음.

###매뉴얼
#현 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 갈 곳을 정함.
#왼쪽 방향에 안 간 칸 있으면 왼쪽으로 회전 후 왼쪽으로 한칸 전진
#왼쪽 방향에 안 간 칸 없으면 왼쪽으로 회전만 함.
#네 방향 모두 가 봤거나 바다인 경우 바라보는 방향 유지한 채로 한 칸 뒤로 감
#뒤가 바다면 움직임 멈춤


#---------------------------------#

#N,M 공백으로 구분해서 입력 받기
n, m = map(int, input().split())

#방문 위치 저장 위해 맵 생성 후 0으로 초기화
d = [[0] * m for _ in range(n)]

#현재 캐릭터의 좌표, 방향 입력 받기
x, y, direction = map(int, input().split())

#현재 좌표 방문 처리
d[x][y] = 1


#전체 맵 정보 입력받기
array = []
for i in range(n) :
    array.append(list(map(int, input().split())))
    
#동서남북 방향 정의 : 북(-1,0), 동(0,1), 남(1,0), 서(0,-1)
dx = [-1,0,1,0]
dy = [0, 1, 0, -1]


#왼쪽으로 회전
def turn_left() :
    global direction 
    direction -= 1
    if direction == -1 :
        direction = 3
        

#시뮬레이션 시작
count = 1
turn_time = 0

while True :
    
    #왼쪽 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    #회전 후 정면에 안간 칸 존재 시
    if d[nx][ny] == 0 and array[nx][ny] == 0 :
        d[nx][ny] = 1
        x = nx
        y = ny
        
        count += 1
        turn_time = 0
        continue

    #회전 후 안간 칸 없거나 바다일 때
    else :
        turn_time += 1
       
        
    #네 방향 모두 갈 수 없을 때
    if turn_time == 4 :
        nx = x - dx[direction]
        ny = y - dy[direction]
        
        #뒤로 이동 가능할 때
        if array[nx][ny] == 0 :
            x = nx
            y = ny
        
        #뒤가 바다일 때
        else :
            break
        
        trun_time = 0
        

print(count)