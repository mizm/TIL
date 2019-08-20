import sys

sys.stdin = open('bj13460.txt','r')

N,M = map(int,input().split())
dx = [0,1,0,-1]
dy = [-1,0,1,0]
ta = []
visited = {}
for i in range(N) :
    t = input()
    te = []
    for j in range(M) :
        if t[j] == 'R' :
            red =[i,j]
            te.append('.')
            continue
        if t[j] == 'B' :
            blue = [i,j]
            te.append('.')
            continue
        te.append(t[j])
    ta.append(te)
def isSafe(x,y,ma) :
    global M,N
    if 0 <= x < M and 0 <= y < N :
        if ma[y][x] == '.':
            return 1
        if ma[y][x] == 'O' :
            return 2
    return 0
def go(i,rx,ry,bx,by,ma) :
    global dx,dy
    ma[ry][rx] = 'R'
    ma[by][bx] = 'B'
    goalred = False
    goalblue = False
    while 1 :
        chk = 0
        gored = isSafe(rx+dx[i],ry+dy[i],ma)
        goblue = isSafe(bx+dx[i],by+dy[i],ma)
        if gored :
            if gored == 1 :
                ma[ry][rx] = '.'
                rx+=dx[i]
                ry+=dy[i]
                ma[ry][rx] = 'R'
            if gored == 2 :
                goalred = True
                ma[ry][rx] = '.'
                ry = -10
                rx = -10
        else :
            chk += 1
        if goblue :
            if goblue == 1 :
                ma[by][bx] = '.'
                bx+=dx[i]
                by+=dy[i]
                ma[by][bx] = 'B'
            if goblue == 2 :
                goalblue = True
                ma[by][bx] = '.'
                by = -1
                bx = -1
        else :
            chk+=1
        if chk == 2:
            break
    if 0<= rx < M and 0<= ry < N :
        ma[ry][rx] = '.'
    if 0 <= bx < M and 0 <= by < N:
        ma[by][bx] = '.'
    if goalblue :
        return 1,rx,ry,bx,by
    if goalred :
        return 2,rx,ry,bx,by
    return 0,rx,ry,bx,by

def bfs(rx,ry,bx,by,ma) :
    Q = []
    pos = 1
    visited[(rx,ry,bx,by)] = 1
    for i in range(4) :
        Q.append((pos,i,rx,ry,bx,by))
    while Q :
        pos,dir,rx,ry,bx,by = Q.pop(0)
        if pos > 10 :
            return -1
        chk,rrx,rry,bbx,bby = go(dir,rx,ry,bx,by,ma)
        if chk == 2 :
            return pos
        if chk == 0 :
            if not visited.get((rrx,rry,bbx,bby)) :
                visited[(rrx,rry,bbx,bby)]=1
                for i in range(4) :
                    if dir != i or dir % 2 == i % 2:
                        Q.append((pos+1,i,rrx,rry,bbx,bby))
    return -1

print(bfs(red[1],red[0],blue[1],blue[0],ta))