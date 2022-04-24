# 마법사 상어와 비바라기
dr = [0,-1,-1,-1,0,1,1,1]
dc = [-1,-1,0,1,1,1,0,-1]
goal = 0
n ,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
moves = [list(map(int,input().split())) for _ in range(m)]
visited = [[False] * n for _ in range(n)]
cloud_init = [[n-2,0],[n-2,1],[n-1,0],[n-1,1]]

def print_array(shark_list):
    for i in range(len(shark_list)):
        print(shark_list[i])


def make_cloud(cloud_list, move,i):
    next_cloud = []
    visited = [[False] * n for _ in range(n)]
    for cloud in cloud_list:
        x = cloud[0]
        y = cloud[1]
        d = move[i][0]
        s = move[i][1]
        new_r , new_c = cloud_move(x,y,d,s)

        visited[new_r][new_c] = True
        board[new_r][new_c] += 1
        next_cloud.append([new_r,new_c])
    return next_cloud

def rain(next_cloud):
    for cloud in next_cloud:
        cnt = 0 
        for tmp in range(4):
            nr = cloud[0] + dr[2*tmp + 1]
            nc = cloud[1] + dc[2*tmp + 1]
            if 0 <= nr < n and 0<= nc < n and board[nr][nc] >= 1:
                cnt += 1
        board[cloud[0]][cloud[1]] += cnt


def new_cloud(cloud_list):
    for r in range(n):
        for c in range(n):
            if board[r][c] >= 2 and visited[r][c] == False:
                board[r][c] -= 2
                cloud_list.append([r,c])
    return cloud_list


def cloud_move(r,c,d,s):
    new_r = r + dr[d-1]*s
    new_c = c + dc[d-1]*s
    if new_r >= n:
        new_r = new_r % n
    if new_r < 0:
        new_r = n - 1 -(((-1)*new_r -1) % n)
    if new_c >= n:
        new_c = new_c % n
    if new_c < 0:
        new_c = n - 1 -(((-1)*new_c -1) % n)
    return new_r,new_c

def answer():
    global goal
    for r in range(n):
        for k in range(n):
            goal += board[r][k]
    print(goal)


for i in range(m):
    print("i:",i)
    print_array(board)
    next_cloud = make_cloud(cloud_init, moves, i)
    print("--------------")
    print_array(board)
    cloud_init = []
    rain(next_cloud)
    print("--------------")
    print_array(board)    
    cloud_init = new_cloud(cloud_init)

answer()

############## 해설 ##############
'''

n, m = map(int, input().split())


arr = [list(map(int, input().split())) for _ in range(n)]
moves = []
for i in range(m):
    tmp = list(map(int, input().split()))
    moves.append([tmp[0] - 1, tmp[1]])

clouds = [[n-2, 0], [n-2, 1], [n-1, 0], [n-1, 1]]

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
for i in range(m):
    # step 1.
    # 이동
    move = moves[i]
    next_clouds = []
    for cloud in clouds:
        x = cloud[0]
        y = cloud[1]
        d = move[0]
        s = move[1]
        nx = (n + x + dx[d] * s) % n
        ny = (n + y + dy[d] * s) % n
        next_clouds.append([nx, ny])

    # step 2.
    visited = [[False]* n for _ in range(n)]
    for cloud in next_clouds:
        x = cloud[0]
        y = cloud[1]
        arr[x][y] += 1
        visited[x][y] = True
    
    # step 3
    clouds = []

    # step 4
    cx = [-1, -1, 1, 1]
    cy = [-1, 1, -1, 1]
    for cloud in next_clouds:
        x = cloud[0]
        y = cloud[1]
        count = 0
        for i in range(4):
            nx = x + cx[i]
            ny = y + cy[i]

            if 0 <= nx < n and 0<= ny < n and arr[nx][ny] >= 1:
                count += 1

        arr[x][y] += count
        
    # step 5

    for i in range(n):
        for j in range(n):
            if arr[i][j] >= 2 and visited[i][j] == False:
                arr[i][j] -= 2
                clouds.append([i, j])

ans = 0
for i in range(n):
    ans += sum(arr[i])


print(ans)
'''