def dfs(pos,dir,x,y,visit) :
    key = visit*1000+pos*10+dir
    k = c.get(key)
    if k :
        return k
    k = 0

    for i in range(1,n+1):
        if visit & (1<<(i-1)) : continue
        s = visit | (1<<(i-1))
        for j in range(3) :
            x1,y1,z1 = data[i][j]
            if x >= x1 and y >= y1 :
                k = max(k,z1+dfs(i,j,x1,y1,s))
    c[key] = k
    return k

for tc in range(int(input())) :
    n = int(input())
    data = [[] for i in range(n+1)]
    data[0].append([1000000,1000000,0])
    data[0].append([1000000, 1000000, 0])
    data[0].append([1000000, 1000000, 0])
    c = {}
    for i in range(n) :
        k = list(map(int,input().split()))
        for p in range(3):
            for j in range(p + 1, 3):
                if k[p] > k[j]:
                    k[p], k[j] = k[j], k[p]
        data[i+1].append([k[0],k[1],k[2]])
        data[i+1].append([k[0], k[2], k[1]])
        data[i+1].append([k[1], k[2], k[0]])
    # print(data)
    res = -1
    print("#%d %d"%(tc+1,dfs(0,0,1000000,1000000,0)))
    # for k,v in c.items() :
    #     print(k,v)
