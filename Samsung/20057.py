# 마법사 상어와 토네이도
# 나선형으로 토네이도가 움직이기에 나선형을 어떻게 구현하는지 숙지

import math
dx = [0,1,0,-1]
dy = [-1,0,1,0]

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
s_x,s_y = n//2,n//2 # r,c direction
speed = 0 # speed
cnt = 1 # 움직임
ans = 0

left = [[-1,-1,0.1],[-1,0,0.07],[-1,1,0.01],[0,-2,0.05],[1,-1,0.1],[1,0,0.07],[1,1,0.01],[2,0,0.02],[-2,0,0.02],[0,-1,0]]
right = [[x, -y, z] for x,y,z in left]
down = [[-y, x, z] for x,y,z in left]
up = [[y, x, z] for x,y,z in left]

def move_wind(s_r,s_c,direction_list):
    global ans
    if s_c < 0:
        return
    total = 0
    for dx,dy,z in direction_list:
        nr = s_r + dx
        nc = s_c + dy
        if z == 0:
            new_sand = board[s_r][s_c] - total
        else:
            new_sand = int(board[s_r][s_c]*z)
            total += new_sand
        if 0 <= nr < n and 0 <= nc < n:
            board[nr][nc] += new_sand
        else:
            ans += new_sand
    board[s_r][s_c] = 0


def select_dir(d):
    if d == 0:
        return left
    elif d == 1:
        return down
    elif d == 2:
        return right
    elif d ==3:
        return up

for i in range(2*n-1):
    d = i % 4
    if d == 0 or d == 2:
        speed += 1
    dirc_list = select_dir(d)
    for k in range(speed):
        n_x = s_x + dx[d]
        n_y = s_y + dy[d]
        move_wind(n_x, n_y, dirc_list)  # y좌표, 방향
        s_x, s_y = n_x, n_y
print(ans)
