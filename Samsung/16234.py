# 인구 이동


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n,L,R = map(int,input().split())
people = [list(map(int,input().split())) for _ in range(n)]
visited = [[False] *n for _ in range(n)]
next = False

def print_array(list):
    for i in range(len(list)):
        print(list[i])

def bfs(x,y):
    global next
    unite = []
    unite.append([x,y])
    union = [[x,y]]
    total = people[x][y]
    visited[x][y] = True
    while unite:
        i ,j = unite.pop(0)
        person = people[i][j]
        for k in range(4):
            ni = i + dx[k]
            nj = j + dy[k]
            if ni < 0 or ni >= n or nj < 0  or nj >= n:
                continue
            if L <= abs(person - people[ni][nj]) <= R and visited[ni][nj] == False:
                total += people[ni][nj]
                visited[ni][nj] = True
                unite.append([ni,nj])
                union.append([ni,nj])
    if len(union) > 1:
        for land in union:
            people[land[0]][land[1]] = total // len(union)
        next = True

answer = 0
while True:
    next = False
    visited = [[False] *n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if visited[r][c] == False:
                bfs(r,c)
    if next:            
        answer += 1
    else:
        break

print(answer)