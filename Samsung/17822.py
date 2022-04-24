n, m, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
moves = [list(map(int, input().split())) for _ in range(t)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
next = False
answer = 0
visited = [[False]*m for _ in range(n)]

def rotate(move):
    for i in range(n):
        if ((i+1) % move[0]) == 0: #의 배수
            for j in range(move[2]): # 회전수 T
                if move[1] == 0: # 시계 방향
                    tmp = graph[i].pop(m-1)
                    graph[i].insert(0, tmp)
                elif move[1] == 1:
                    tmp = graph[i].pop(0)
                    graph[i].append(tmp)
        else:
            continue
    return graph

def find_same(x,y): # bfs
    queue = []
    cnt = 0
    queue.append([x,y])
    num = graph[x][y]
    while queue:
        i,j = queue.pop(0)

        visited[i][j] = True
        for k in range(4):
            ni = i + dx[k]
            nj = j + dy[k]
            if nj < 0:
                nj = m-1
            elif nj > m-1:
                nj = 0
            if ni < 0 or ni >= n or nj < 0 or nj >= m :
                continue
            if graph[ni][nj] == num and visited[ni][nj] == False and num != 0:
                cnt += 1
                num = graph[ni][nj]
                graph[ni][nj] = 0
                graph[i][j] = 0
                queue.append([ni,nj])

    return cnt

for move in moves:
    visited = [[False]*m for _ in range(n)]
    # print("move:", move)
    graph = rotate(move)
    stop = 0
    # print(graph)
    while True:
        for x in range(n):
            for y in range(m):
                cnt = find_same(x,y)
                stop = max(cnt,stop)
        if stop == 0:
            total = 0
            all = n*m
            for i in range(n):
                total += sum(graph[i])
                all -= graph[i].count(0)
            try:
                threshold = float(total /all)
            except ZeroDivisionError:
                threshold = 0
            # print(threshold)
            for x in range(n):
                for y in range(m):
                    if graph[x][y] > 0 and graph[x][y] > threshold:
                        graph[x][y] -= 1
                    elif graph[x][y] > 0 and graph[x][y] < threshold:
                        graph[x][y] += 1
            # print(graph)
            break
        else:
            # print(graph)
            break
for i in range(n):
    answer += sum(graph[i])

print(answer)
