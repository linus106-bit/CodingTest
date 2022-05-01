dx = [0,0,-1,1]
dy = [-1,1,0,0]


n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

viruses = []
wall_num = 0
room_num = 0
answer = 1e10
cnt = 0

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            wall_num += 1
        elif graph[i][j] == 2:
            viruses.append([i,j])
        elif graph[i][j] == 0:
            room_num += 1


def bfs(starts):
    q = []
    for s in starts:
        q.append((s[0], s[1], 0))

    # temp = [row[:] for row in graph]
    visited = [[0] * n for _ in range(n)]
    while q:
        i, j, t = q.pop(0)
        if visited[i][j]:
            continue
        visited[i][j] = t
        # temp[i][j] = 2
        for d in range(4):
            new_i = i + dx[d]
            new_j = j + dy[d]
            if 0 <= new_i < n and 0 <= new_j < n and graph[new_i][new_j] != 1:
                q.append((new_i, new_j, t + 1))

    result = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0: # 빈공간에서 t를 보기
                if visited[i][j] == 0: # 다 안간거니까 다 못퍼트린걸로 간주
                    return 1e10
                result = max(result, visited[i][j])
    return result


def dfs(virus_list,depth): # M개의 조합 찾기 Combination
    global cnt,answer
    if len(virus_list) == m:
        answer = min(answer, bfs(virus_list))
        return
    elif depth == len(viruses):
        return
    new_list = [row[:] for row in virus_list]

    new_list.append(viruses[depth])
    dfs(new_list,depth+1)

    new_list.pop(-1)
    dfs(new_list, depth + 1)

dfs([],0)
if answer == 1e10:
    print(-1)
else:
    print(answer)