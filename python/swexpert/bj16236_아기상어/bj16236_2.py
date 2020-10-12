import sys

sys.stdin = open('bj16236.txt','r')

N = int(input())

originMap = []
shark = [-1,-1,2,0]
# x, y , size, eat
# fishes = []
for i in range(N) :
    originMap.append(list(map(int,input().split())))

for i in range(N) :
    for j in range(N) :
        if originMap[i][j] == 9 :
            shark[0] = j
            shark[1] = i
            originMap[i][j] = 0


time = 0
visited = [[0 for _ in range(N)] for __ in range(N)]
godir = [(0,-1),(-1,0),(1,0),(0,1)]

def isSafe(x,y,size) :
    global visited, originMap
    return 0 <= x < N and 0 <= y < N and visited[y][x] == 0 and originMap[y][x] <= size

def check(x,y,size) :
    visited[y][x] = 1
    q = [(x,y,0)]
    time = N*N
    hunted = []
    while q :
        x,y,t = q.pop(0)
        if t > time :
            continue
        for i in range(4) :
            dx,dy = godir[i]
            if isSafe(x+dx,y+dy,size) :
                if originMap[y+dy][x+dx] == size or originMap[y+dy][x+dx] == 0 :
                    q.append((x+dx,y+dy,t+1))
                    visited[y+dy][x+dx] = 1
                    continue
                if 0 < originMap[y+dy][x+dx] < size :
                    time = t+1
                    hunted.append((x+dx,y+dy,time))
    if hunted :
        x,y,t = hunted[0]
        for hx,hy,ht in hunted :
            if ht <= t :
                t = ht
                if hy < y :
                    y = hy
                    x = hx
                    continue
                if hy == y :
                    x = min(x,hx)
        return (x,y,t)
    else :
        return (0,0,0)

res = 0
while True :
    visited = [[0 for _ in range(N)] for __ in range(N)]
    x,y,t = check(shark[0],shark[1],shark[2])
    if t == 0 :
        break
    else :
        originMap[y][x] = 0
        shark[0] = x
        shark[1] = y
        shark[3] += 1
        if shark[2] == shark[3] :
            shark[2] += 1
            shark[3] = 0
        res += t
print(res)