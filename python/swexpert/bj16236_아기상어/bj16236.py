import sys

sys.stdin = open('bj16236.txt', 'r')


N = int(input())
map = [list(map(int,input().split())) for i in range(N)]
babyShark = []
for i in range(N) :
    for j in range(N) :
        if map[i][j] == 9 :
            babyShark = [j,i,2,0]
            map[i][j] = 0
dx = [0,-1,1,0]
dy = [-1,0,0,1]
def isOk(x,y,size) :
    global N,map,visited
    if y < 0 or y >= N or x < 0 or x >= N or map[y][x] > size or visited[y][x] == 1:
        return 0
    if map[y][x] < size and map[y][x] > 0:
        return 1
    if map[y][x] == size or map[y][x] == 0 :
        return 2
def check(x,y,size) :
    # 먹을 수 있는 물고기 찾기
    Q = []
    time = 987654321
    re = []
    Q.append((x,y,0))
    while Q :
        tx,ty,tm = Q.pop(0)
        if tm > time :
            continue
        for i in range(4) :
            ok = isOk(tx+dx[i],ty+dy[i],size)
            if ok == 1 :
                time = tm + 1
                re.append((tx+dx[i],ty+dy[i],time))
            if ok == 2 :
                Q.append((tx+dx[i],ty+dy[i],tm+1))
                visited[ty+dy[i]][tx+dx[i]] = 1
    if re:
        rx,ry,rt = re[0]
        for x,y,t in re :
            if rt < t :
                continue
            if y < ry :
                ry = y
                rx = x
                continue
            if y == ry :
                if x < rx :
                    rx = x

        return (rx,ry,rt)
    else:
        return (0,0,0)

res = 0
while 1 :
    visited = [[0 for i in range(N)] for i in range(N)]
    visited[babyShark[1]][babyShark[0]] = 1
    x,y,c = check(babyShark[0],babyShark[1],babyShark[2])
    if c > 0 :
        res += c
        map[y][x] = 0
        babyShark[0] = x
        babyShark[1] = y
        babyShark[3] += 1
        if babyShark[3] == babyShark[2] :
            babyShark[3] = 0
            babyShark[2] += 1
    else :
        break
print(res)











