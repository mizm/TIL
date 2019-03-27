n = int(input())
gset = [i for i in range(n)]
k = int(input())
def find_parent(x) :
    if gset[x] != x :
        gset[x] = find_parent(gset[x])
    return gset[x]
def union(a,b) :
    gset[find_parent(b)] = find_parent(a)

for i in range(k) :
    a,b = map(int,input().split())
    union(a-1,b-1)
cnt = 0
for i in range(n) :
    gset[i] = find_parent(i)
for i in range(1,n):
    if gset[0] == gset[i] :
        cnt+=1
print(cnt)