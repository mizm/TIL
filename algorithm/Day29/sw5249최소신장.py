def find(x) :
    if dis[x] != x:
        dis[x] = find(dis[x])
    return dis[x]
def union(x,y) :
    dis[find(y)] = find(x)
for tc in range(int(input())) :
    v,e = map(int,input().split())
    data = []
    for i in range(e) :
        f,t,l = map(int,input().split())
        data.append([l,f,t])
    data.sort()
    item = [0]*(v+1)
    res = 0
    dis = [i for i in range(v+1)]
    cnt = 0
    for i in data :
        l,f,t = i
        if find(f) != find(t) :
            res += l
            union(t,f)
            item[f] += 1
            item[t] += 1
            cnt+=1
        if cnt == v :
            break
    print("#%d %d"%(tc+1,res))