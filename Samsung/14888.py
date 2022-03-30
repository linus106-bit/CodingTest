# 연산자 끼워넣기


minimum = 1e9
maximum = -1e9
n = int(input())
num = list(map(int,input().split()))
cal = list(map(int,input().split()))

def solve(depth,total,plus,minus,mul,div):
    global minimum,maximum
    if depth == n:
        minimum = min(total, minimum)
        maximum = max(total, maximum)
        return
    
    if plus:
        solve(depth + 1, total + num[depth], plus - 1, minus, mul, div)
    if minus:
        solve(depth + 1, total - num[depth], plus, minus - 1, mul, div)
    if mul:
        solve(depth + 1, total * num[depth], plus, minus, mul - 1, div)
    if div:
        solve(depth + 1, int(total / num[depth]), plus, minus, mul, div - 1)


solve(1,num[0],cal[0],cal[1],cal[2],cal[3])
print(maximum)
print(minimum)


