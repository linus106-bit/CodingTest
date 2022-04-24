# N과M 1번 => 중복되지 않게 숫자 조합 찾기
n,m = map(int, input().split())

answer = []
def dfs(i,answer):
    if i == m:
        print(' '.join(map(str,answer)))
        return
    for k in range(n):
        if k+1 not in answer: 
            new_answer = answer[:]
            new_answer.append(k+1)
            dfs(i+1,new_answer)
dfs(0,answer)
