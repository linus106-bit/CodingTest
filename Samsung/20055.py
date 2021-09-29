def init():
    belt = list(map(int, input().split()))
    A = list(map(int, input().split()))
    return belt, A

def put_robot(belt, A, robot):
    if A[0] > 0:
        A[0] += -1
        robot[0] = 1
    return robot, A 

def move_robot(belt, A, robot):
    A.insert(0,A[-1])
    A.pop(-1)
    robot.insert(0,robot[-1])
    robot.pop(-1)
    robot[belt[0]-1] = 0
    for i in range(belt[0]-1):
        idx = belt[0]-2-i
        if robot[idx] == 1:
            if robot[idx+1] == 0 and A[idx+1] > 0:
                robot[idx+1], robot[idx] = robot[idx], robot[idx+1]
                A[idx+1] += -1
                robot[belt[0]-1] = 0
    return robot, A


if __name__ == "__main__":
    belt , A = init()
    robot = [0 for i in range(belt[0])]
    answer = 0
    while A.count(0) < belt[1]:
        robot, A = move_robot(belt, A, robot)
        robot, A = put_robot(belt, A, robot)
        answer += 1
    print(answer)