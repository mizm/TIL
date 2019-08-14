import sys

sys.stdin = open('bj17144.txt', 'r')

R,C,T = list(map(int,input().split()))
map = [list(map(int,input().split())) for i in range(R)]
dx = [0,1,0,-1]
dy = [-1,0,1,0]
udx = [1,0,-1,0]
udy = [0,-1,0,1]
ddx = [1,0,-1,0]
ddy = [0,1,0,-1]
airclear = []
def diffusion() :
    global map,dx,dy,airclear
    tmpmap = [[0 for i in range(C)] for i in range(R)]
    for i in range(R) :
        for j in range(C) :
            if map[i][j] == -1 :
                airclear.append((i,j))
            if map[i][j] > 0 :
                cnt = 0
                point = int(map[i][j]/5)
                for k in range(4) :
                    tx = j+dx[k]
                    ty = i+dy[k]
                    if 0 <= tx < C and 0 <= ty < R and map[ty][tx] >= 0 :
                        cnt += 1
                        tmpmap[ty][tx] += point
                map[i][j] -= point*cnt
    for i in range(R) :
        for j in range(C) :
            if tmpmap[i][j] > 0 :
                map[i][j] += tmpmap[i][j]

def wind() :
    global map,udx,udy,ddx,ddy
    temp = [0]
    # upward
    d = 0
    sy,sx = airclear[0]
    while (1):
        if 0 > sy + udy[d] or sy + udy[d] >= R or 0 > sx + udx[d] or sx + udx[d] >= C:
            d += 1
        if map[sy][sx] >= 0 :
            temp.append(map[sy][sx])
            map[sy][sx] = temp[len(temp)-2]
        sy += udy[d]
        sx += udx[d]
        if (sy, sx) == airclear[0]:
            break
    # downward
    temp = [0]
    d = 0
    sy,sx = airclear[1]
    while (1):
        if 0 > sy + ddy[d] or sy + ddy[d] >= R or 0 > sx + ddx[d] or sx + ddx[d] >= C:
            d += 1
        if map[sy][sx] >= 0 :
            temp.append(map[sy][sx])
            map[sy][sx] = temp[len(temp)-2]
        sy += ddy[d]
        sx += ddx[d]
        if (sy, sx) == airclear[1]:
            break
for i in range(T) :
    diffusion()
    wind()
res = 0
for i in range(R):
    res += sum(map[i])
print(res+2)
