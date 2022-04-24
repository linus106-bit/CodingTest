dx = [1,-1,0,0]
dy = [0,0,1,-1]

def deepcopy(graph):
    new_graph = [row[:] for row in graph]
    return new_graph
def print_array(list):
    print("--------------")
    for i in range(len(list)):
        print(list[i])
    print("--------------")
n = int(input())
shark = []
fish = []
board = []
visited = [[False]*n for _ in range(n)]
cnt = 0
answer = 0
for i in range(n):
    row = list(map(int,input().split()))
    board.append(row)
    for j in range(n):
        if row[j] == 9: 
            shark = [i,j]
            board[i][j] = 2
        elif row[j] > 0:
            fish.append([i,j,0])

def bfs(x,y):
    queue = []
    queue.append([x,y])
    new_board = deepcopy(board)
    new_map = [[0]*n for _ in range(n)]
    while queue:
        i,j = queue.pop(0)
        shark_size = new_board[i][j]
        visited[i][j] = True
        for k in range(4):
            ni = i + dx[k]
            nj = j + dy[k]
            if ni < 0 or ni >= n or nj < 0 or nj >= n:
                continue
            if shark_size >= new_board[ni][nj] and visited[ni][nj] == False :
                visited[ni][nj] = True
                new_board[ni][nj] = shark_size
                new_board[i][j] = 0
                new_map[ni][nj] = new_map[i][j] + 1
                queue.append([ni,nj])
    return new_map

while True:
    if len(fish) == 0:
        print(answer)
        break
    else:
        visited = [[False]*n for _ in range(n)]
        maps = bfs(shark[0],shark[1])
        next = False
        # print("map :")
        # print_array(maps)
        # print("board :")
        # print_array(board)
        for i in range(len(fish)):
            fish_x = fish[i][0]
            fish_y = fish[i][1]
            fish[i][2] = maps[fish_x][fish_y]
        # print("fish: ",fish)
        fish.sort(key=lambda x:(x[2],x[0],x[1]))
        for i in range(len(fish)):
            fish_x = fish[i][0]
            fish_y = fish[i][1]
            if fish[i][2] > 0 and board[shark[0]][shark[1]] > board[fish_x][fish_y]:
                cnt += 1
                # print("move : ", fish[i][2])
                answer += fish[i][2]
                if cnt % board[shark[0]][shark[1]] == 0:
                    board[shark[0]][shark[1]] += 1
                    cnt = 0
                # print("sharK_size : ", board[shark[0]][shark[1]])
                board[fish_x][fish_y] = board[shark[0]][shark[1]]
                board[shark[0]][shark[1]] = 0
                shark[0],shark[1] = fish_x, fish_y
                fish.pop(i)
                break
            if i == len(fish)-1 and fish[i][2] >= 0:
                next = True
                break
            if fish[i][2] == 0:
                continue
        if next:
            print(answer)
            break
        


