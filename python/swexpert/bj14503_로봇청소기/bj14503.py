import sys

sys.stdin = open('bj14503.txt','r')

N,M = map(int,input().split())

r,c,d = list(map(int,input().split()))

MAP = [list(map(int,input().split())) for i in range(N)]

dx = [-1,0,1,0]
dy = [0,-1,0,1]
dd = [3,0,1,2]
backx = [0,-1,0,1]
backy = [1,0,-1,0]
visited = [ [1 for i in range(M)] for j in range(N)]
res = 0
def isSafe(y,x,k) :
    if k :
        return 0<= y < N and 0 <= x < M and MAP[y][x] == 0
    else :
        return 0 <= y < N and 0 <= x < M and MAP[y][x] != 1
Q = [(r,c,d,1)]

while Q :

    y,x,d,r= Q.pop(0)
    res+=r
    td = d
    MAP[y][x] = 2
    chk = True
    for i in range(4) :
        if isSafe(y+dy[td],x+dx[td],True):
            Q.append((y+dy[td],x+dx[td],dd[td],1))
            chk = False
            break
        else :
            td = dd[td]
    if isSafe(y+backy[d], x+backx[d],False) and chk:
        Q.append((y+backy[d],x+backx[d],d,0))


print(res)

