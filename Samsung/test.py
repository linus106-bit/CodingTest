M = 3
some_list = [[1,2], [2,3], [3,4], [4,5]]

visited = [False] * len(some_list)


def dfs(perm):
    if len(perm) == M:  # 종료 조건 : M개를 모두 선택했을 때
        print(perm)
        return

    for i, val in enumerate(some_list):
        if visited[i]:  # 방문한 노드인 경우 제외
            continue
        # i번째 노드를 포함하여 재귀 호출
        perm.append(val)
        visited[i] = True
        dfs(perm)
        # i번째 노드 삭제
        perm.pop(-1)
        visited[i] = False

dfs([])
print("-----------comb------------")
def dfs(comb,depth):
    if len(comb) == M:
        print(comb)
        # solve(comb)
        return
    elif depth == len(some_list):
        return
    # new_list = deepcopy(comb)

    comb.append(some_list[depth])
    dfs(comb,depth+1)

    comb.pop(-1)
    dfs(comb, depth + 1)

dfs([],0)