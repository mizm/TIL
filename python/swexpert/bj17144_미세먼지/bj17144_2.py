import sys
sys.stdin = open('bj17144.txt','r')

R, C, T = map(int,input().split())

originMap = []

for i in range(R) :
    originMap.append(list(map(int,input().split())))

startPoint = []

upDir = [(1,0),(0,-1),(-1,0),(0,1)]
downDir = [(1,0),(0,1),(-1,0),(0,-1)]
for i in range(R) :
    if originMap[i][0] == -1 :
        startPoint.append((0,i))

def isSafe(x,y) :
    return 0 <= x < C and 0 <= y < R

def diffusion() :
    global originMap
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    tmpmap = [[0 for i in range(C)] for i in range(R)]
    for i in range(R):
        for j in range(C):
            if originMap[i][j] > 0:
                cnt = 0
                point = int(originMap[i][j] / 5)
                for k in range(4):
                    tx = j + dx[k]
                    ty = i + dy[k]
                    if 0 <= tx < C and 0 <= ty < R and originMap[ty][tx] >= 0:
                        cnt += 1
                        tmpmap[ty][tx] += point
                originMap[i][j] -= point * cnt
    for i in range(R):
        for j in range(C):
            if tmpmap[i][j] > 0:
                originMap[i][j] += tmpmap[i][j]

def wind() :
    global originMap
    # up
    uplist = [0]
    sx,sy = startPoint[0]
    sd = 0
    while 1:
        dx, dy = upDir[sd]
        if not isSafe(sx + dx, sy + dy):
            sd += 1
        dx, dy = upDir[sd]
        if originMap[sy][sx] >= 0:
            uplist.append(originMap[sy][sx])
            originMap[sy][sx] = uplist[len(uplist) - 2]
        sy += dy
        sx += dx
        if (sx, sy) == startPoint[0]:
            break
    sx, sy = startPoint[1]
    downlist = [0]
    sd = 0
    while 1 :
        dx, dy = downDir[sd]
        if not isSafe(sx+dx, sy+dy) :
            if sd == 3 :
                break
            sd += 1
        dx, dy = downDir[sd]
        if originMap[sy][sx] >= 0:
            downlist.append(originMap[sy][sx])
            originMap[sy][sx] = downlist[len(downlist) - 2]
        sy += dy
        sx += dx
        if (sx,sy) == startPoint[1] :
            break
for i in range(T) :
    diffusion()
    wind()
res = 0
for i in range(R) :
    res += sum(originMap[i])
print(res+2)