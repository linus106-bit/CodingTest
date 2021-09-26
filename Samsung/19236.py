import copy


def init():
    grid = [list(map(int, input().split())) for _ in range(4)]
    score = grid[0][0]
    grid[0][0] = 17 # Shark
    return grid, score


def find_fish(grid,n):
    for i in range(len(grid)):
        for j in range(int((len(grid[i])/2))):
            fish = grid[i][2*j]
            if fish == n:
                return i,j,grid[i][2*j+1]
    return 0,0,0

def move_fish(grid,i,j,fish_movement):
    while True:
        if fish_movement == 0 :
            break
        new_i = i + di[fish_movement-1]
        new_j = j + dj[fish_movement-1]
        if new_i < 0 or new_j < 0 or new_i > 3 or new_j > 3 or grid[new_i][2*new_j] == 17: 
            fish_movement += 1
            if fish_movement == 9:
                fish_movement = 1
            grid[i][2*j+1] = fish_movement
        else:
            grid[i][2*j],grid[new_i][2*new_j] = grid[new_i][2*new_j],grid[i][2*j]
            grid[i][2*j+1],grid[new_i][2*new_j+1] = grid[new_i][2*new_j+1],grid[i][2*j+1]
            break

def grid_update(grid,score,eaten_fish):
    global answer
    score += eaten_fish
    answer = max(answer,score)

    for k in range(1,17):
        fish_idx_i, fish_idx_j, fish_movement = find_fish(grid,k)
        move_fish(grid,fish_idx_i,fish_idx_j,fish_movement)
    for step in range(1,4):

        shark_idx_i, shark_idx_j, shark_movement = find_fish(grid,17)
        eat_i = shark_idx_i + di[shark_movement-1]*step
        eat_j = shark_idx_j + dj[shark_movement-1]*step
        if 0 <= eat_i < 4 and 0 <= eat_j < 4 and grid[eat_i][2*eat_j] > 0:
            new_grid = copy.deepcopy(grid)
            eaten_fish = new_grid[eat_i][2*eat_j]
            new_grid[eat_i][2*eat_j] = 17
            new_grid[shark_idx_i][2*shark_idx_j] = 0
            new_grid[shark_idx_i][2*shark_idx_j+1] = 0

            grid_update(new_grid,score,eaten_fish)
        else:
            pass
        

if __name__ == "__main__":
    di = [-1,-1,0,1,1,1,0,-1]
    dj = [0,-1,-1,-1,0,1,1,1]
    answer = 0

    init_grid,score = init()
    grid_update(init_grid,score,eaten_fish=0)

    print(answer)
