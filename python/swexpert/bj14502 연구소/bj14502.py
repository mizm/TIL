import itertools
N, M = map(int,input().split())
mymap = [list(map(int,input().split())) for i in range(N)]

space = []
virus = []
idx = -1
spaceCnt = -3
for i in range(N) :
    for j in range(M) :
        if mymap[i][j] == 0 :
            space.append(idx)
            mymap[i][j] = idx
            idx -= 1
            spaceCnt+=1
        if mymap[i][j] == 2 :
            virus.append((i,j))

dx = [0,1,0,-1]
dy = [-1,0,1,0]

def isSafe(x,y,twall) :
    return 0<=x< M and 0<= y < N and mymap[y][x] < 0 and not mymap[y][x] in twall
res = N*M
# for i in range(N) :
# print(mymap[i])
for t in itertools.combinations(space,3) :
    # print(list(t))
    tw = list(t)
    # tw = [-1,-5,-16]
    emr = 0
    Q = virus[:]
    while Q :
        if emr > res :
            break
        y,x = Q.pop(0)
        for i in range(4):
            if isSafe(x+dx[i],y+dy[i],tw) :
                Q.append((y+dy[i],x+dx[i]))
                emr+=1
                tw.append(mymap[y+dy[i]][x+dx[i]])
                # print(tw)
     if res > emr :
        res = emr
print(spaceCnt - res)