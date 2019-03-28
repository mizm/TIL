def find(x) :
    if dis[x] != x:
        dis[x] = find(dis[x])
    return dis[x]
def union(x,y) :
    dis[find(y-1)] = find(x-1)
for tc in range(int(input())) :
    n,m = map(int,input().split())
    dis = [i for i in range(n)]
    vote = list(map(int,input().split()))
    for i in range(m) :
        union(vote[i*2],vote[i*2+1])
    res = []
    for i in dis :
        t = find(i)
        if not t in res :
            res.append(t)
    print("#%d %d"%(tc+1,len(res)))