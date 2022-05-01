dx = [0,0,-1,1]
dy = [1,-1,0,0]

n,k = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)] # 0 빈칸 1 빨간색 2 파란색
horse_map = [[[] * n for _ in range(n)] for __ in range(n)]
horse_list = []
for i in range(k):
    r,c,d = map(int,input().split()) # 0 r 1 c 2 d 3 num-1
    horse_list.append([r-1,c-1,d-1])
    horse_map[r-1][c-1].append(i)
time = 0
next = True
while next:
    if time > 1000:
        time = -1
        break
    for i in range(k):
        x,y,d = horse_list[i]
        nx = x + dx[d]
        ny = y + dy[d]
        if not (0 <= nx < n and 0 <= ny < n) or graph[nx][ny] == 2:
            d ^= 1
            nx = x + dx[d]
            ny = y + dy[d]
            if not (0 <= nx < n and 0 <= ny < n) or graph[nx][ny] == 2:
                nx = x
                ny = y
        horse_list[i] = [nx,ny,d]
        if nx == x and ny == y:
            continue
        idx = horse_map[x][y].index(i)
        for tmp in horse_map[x][y][idx+1:]:
            horse_list[tmp][0], horse_list[tmp][1] = nx,ny
        if graph[nx][ny] == 0:
            horse_map[nx][ny].extend(horse_map[x][y][idx:])
        elif graph[nx][ny] == 1:
            reverse_list = horse_map[x][y][idx:]
            reverse_list.reverse()
            horse_map[nx][ny].extend(reverse_list)
        horse_map[x][y] = horse_map[x][y][:idx]
        if len(horse_map[nx][ny]) > 3:
            next = False
            break

    time += 1

print(time)
