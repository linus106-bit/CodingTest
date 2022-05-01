# 어른 상어
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def deepcopy(graph):
    new_graph = [row[:] for row in graph]
    return new_graph

n, m, k = map(int,input().split()) # m: 상어 개수, k : 냄새 사라지는 시간
graph = [list(map(int,input().split())) for _ in range(n)]
directions = list(map(int, input().split()))


prior = []
for i in range(m):
    prior_row = []
    for k in range(4):
        prior_row.append(list(map(int,input().split())))
    prior.append(prior_row)

print(prior)

