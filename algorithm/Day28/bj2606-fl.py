n = int(input())
gset = [[0]*n for i in range(n)]
k = int(input())

for i in range(k) :
    a,b = map(int,input().split())
    gset[a-1][b-1] = 1
    gset[b - 1][a - 1] = 1
for k in range(n) :
    for i in range(n) :
        for j in range(n) :
            gset[j][i] = gset[j][i] or (gset[k][i] and gset[j][k])
print(gset[0].count(1)-1)