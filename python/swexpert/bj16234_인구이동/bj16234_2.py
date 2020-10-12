import sys

sys.stdin = open('bj16234.txt','r')

N,L,R = map(int,input().split())

people = []

for _ in range(N) :
    people.append(list(map(int,input().split())))

dx = [0,0,1,-1]
dy = [1,-1,0,0]
def isSafe(x,y) :
    global visited
    return 0<= x < N and 0 <= y < N and visited[y][x] == 0

def doUnion(x,y) :
    global visited,people,dx,dy
    visited[y][x] = 1
    union = [(x,y)]
    cnt = people[y][x]
    q = [(x,y)]
    while q :
        x,y = q.pop(0)
        for i in range(4) :
            rx = x+dx[i]
            ry = y+dy[i]
            if isSafe(rx,ry) and L <= abs(people[y][x] - people[ry][rx]) <= R :
                union.append((rx,ry))
                visited[ry][rx] = 1
                q.append((rx,ry))
                cnt+= people[ry][rx]
    cnt = int(cnt / len(union))
    for x,y in union :
        people[y][x] = cnt
    return 1 if len(union) == 1 else 0

for res in range(2000) :
    visited = [[0 for _ in range(N)] for __ in range(N)]
    k = 0
    for y in range(N) :
        for x in range(N) :
            if visited[y][x] == 0 :
                k += doUnion(x,y)
    if k == N*N :
        print(res)
        break