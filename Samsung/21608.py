# 상어 초등학교

dx = [-1,1,0,0]
dy = [0,0,1,-1]


n = int(input())
students = [list(map(int,input().split())) for _ in range(n*n)]
classroom = [[0]*n for _ in range(n)]

# 가능한 자리를 다 담아서 정렬
for student in students:
    tmp = []
    for i in range(n):
        for j in range(n):
            if classroom[i][j] == 0:
                like = 0
                blank = 0
                for k in range(4):
                    nx , ny = i + dx[k], j + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if classroom[nx][ny] in student[1:]:
                            like += 1
                        if classroom[nx][ny] == 0:
                            blank += 1
                tmp.append([like,blank,i,j])
    tmp.sort(key=lambda x:(-x[0],-x[1],x[2],x[3]))
    classroom[tmp[0][2]][tmp[0][3]] = student[0]

students.sort()
answer = 0
for i in range(n):
    for j in range(n):
        ans = 0
        for k in range(4):
            nx, ny = i + dx[k], j + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if classroom[nx][ny] in students[classroom[i][j]-1]:
                    ans += 1
        if ans != 0:
            answer += 10 ** (ans-1)
print(answer)