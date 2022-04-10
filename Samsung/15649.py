import copy


n,m = map(int, input().split())

answer = []
def dfs(i,answer):
    if i == m:
        print(' '.join(map(str,answer)))
        return
    for k in range(n):
        if k not in answer: 
            new_answer = copy.deepcopy(answer)
            new_answer.append(k+1)
            dfs(i+1,new_answer)
dfs(0,answer)
