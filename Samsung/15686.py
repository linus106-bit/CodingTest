# import copy

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
house = []
chickens = []
ans = 10e7
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append([i,j])
        elif graph[i][j] == 2:
            chickens.append([i,j])
def deepcopy(graph):
    new_graph = [row[:] for row in graph]
    return new_graph


def solve(chicken_list):
    global ans
    count = 0
    for home in house:
        x = home[0]
        y = home[1]
        route = n*n+1
        for chicken in chicken_list:
            h_x = chicken[0]
            h_y = chicken[1]
            route = min(route,abs(x - h_x) + abs(y - h_y))
        count += route
    ans = min(ans, count)


def dfs(chicken_list,depth):
    if len(chicken_list) == m:
        solve(chicken_list)
        return
    elif depth == len(chickens):
        return
    new_list = deepcopy(chicken_list)

    new_list.append(chickens[depth])
    dfs(new_list,depth+1)

    new_list.pop(-1)
    dfs(new_list, depth + 1)

dfs([],0)
print(ans)