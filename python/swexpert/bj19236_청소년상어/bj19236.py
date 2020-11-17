import sys
sys.stdin = open('bj19236.txt','r')

import copy
myMap = [[[0,0] for i in range(4)] for j in range(4)]

for i in range(4) :
    items = list(map(int,input().split()))
    for j in range(4) :
        myMap[i][j] = [items[j*2], items[j*2+1]]
dirs = [(),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]


ans = myMap[0][0][0]
sharkDir = myMap[0][0][1]
sx,sy = 0,0
myMap[0][0] = [0,sharkDir]

def isGo(myMap, x,y,sx,sy) :
    # print(sx,sy,x,y)
    # print(0 <= x < 4 and 0 <= y < 4 and (x != sx or y != sy))
    return 0 <= x < 4 and 0 <= y < 4 and (x != sx or y != sy)
def isGo2(myMap, x,y) :
    return 0 <= x < 4 and 0 <= y < 4 and myMap[y][x][0] != 0
def move(myMap,x,y,sx,sy,dir) :
    global dirs
    chk = 0
    while chk < 8 :
        if dir > 8 :
            dir = 1
        dx, dy = dirs[dir]
        if isGo(myMap,x+dx,y+dy,sx,sy) :
            num = myMap[y+dy][x+dx][0]
            d = myMap[y + dy][x + dx][1]
            myMap[y+dy][x+dx][0] = myMap[y][x][0]
            myMap[y+dy][x+dx][1] = dir
            myMap[y][x][0] = num
            myMap[y][x][1] = d
            return
        dir += 1
        chk += 1
def dfs(myMap, sx,sy, sd, res) :
    global ans,dirs
#ans = max(ans,res)
    # tx, ty = sx, sy
    # sdx, sdy = dirs[sd]
    # chk = False
    # # tmap = copy.deepcopy(myMap)
    # for i in range(3):
    #     tx += sdx
    #     ty += sdy
    #     if isGo(myMap, tx, ty):
    #         chk = True
    # if not chk :
    #     print(sx,sy)
    #     for i in range(4) :
    #         print(myMap[i])
    #     ans = max(ans,res)
    #     print(ans,res)
    #     return

    # 물고기 이동
    for cnt in range(1,17) :
        chk = False
        for i in range(4) :
            for j in range(4) :
                if myMap[i][j][0] == cnt :
                    move(myMap,j,i,sx,sy,myMap[i][j][1])
                    chk = True
                if chk :
                    break
            if chk :
                break
    # 상어가 먹을곳 탐방
    tx, ty = sx,sy
    sdx, sdy = dirs[sd]
    chk = False
    # tmap = copy.deepcopy(myMap)
    for i in range(3) :
        tx += sdx
        ty += sdy
        if isGo2(myMap,tx,ty) :
            chk = True
            # originN = tmap[ty][tx][0]
            # originD = tmap[ty][tx][1]
            # tmap[ty][tx][0] = 0
            # dfs(tmap,tx,ty,originD,res+originN)
            # tmap[ty][tx][0] = originN
            # tmap[ty][tx][1] = originD
            tmap = copy.deepcopy(myMap)
            originN = tmap[ty][tx][0]
            #originD = tmap[ty][tx][1]
            gr = tmap[ty][tx][0]
            gsd = tmap[ty][tx][1]
            tmap[ty][tx][0] = 0
            #tmap[ty][tx][1] = gsd
            dfs(tmap,tx,ty,gsd,res + gr)
            tmap[ty][tx][0] = originN
            #tmap[ty][tx][1] = originD
        # else :
        #     return
    if not chk  :
        ans = max(ans,res)
        return
        # ans = max(ans,res)

dfs(myMap,0,0,sharkDir, ans)
print(ans)