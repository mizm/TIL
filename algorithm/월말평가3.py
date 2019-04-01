def dfs(present_distance,present_robot):
    global distancesum
    if sum(visit)==len(visit):
        # print(present_distance)
        if distancesum>present_distance:
            distancesum=present_distance
        return
    if present_distance>=distancesum:
        return

    for i in range(len(visit)):
        if visit[i]==0:
            visit[i]=1
            plus_distance=abs(robot_data[2*present_robot]-snack_data[2*i])+abs(robot_data[2*present_robot+1]-snack_data[2*i+1])
            # print(present_distance+plus_distance,present_robot+1)
            dfs(present_distance+plus_distance,present_robot+1)
            visit[i]=0




T=int(input())
for t in range(T):
    N=int(input())
    snack_data=list(map(int,input().split()))
    robot_data=list(map(int,input().split()))
    visit=[0]*N
    distancesum=987654321
    dfs(0,0)
    print("#{} {}".format(t+1,distancesum))
# 3
# 3
# 2 2 2 5 5 0
# 3 3 4 2 1 0
# 4
# 1 1 3 5 3 9 4 1
# 9 1 11 0 0 4 7 8
# 4
# 1 1 3 3 5 5 7 7
# 2 2 4 4 6 6 8 8
# 1
# 3
# 2 2 2 5 5 0
# 3 3 4 2 1 0