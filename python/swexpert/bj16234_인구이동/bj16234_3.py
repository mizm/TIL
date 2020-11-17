import sys
sys.stdin = open('bj16234.txt','r')

N,L,R = map(int,input().split())

country = []

for i in range(N) :
    country.append(list(map(int,input().split())))

from collections import deque


def isGo(x,y,union) :
    return 0<=x<N and 0<=y<N and union[y][x] == 0

dir = [(1,0),(-1,0),(0,1),(0,-1)]

res = 0
while res < 2001 :
    union = [[0 for _ in range(N)] for __ in range(N)]
    unionCnt = 0
    for i in range(N) :
        for j in range(N) :
            if union[i][j] != 0 :
                continue
            else :
                unionCnt+=1
                q = deque()
                q.append((i,j))
                while q :
                    y,x = q.popleft()
                    for dx,dy in dir :
                        if isGo(x+dx,y+dy,union) :
                            if L<= abs(country[y][x] - country[y+dy][x+dx]) <= R :
                                union[y+dy][x+dx] = unionCnt
                                q.append((y+dy,x+dx))
    if unionCnt >= N*N :
        break
    res += 1
    unionNum = [0 for i in range(N*N)]
    people = [0 for i in range(N*N)]
    for i in range(N) :
        for j in range(N) :
            if union[i][j] > 0 :
                unionNum[union[i][j]] += 1
                people[union[i][j]] += country[i][j]
    for i in range(N) :
        for j in range(N) :
            if union[i][j] > 0 :
                country[i][j] = people[union[i][j]]//unionNum[union[i][j]]
    # for i in range(N) :
    #     print(country[i])
print(res)
