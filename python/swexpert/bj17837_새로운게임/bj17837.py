import sys
sys.stdin = open('bj17837.txt','r')

N, K = map(int,sys.stdin.readline().split())

originMap = []
for i in range(N) :
    originMap.append(list(map(int,sys.stdin.readline().split())))
gameMap = [[[] for _ in range(N)] for __ in range(N)]
knights = []
# 2 파랑 1 빨강 0 흰색
for i in range(K) :
    y,x,dir = map(int,input().split())
    knights.append([y-1,x-1,dir])
    gameMap[y-1][x-1].append(i)

res = 0

def isSafe(y,x) :
    return 0<= x < N and 0 <= y < N and originMap[y][x] < 2

def go(y,x,dy,dx) :
    goList = gameMap[y][x][gameMap[y][x].index(num):]
    for i in range(len(goList)):
        gameMap[y][x].pop()
    if originMap[y + dy][x + dx] == 1:
        goList.reverse()
    for k in goList:
        knights[k][0] = y + dy
        knights[k][1] = x + dx
    gameMap[y + dy][x + dx].extend(goList)
    return len(gameMap[y+dy][x+dx]) >= 4
while res < 1001 :
    res+=1
    end = False
    dirArray = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)]
    for (num,knight) in enumerate(knights) :
        y,x,dir = knight
        dy, dx = dirArray[dir]
        if isSafe(y + dy, x + dx):
            end = go(y,x,dy,dx)
        else :
            # 못갈경우 방향 바꾸고 한번더 가보고 또 못가면 제자리
            dir += 1 if dir%2 == 1 else -1
            dy, dx = dirArray[dir]
            if isSafe(y+dy, x+dx) :
             #go
                end = go(y, x, dy, dx)
            knight[2] = dir
        if end :
            break
    if end :
        break
print(res if res <= 1000 else -1)

#


