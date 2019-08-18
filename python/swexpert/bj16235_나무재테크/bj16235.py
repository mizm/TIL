import sys

sys.stdin = open('bj16235.txt', 'r')

N,M,K = list(map(int,input().split()))
A = [ list(map(int,input().split())) for i in range(N) ]
trees = [list(map(int,input().split())) for i in range(M)]
map = [ [ [] for i in range(N)] for i in range(N)]
power = [ [5 for i in range(N)] for i in range(N)]
# 나무셋팅
for r,c,age in trees :
    map[r-1][c-1].append(age)
    if len(map[r-1][c-1]) > 1 :
        map[r-1][c-1].sort()

dx = [-1,0,1,1,1,0,-1,-1]
dy = [-1,-1,-1,0,1,1,1,0]

for year in range(K) :
    for i in range(N) :
        for j in range(N) :
            if map[i][j] :
                temp = []
                die = 0
                for k in range(len(map[i][j])) :
                    if power[i][j] >= map[i][j][k] :
                        power[i][j] -= map[i][j][k]
                        temp.append(map[i][j][k] + 1)
                    else :
                        die += int(map[i][j][k] / 2)
                map[i][j] = temp
                # summer
                power[i][j] += die
    # fall
    for i in range(N):
        for j in range(N):
            if map[i][j] :
                for age in map[i][j] :
                    if age % 5 == 0 :
                        for k in range(8) :
                            tx = j + dx[k]
                            ty = i + dy[k]
                            if 0 <= tx < N and 0 <= ty < N :
                                map[ty][tx].insert(0,1)
    # winter
    for i in range(N) :
        for j in range(N) :
            power[i][j] += A[i][j]
res = 0
for i in range(N) :
    for j in range(N) :
        if map[i][j] :
            res += len(map[i][j])
print(res)

