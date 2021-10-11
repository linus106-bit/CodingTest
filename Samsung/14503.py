dr = [-1,0,1,0] # d = 0,1,2,3
dc = [0,1,0,-1]


def init():
    n,m = map(int, input().split())
    r,c,d = map(int, input().split())
    room =  [list(map(int, input().split())) for _ in range(n)]
    return n,m,r,c,d,room

def search_room(r,c,d):
    global ans
    if room[r][c] == 0:
        room[r][c] = 2
        ans += 1
    for step in range(4):
        left_d = (d + 3) % 4
        new_r = r + dr[left_d]
        new_c = c + dc[left_d]
        if room[new_r][new_c] == 0:
            search_room(new_r,new_c,left_d)
            return
        d = left_d
    back_d = (d + 2) % 4
    new_r = r + dr[back_d]
    new_c = c + dc[back_d]
    if room[new_r][new_c] == 1:
        return
    search_room(new_r,new_c,d)
    return

n,m,r,c,d,room = init()
ans = 0
search_room(r,c,d)

print(ans)
