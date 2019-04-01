def dfs(x,item):
    if len(k[x-1]) == 0:
        res[x-1] += item
        return
    for i in k[x-1] :
        dfs(i[0],item*i[1])
n = int(input())
m = int(input())
k = [[] for i in range(n)]
res = [0]*n
for i in range(m) :
    x,y,t = map(int,input().split())
    k[x-1].append((y,t))
dfs(n,1)
for i in range(n) :
    if res[i] > 0 :
        print("%d %d"%(i+1,res[i]))
