# r,c,m = map(int, input().split())
# shark_list = [list(map(int, input().split()))  for _ in range(m)] # [r,c,s,d,z]
# answer = 0


# dy = [0,0,1,-1]
# dx = [-1,1,0,0]
# def print_array(shark_list):
#     for i in range(len(shark_list)):
#         print(shark_list[i])

# def shark_init(shark_list):
#     shark_place = [[0 for col in range(c)] for row in range(r)]
#     for i in range(m):
#         x = shark_list[i][0]-1
#         y = shark_list[i][1]-1
#         if x < 0 or y < 0 :
#             pass
#         else:
#             if shark_place[x][y] != 0:
#                 if shark_place[x][y][1] < shark_list[i][4]:
#                     shark_list[shark_place[x][y][0]] = [0 for k in range(5)]
#                     shark_place[x][y] = [i,shark_list[i][4]]
#                 else:
#                     shark_list[i] = [0 for k in range(5)]
#             else:
#                 shark_place[x][y] = [i,shark_list[i][4]]
#     return shark_place

# def switch_dir(shark):
#     if shark[3] == 1:
#         shark[3] = 2
#     elif shark[3] == 2:
#         shark[3] = 1
#     elif shark[3] == 3:
#         shark[3] = 4
#     elif shark[3] == 4:
#         shark[3] = 3
#     return shark


# def shark_move(shark):
#     if shark[2] < 1:
#         return
#     new_x = shark[0] + dx[shark[3]-1]
#     new_y = shark[1] + dy[shark[3]-1]
#     if new_x < 1 or new_x > r:
#         shark = switch_dir(shark)
#     elif new_y < 1 or new_y > c:
#         shark = switch_dir(shark)
#     shark[0] += dx[shark[3]-1]
#     shark[1] += dy[shark[3]-1]
#     shark[2] -= 1
#     shark_move(shark)
#     shark[2] += 1

# def shark_catch(cnt, shark_list):
#     global answer
#     # print("cnt:",cnt)
#     row = r+1
#     catch = None
#     for i in range(m):
#         if shark_list[i][1] == cnt:
#             # print("ok:",i)
#             # print("row:", row,shark_list[i][0])
#             if row >= shark_list[i][0]:
#                 catch = i
#                 row = shark_list[i][0]
#     if catch is not None:
#         # print("eaten: ", catch,shark_list[catch][4])
#         answer += shark_list[catch][4]
#     # print("answer: ", answer)
#         shark_list[catch] = [0 for k in range(5)]


# if m == 0:
#     print(answer)
# else:
#     for k in range(c):
#         # print("K:",k)
#         shark_catch(k+1,shark_list)
#         for i in range(m):
#             shark_move(shark_list[i])
#         shark_now = shark_init(shark_list)
#         # print("shark_list:")
#         # print_array(shark_list)
#         # print("shark_now:")
#         # print_array(shark_now)    
#     print(answer)


r, c, m = map(int, input().split())                                                   
                                                                       
dx = [-1, 1, 0, 0]                                                                    
dy = [0, 0, 1, -1]                                                                    
                                                                                      
graph = [[[] for _ in range(c)] for _ in range(r)]                                    
                                                                                      
for _ in range(m):                                                                    
    x, y, s, d, z = map(int, input().split())                                         
    graph[x-1][y-1].append([z, s, d-1])                                               
                                                                                      
def moving():                                                                         
    g = [[[] for _ in range(c)] for _ in range(r)]                                    
    for i in range(r):                                                                
        for j in range(c):                                                            
            if graph[i][j]:                                                           
                x, y = i, j                                                           
                z, s, d = graph[i][j][0]                                              
                s_count = s                                                           
                while s_count > 0:                                                    
                    nx = x + dx[d]                                                    
                    ny = y + dy[d]                                                    
                    if 0 > nx or nx >= r or ny < 0 or ny >= c:                        
                        if d in [0, 2]:                                               
                            d += 1                                                    
                        elif d in [1, 3]:                                             
                            d -= 1                                                    
                        continue                                                      
                    else:                                                             
                        x, y = nx, ny                                                 
                        s_count -= 1                                                  
                g[x][y].append([z, s, d])                                             
    for i in range(r):                                                                
        for j in range(c):                                                            
            graph[i][j] = g[i][j]                                                     
                                                                                      
eat_count = 0                                                                         
                                                                                      
for i in range(c):                                                                    
    for j in range(r):                                                                
        if graph[j][i]:                                                               
            value = graph[j][i][0]                                                    
            eat_count += value[0]                                                     
            graph[j][i].remove(value)                                                 
            break                                                                     
                                                                                      
    moving()                                                                          
                                                                                      
    for p in range(r):                                                                
        for q in range(c):                                                            
            if len(graph[p][q]) >= 2:                                                 
                graph[p][q].sort(reverse=True)                                        
                while len(graph[p][q]) >= 2:                                          
                    graph[p][q].pop()                                                 
                                                                                      
                                                                                      
print(eat_count)
