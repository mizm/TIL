import sys

sys.stdin = open('bj15683.txt','r')

def dfs(pos):
    global N, M, res, map, dx, dy, seeDelta, cameraCount, camera, seeXY
    if pos == cameraCount :
        if len(seeXY) > res :
            res = len(seeXY)
        return
    y,x,d = camera[pos]
    for go in seeDelta[d] :
        cnt = 0
        for w in go :
            ty = y + dy[w]
            tx = x + dx[w]
            for i in range(30) :
                if 0 > tx or tx >= M or 0 > ty or ty >= N or map[ty][tx] == 6 :
                    break
                if not (tx,ty) in seeXY and map[ty][tx] == 0:
                    cnt += 1
                    seeXY.append((tx,ty))
                tx += dx[w]
                ty += dy[w]
        dfs(pos+1)
        for i in range(cnt) :
            seeXY.pop(len(seeXY)-1)



N, M = list(map(int,input().split()))

map = [list(map(int,input().split())) for i in range(N)]

dx = [0,1,0,-1]
dy = [-1,0,1,0]

seeDelta = [
    [],
    [[0],[1],[2],[3]],
    [(0,2),(1,3)],
    [(0,1),(1,2),(2,3),(3,0)],
    [(0,1,3),(0,1,2),(1,2,3),(0,2,3)],
    [(0,1,2,3)]
]

camera = []
wallCount = 0
for i in range(N) :
    for j in range(M) :
        if 0 < map[i][j] < 6 :
            camera.append([i,j,map[i][j]])
        elif map[i][j] == 6 :
            wallCount += 1
cameraCount = len(camera)

seeXY = []
res =  -1
dfs(0)
print(N*M - res - cameraCount - wallCount)