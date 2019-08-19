import sys
sys.stdin = open('bj15684.txt', 'r')

N, M, H = map(int, input().split())

garo = [[0]*N for _ in range(H)]
for i in range(M):
    a, b = map(int, input().split())
    garo[a - 1][b - 1] = 1

def check():
    for i in range(N):
        k = i
        for j in range(H):
            if garo[j][k]:
                k += 1
            elif k > 0 and garo[j][k - 1]:
                k -= 1
        if i != k:
            return False
    return True

res = 4

def dfs(pos,x,y) :
    global res
    if res <= pos :
        return
    if check() :
        if res > pos :
            res = pos
        return
    if pos >= 3 :
        return
    for i in range(x, H):
        if i == x :
            k = y
        else :
            k = 0
        for j in range(k, N-1):
            if garo[i][j]:
                j += 1
            else:
                garo[i][j] = 1
                dfs(pos+1, i, j+2)
                garo[i][j] = 0
dfs(0,0,0)
if res == 4 :
    res = -1
print(res)