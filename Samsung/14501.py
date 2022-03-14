# 14501번 퇴사

''' # 잘못 푼 코드 (시작부터 불가능하면 넘어가는 코드가 구현 안되어있음)
def init():
    n = int(input())
    table = [list(map(int,input().split())) for _ in range(n)] # T_i, P_i
    return n,table

def search(table,new_t,new_p,cnt):
    global ans
    for i in range(new_t,n):
        print("i:",i)
        new_t = table[i][0] # T_i
        new_p = table[i][1] # P_i
        print("next t :",i + new_t)
        if i+new_t == n:
            new_cnt = cnt + new_p
            ans = max(ans,new_cnt)            
            return
        if i+new_t > n:
            print("------------over------------")            
            return
        else:
            new_cnt = cnt + new_p
            print("cnt: ",new_cnt)
            search(table,i+new_t,new_p,new_cnt)
        print("------------next------------")
        ans = max(ans,new_cnt)
        print("ans:", ans)

if __name__ == "__main__":
    n,table = init()
    ans = 0
    search(table,0,0,0)
    print(ans)
'''

n = int(input())
table = [list(map(int,input().split())) for _ in range(n)] # T_i, P_i
ans = 0

def search(date, cnt):
    global ans
    if date == n:  # n에 딱 맞게 도착
        ans = max(ans, cnt)
        return
    if date > n:  # n 초과 시 불가능
        return
    search(date + 1, cnt) # date 일때 일 안하기
    search(date + table[date][0], cnt + table[date][1]) # date 일때 일 하기

search(0, 0)
print(ans)