n,m = map(int,input().split())
tray = [list(map(int, str(input()))) for _ in range(n)]
answer = 0 

def dfs(tray,i,j):
    if i < 0 or i >= n  or j < 0 or j >= m:
        return False
    if tray[i][j] == 0:
        tray[i][j] = 1
        dfs(tray,i-1,j)
        dfs(tray,i,j-1)
        dfs(tray,i+1,j)
        dfs(tray,i,j+1)
        return True
    return False

for i in range(n):
    for j in range(m):
        if dfs(tray,i,j) == True:
            answer += 1
print(answer)
