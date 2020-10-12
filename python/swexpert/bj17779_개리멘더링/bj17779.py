import sys

sys.stdin = open('bj1779.txt', 'r')

N = int(input())
m = [list(map(int,input().split())) for _ in range(N)]
res = 101 * N * N
def makeMap(x,y,d1,d2) :
    tm = [[7 for i in range(N)] for j in range(N)]
    for j in range(N):
        for i in range(N):
            r = i + 1
            c = j + 1
            if 1 <= r and r < x + d1 and 1 <= c and c <= y:
                tm[i][j] = 0
                continue
            if 1 <= r and r <= x + d2 and y < c and c <= N:
                tm[i][j] = 1
                continue
            if x + d1 <= r and r <= N and 1 <= c and c < y - d1 + d2:
                tm[i][j] = 2
                continue
            if x + d2 < r and r <= N and y - d1 + d2 <= c and c <= N:
                tm[i][j] = 3
                continue
    y1 = y
    y2 = y
    tm[x - 1][y - 1] = 4
    for i in range(1, d1 + d2 + 1):
        x1 = x + i
        if i > d1 :
            ls = 1
        else :
            ls = -1
        if i > d2 :
            rs = -1
        else :
            rs = 1
        y1 += ls
        y2 += rs
        for j in range(y1, y2 + 1):
            tm[x1 - 1][j - 1] = 4
    return tm
for d1 in range(1,N-1) :
    for d2 in range(1,N-1) :
        for x in range(1,N-1) :
            for y in range(1, N-1) :
                if 1 <= x  and x < x+d1+d2 and x+d1+d2 <= N and 1 <= y-d1 and y-d1 < y and y < y+d2 and y+d2 <= N :
                    item = [0,0,0,0,0]
                    tm = makeMap(x,y,d1,d2)
                    for i in range(N) :
                        for j in range(N) :
                            item[tm[i][j]] += m[i][j]
                    res = min(res, max(item) - min(item))
print(res)

