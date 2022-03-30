gear = [list(map(int,str(input()))) for _ in range(4)]
n = int(input())
rot = [list(map(int,input().split())) for _ in range(n)]
answer = 0

def rotate(l, n):
    return l[-n:] + l[:-n]

def rot_left(num,direction):
    if num < 0:
        return 
    if gear[num][2] != gear[num+1][6]:
        rot_left(num-1, -direction)
        gear[num] = rotate(gear[num],direction)

def rot_right(num,direction):
    if num > 3:
        return
    if gear[num][6] != gear[num-1][2]:
        rot_right(num+1, -direction)
        gear[num] = rotate(gear[num],direction)


for i in range(n):
    gear_num = rot[i][0]-1
    rot_left(gear_num-1,-rot[i][1])
    rot_right(gear_num+1,-rot[i][1])
    gear[gear_num] = rotate(gear[gear_num],rot[i][1])

for i in range(4):
    if gear[i][0] == 1:
        answer = answer + 2**i
print(answer)



