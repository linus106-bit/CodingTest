import copy

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
path = [[], [[0], [1], [2], [3]], [[0, 1], [2, 3]], [[0, 2], [2, 1], [1, 3], [3, 0]],
    [[3, 0, 2], [1, 3, 0], [0, 2, 1], [2, 1, 3]], [[0, 1, 2, 3]]]

def init():
    n, m = map(int, input().split())
    room = [list(map(int, input().split()))  for _ in range(n)]
    return n,m, room

def find_cctv(n,m, room):
    cctv_list = []
    for i in range(n):
        for j in range(m):
            if 0 < room[i][j] < 6:
                cctv_list.append([i, j, room[i][j]])
    return cctv_list

def count_room(room):
    cnt = 0
    for i in range(len(room)): 
        cnt += room[i].count(0)
    return cnt



def cctv_watching(x,y, path, room):
    for k in path:
        new_x = x
        new_y = y
        while True:
            new_x += dx[k]
            new_y += dy[k]
            if new_x >= 0 and new_x < m and new_y >= 0 and new_y < n and room[new_y][new_x] != 6:
                if room[new_y][new_x] == 0:
                    room[new_y][new_x] = '#'
            else:
                break


def dfs(room, cctv_list, step):
    global answer
    new_room = copy.deepcopy(room)
    if step == len(cctv_list):
        cnt = count_room(new_room)
        answer = min(answer,cnt)
        return
    y,x,cctv_num = cctv_list[step][0], cctv_list[step][1], cctv_list[step][2]
    for i in path[cctv_num]:
        cctv_watching(x,y,i,new_room)
        dfs(new_room,cctv_list,step+1)
        new_room = copy.deepcopy(room)  # 끝나고 이동하기 전 room으로 다시 되돌리기

    

n,m, room = init()
answer = n*m
cctv_list = find_cctv(n,m,room)
dfs(room, cctv_list, step=0)
print(answer)

    

