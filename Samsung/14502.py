import copy


di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]



def init():
    n,m = map(int,input().split())
    lab = [list(map(int,input().split())) for _ in range(n)]
    return n,m,lab

def find_virus(lab):
    virus_list = []
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 2:
                virus_list.append([i,j])
    return virus_list

def count_lab(lab):
    cnt = 0
    for i in range(len(lab)): 
        cnt += lab[i].count(0)
    return cnt

def place_wall(lab,virus_list,step):
    global ans
    new_lab = copy.deepcopy(lab)
    if step == 3:
        for num in range(len(virus_list)):
            i , j = virus_list[num]
            move_virus(i,j,new_lab)
        cnt = count_lab(new_lab)
        ans = max(ans,cnt)
        return
    for i in range(n):
        for j in range(m):
            if new_lab[i][j] == 0:
                new_lab[i][j] = 1
                place_wall(new_lab,virus_list,step+1)
                new_lab = copy.deepcopy(lab)

def move_virus(i,j,lab):
    for k in range(4):
        new_i = i +di[k]
        new_j = j +dj[k]
        if new_i >= 0 and new_j>=0 and new_i < n and new_j < m :
            if lab[new_i][new_j] == 0:
                lab[new_i][new_j] = 2
                move_virus(new_i,new_j,lab)





n,m,lab = init()
ans = 0
virus_list = find_virus(lab)
place_wall(lab,virus_list,step=0)
print(ans)



