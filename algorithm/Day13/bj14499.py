def dice(dir) :
    if dir == 3: #북
        temp =[mdice[1][1],mdice[2][1],mdice[3][1],mdice[0][1]]
        for i in range(4) :
            mdice[i][1] = temp[i]
    if dir == 4: #남
        temp = [mdice[3][1],mdice[0][1],mdice[1][1],mdice[2][1]]
        for i in range(4) :
            mdice[i][1] = temp[i]
    if dir == 1: #동
        temp = [mdice[1][1],mdice[1][2],mdice[3][1],mdice[1][0]]
        for i in range(3) :
            mdice[1][i] = temp[i]
        mdice[3][1] = temp[3]
    if dir == 2:#서
        temp = [mdice[3][1], mdice[1][0],mdice[1][1], mdice[1][2]]
        for i in range(3) :
            mdice[1][i] = temp[i]
        mdice[3][1] = temp[3]
# def dice(dir) :
#     temp = mdice[:]
#     if dir == 1 :
#         mdice[1] = temp[4]
#         mdice[3] = temp[1]
#         mdice[4] = temp[6]
#         mdice[6] = temp[3]
#     elif dir == 2 :
#         mdice[1] = temp[3]
#         mdice[3] = temp[6]
#         mdice[4] = temp[1]
#         mdice[6] = temp[4]
#     elif dir == 3 :
#         mdice[1] = temp[5]
#         mdice[2] = temp[1]
#         mdice[5] = temp[6]
#         mdice[6] = temp[2]
#     elif dir == 4 :
#         mdice[1] = temp[2]
#         mdice[2] = temp[6]
#         mdice[5] = temp[1]
#         mdice[6] = temp[5]

def issafe(x,y) :
    return x >= 0 and x < m and y >= 0 and y < n
n,m,y,x,k = map(int,input().split())
# mdice = [0,0,0,0,0,0,0]
mdice = [[-1,0,-1],[0,0,0],[-1,0,-1],[-1,0,-1]]
# mdice = [[-1,1,-1],[2,3,4],[-1,5,-1],[-1,6,-1]]
dx = [0,1,-1,0,0]
dy = [0,0,0,-1,1]
#첫번째가 밑면
my_map = []
for i in range(n) :
    my_map.append(list(map(int,input().split())))
Data = list(map(int,input().split()))
for i in Data :
    if issafe(x+dx[i],y+dy[i]) :
        x+=dx[i]
        y+=dy[i]
        dice(i)
        print(mdice[1][1])
        if my_map[y][x] > 0 :
            mdice[3][1] = my_map[y][x]
            my_map[y][x] = 0
        else :
            my_map[y][x] = mdice[3][1]
        # print(mdice)

#
# dice(2)
# print(mdice)
# # dice(4)
# print(mdice)