def dfs(x,y) :
    global temp
    if temp < Data[y][x] :
        temp = Data[y][x]
    Data[y][x] = -1
    for i in range(4) :
        nx = x +dx[i]
        ny = y +dy[i]
        if issafe(nx,ny) :
            dfs(nx,ny)

def issafe(x,y) :
    return x >= 0 and x < n and y >= 0 and y < n and Data[y][x] > 0

dx = [0,0,1,-1]
dy = [1,-1,0,0]
for tc in range(int(input())):
    n = int(input())
    Data = []
    cnt = 0
    temp = 0
    for i in range(n) :
        Data.append(list(map(int,input().split())))
    for i in range(n) :
        for j in range(n) :
            if Data[i][j] > 0 :
                cnt += 1
                dfs(j,i)
    print('#%d %d %d'%((tc+1),cnt,temp))