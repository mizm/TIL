for tc in range(int(input())):
    vn,en,ax,ay = map(int,input().split())
    data = list(map(int,input().split()))
    tree = {1:[0,[]]}
    for i in range(len(data)) :
        if not i & 1 :
            if tree.get(data[i]) :
                tree[data[i]][1].append(data[i+1])
            else :
                tree[data[i]] = [0,[data[i+1]]]
            if tree.get(data[i+1]) :
                tree[data[i+1]][0] = data[i]
            else :
                tree[data[i+1]] = [data[i],[]]
    rea = []
    a = tree[ax][0]
    while a > 0 :
        rea.append(a)
        a = tree[a][0]
    reb = []
    b = tree[ay][0]
    while b > 0:
        reb.append(b)
        b = tree[b][0]
    for res_idx in rea :
        if res_idx in reb :
            break
    cnt = 0
    Q = [res_idx]
    while Q :
        cnt += 1
        item = Q.pop(0)
        for i in tree[item][1] :
            Q.append(i)
    print("#%d %d %d"%(tc+1,res_idx,cnt))
