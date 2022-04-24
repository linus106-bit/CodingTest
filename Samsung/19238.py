# 스타트 택시
# board에서 못가는 길을 넣어주기 위해서 음수 값(-1,-2)를 넣어서 예외 케이스 넣어주기


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def print_array(list):
    for i in range(len(list)):
        print(list[i])

def deepcopy(graph):
    new_graph = [row[:] for row in graph]
    return new_graph

n,m,gas = map(int,input().split())
board = []
for i in range(n):
    data = list(map(int, input().split()))
    array = []
    for d in data:
        if d == 1:
            array.append(-1)
        else:
            array.append(-2)

    board.append(array)

start_r,start_c = map(int, input().split())

customer = [list(map(int,input().split())) for _ in range(m)]

def bfs(board,x,y):
    # print("start", x, y)
    queue = []
    queue.append([x,y])
    new_board = deepcopy(board)
    visited = [[False] *n for _ in range(n)]
    new_board[x][y] = 0
    visited[x][y] = True
    while queue:
        x,y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if new_board[nx][ny] == -1 or visited[nx][ny] == True:
                continue
            new_board[nx][ny] = new_board[x][y] + 1
            visited[nx][ny] = True
            queue.append([nx,ny])
    return new_board

while True:
    # print("start: ",start_r,start_c)
    new_board = bfs(board,start_r-1,start_c-1)
    if gas < 0:
        break
    if len(customer) == 0:
        break
    move = []
    for i in range(len(customer)):
        r = customer[i][0]-1
        c = customer[i][1]-1
        end_r = customer[i][2]-1
        end_c = customer[i][3]-1
        dis = new_board[r][c]
        if dis < 0:
            continue
        move.append([dis,r,c,end_r,end_c])
    if len(move) == 0:
        gas = -1
        break
    else:
        move.sort(key=lambda x:(x[0],x[1],x[2]))
        # print("move: ",move)
        if move[0][0] > gas:
            gas = -1
            break
        else:
            gas -= move[0][0]
            r,c,end_r,end_c = move[0][1:]
            end = bfs(board,r,c)
            d = end[end_r][end_c]
            if d < 0:
                gas = -1
                break
            gas -= d
            if gas >=0:
                # print("end gas:",gas, "d: ",d)
                gas += d*2
                customer.remove([r+1,c+1,end_r+1,end_c+1])
                start_r,start_c = end_r +1, end_c +1
                # print(gas)
            else:
                gas = -1
                break
print(gas)





