import sys
sys.stdin = open('bj17472.txt','r')

N, M = map(int,input().split())
originMap = []
for _ in range(N) :
    originMap.append(list(map(int,input().split())))
def isSafe(x,y) :
    return 0 <= x < M and 0 <= y < N and originMap[y][x] == 1
def getDirXY(x,y,dir) :
    if dir == 0 :
        return (x,y-1)
    elif dir == 1 :
        return (x+1,y)
    elif dir == 2 :
        return (x,y+1)
    elif dir == 3 :
        return (x-1,y)
def drawCountry(x,y,num) :
    originMap[y][x] = num
    country = [(x,y)]
    q = [(x,y)]
    while q :
        x1,y1 = q.pop(0)
        for i in range(4) :
            dx,dy = getDirXY(x1,y1,i)
            if isSafe(dx,dy) :
                originMap[dy][dx] = num
                q.append((dx,dy))
                country.append((dx,dy))
    countries[num] = country
countryNum = 2
countries = {}
for y in range(N) :
    for x in range(M) :
        if originMap[y][x] == 1 :
            drawCountry(x,y,countryNum)
            countryNum += 1

count = countryNum - 2
ledge = []

def distance(x1,y1,x2,y2) :
    if x1 != x2 and y1 != y2 :
        return 1
    if x2 == x1 :
        for k in range(min(y2, y1) + 1, max(y2, y1)) :
            if originMap[k][x1] != 0 :
                return 1
        return abs(y2-y1) - 1
    if y2 == y1 :
        for k in range(min(x2, x1) + 1, max(x2, x1)) :
            if originMap[y1][k] != 0 :
                return 1
        return abs(x2 - x1) - 1
    return 1
for i in range(2,countryNum) :
    for j in range(i+1, countryNum) :
        dis = N*M
        for x1,y1 in countries[i] :
            for x2,y2 in countries[j] :
                t = distance(x1,y1,x2,y2)
                if t > 1:
                    ledge.append((i,j,t))
used = [0 for i in range(len(ledge))]
res = N*M*N*M
def dfs(n) :
    global res
    if n >= len(used) :
        visited = [0 for i in range(count)]
        cnt = 0
        for i in range(len(used)) :
            if used[i] == 1 :
                visited[ledge[i][0] - 2] = 1
                visited[ledge[i][1] - 2] = 1
                cnt+= ledge[i][2]
        if cnt > res :
            return
        if sum(visited) == len(visited):
            needledge = []
            for i in range(len(used)) :
                if used[i] == 1 :
                    needledge.append(ledge[i])
            needVisited = [0 for i in range(count)]
            q = [2]
            while q :
                start = q.pop(0)
                needVisited[start-2] = 1
                for s,e,t in needledge :
                    if s == start and needVisited[e-2] == 0:
                        q.append(e)
                    if e == start and needVisited[s-2] == 0:
                        q.append(s)

            if sum(needVisited) == len(visited) and res > cnt :
                res = cnt
        return
    used[n] = 1
    dfs(n+1)
    used[n] = 0
    dfs(n + 1)

dfs(0)
print(res if res != N*M*N*M else -1)


