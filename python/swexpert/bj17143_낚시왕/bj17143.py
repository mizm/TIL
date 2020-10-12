import sys
sys.stdin = open('bj17143.txt','r')

R,C,M = map(int,input().split())
dir = [(0,0),(0,-1),(0,1),(1,0),(-1,0)]
# 위 아래 오 왼
sharks = []
for i in range(M) :
    r,c,s,d,z = list(map(int,input().split()))
    sharks.append([i,r,c,s,d,z])

def cal(now, m, z, nowd) :
    while z > 0 :
        if nowd == 0 :
            if now - z > 0 :
                return now-z,nowd
            z -= now - 1
            now = 1
            nowd = 1
            continue
        elif nowd == 1 :
            if now + z <= m :
                return now+z,nowd
            z -= m - now
            now = m
            nowd = 0
            continue
    return (now,nowd)

def go(k) :
    n,r,c,s,d,z = sharks[k]
    if n < -1 :
        return
    if d <= 2 :
        r,td = cal(r,R,s,0 if d%2 == 1 else 1)
        if td == 1 :
            d = 2
        else :
            d = 1
    else :
        c,td = cal(c,C,s,1 if d%2 == 1 else 0)
        if td == 1 :
            d = 3
        else :
            d = 4
            sharks[k] = [n, r, c, s, d, z]
    for i in range(k) :
        if sharks[i][0] > -1 and sharks[i][1] == r and sharks[i][2] == c :
            if sharks[i][5] > z :
                n = -1
            else :
                sharks[i][0] = -1
    sharks[k] = [n,r,c,s,d,z]


res = 0
for k in range(C) :
    srow = R + 1
    sidx = -1
    for s in sharks :
        if s[0] >= 0 and s[2] == k + 1:
            if s[1] < srow :
                sidx = s[0]
                srow = s[1]
    if sidx > -1 :
        sharks[sidx][0] = -1
        res += sharks[sidx][5]
    for i in range(M) :
        go(i)
print(res)