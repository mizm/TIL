import sys
sys.stdin = open('bj16234.txt','r')

from collections import deque
N,L,R = map(int,input().split())
A = [list(map(int,input().split())) for i in range(N)]
dx = [0,1,0,-1]
dy = [-1,0,1,0]

cnt = 0
def bfs(y,x,pk) :
    global A,visited
    Q = deque([(y,x)])
    visited[y][x] = pk
    cnt = 1
    people = A[y][x]
    temp = [(y,x)]
    while Q :
        y,x = Q.popleft()
        for i in range(4) :
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx < N and 0 <= ty < N and visited[ty][tx] == 0 and L <= abs(A[y][x] - A[ty][tx]) <= R:
                visited[ty][tx] = pk
                Q.append((ty,tx))
                cnt += 1
                people += A[ty][tx]
                temp.append((ty,tx))
    t = int(people/cnt)
    for y,x in temp:
        A[y][x] = t


while 1 :
    visited = [[0 for i in range(N)] for i in range(N)]
    p = 1
    for i in range(N) :
        for j in range(N) :
            if visited[i][j] == 0 :
                bfs(i,j,p)
                p += 1
    if p-1 == N*N :
        break
    cnt += 1
print(cnt)
