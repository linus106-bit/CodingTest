import copy

def print_list(list):
    for i in range(len(list)):
        print(list[i])


'''
n,m = map(int, input().split())
maze = [list(map(int,str(input()))) for _ in range(n)]
answer = n*m
def dfs(i,j,step):
    global answer
    step += 1
    if i == n-1 and j == m-1 :
        answer = min(answer,step)
        print(maze)
        return
    if i < 0 or i > n-1 or j < 0 or j > m-1:
        return
    if maze[i][j] == 1:
        maze[i][j] = 2
        dfs(i-1,j,step)
        dfs(i,j-1,step)
        dfs(i+1,j,step)
        dfs(i,j+1,step)

dfs(0,0,0)
print(answer)
'''
n,m = map(int, input().split())
maze = [list(map(int,str(input()))) for _ in range(n)]
answer = n*m
def dfs(maze,i,j,step):
    global answer
    step += 1
    if i == n-1 and j == m-1 :
        answer = min(answer,step)
        return
    if i < 0 or i > n-1 or j < 0 or j > m-1:
        return
    if maze[i][j] == 1:
        new_maze = copy.deepcopy(maze)
        new_maze[i][j] = 2
        dfs(new_maze,i-1,j,step)
        dfs(new_maze,i,j-1,step)
        dfs(new_maze,i+1,j,step)
        dfs(new_maze,i,j+1,step)

dfs(maze,0,0,0)
print(answer)