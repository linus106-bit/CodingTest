n, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0





for i in range(n):
    y = 0
    next = True
    visited = [False]*n
    while next:
        if y >= n-1:
            answer += 1   
            break
        if board[i][y] - board[i][y+1] == 1: # 경사로가 밑으로 차이난다면
            for k in range(L-1):
                try:
                    if board[i][y+1+k] != board[i][y+2+k]: # 계속 평평한지 확인
                        next = False
                except IndexError:
                    next = False
            if next:
                for k in range(L):
                    y += 1
                    visited[y] = True

        elif board[i][y] - board[i][y+1] == -1: # 경사로가 위로 차이난다면
            if visited[y-L+1] == True:
                break
            for k in range(L-1):
                try:
                    if board[i][y-k] != board[i][y-k-1] or y-k-1 < 0 : # 계속 평평한지 확인
                        next = False
                except IndexError:
                    next = False
            y += 1
        elif abs(board[i][y] - board[i][y+1]) == 0:
            y += 1
        else:
            break






for j in range(n):
    x = 0
    next = True
    visited = [False]*n
    while next:
        if x >= n-1:
            answer += 1
            break
        if board[x][j] - board[x+1][j] == 1: # 경사로가 밑으로 차이난다면
            for k in range(L-1):
                try:
                    if board[x+1+k][j] != board[x+2+k][j]: # 계속 평평한지 확인
                        next = False
                except IndexError:
                    next = False
            if next:
                for k in range(L):
                    x += 1
                    visited[x] = True
        elif board[x][j] - board[x+1][j] == -1: # 경사로가 위로 차이난다면
            if visited[x-L+1] == True:
                break
            for k in range(L-1):
                try:
                    if board[x-k][j] != board[x-k-1][j] or x-k-1 < 0: # 계속 평평한지 확인
                        next = False
                except IndexError:
                    next = False
            x += 1
        elif abs(board[x][j] - board[x+1][j]) == 0:
            x += 1
        else:
            break

print(answer)