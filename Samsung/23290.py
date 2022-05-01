dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]
sdx = [-1,0,1,0]
sdy = [0,-1,0,1]

def deepcopy(graph):
    new = [[[] for _ in range(4)] for __ in range(4)]
    for i in range(4):
        for j in range(4):
            new[i][j] = graph[i][j][:]
    return new

m,s = map(int,input().split())
graph = [[[] for _ in range(4)] for __ in range(4)]
fish_list=[]

for i in range(m):
    r,c,d = map(int,input().split())
    graph[r-1][c-1].append(d-1)
    fish_list.append([r-1,c-1,d-1])
s_r ,s_c = map(int,input().split())
shark = [s_r,s_c] # 상어 위치

fish_smell = [[0]*4 for _ in range(4)] # 물고기 냄새

def fish_move():
    new_graph = [[[] for _ in range(4)] for __ in range(4)]
    for fish in fish_list:
        cnt = 0
        x,y,d = fish[0],fish[1],fish[2]
        while True:
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < 4 and 0 <= ny < 4 and [nx,ny] != [s_r,s_c] and fish_smell[nx][ny] == 0:
                fish[0], fish[1], fish[2] = nx, ny, d
                new_graph[nx][ny].append(d)
                break
            else:
                d = (d - 1) % 8
                cnt += 1

            if cnt == 8:
                new_graph[x][y].append(d)
                break
    return new_graph

for _ in range(s):
    new_graph = fish_move()
