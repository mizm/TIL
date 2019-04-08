for tc in range(int(input())) :
    n,o,m = list(map(int,input().split()))
    item = list(map(int,input().split()))
    oper = list(map(int,input().split()))
    w = int(input())
    c = [1000] * 1000
    ar = []
    for i in item :
        if i == 0 :
            c[i] = 1
            continue
        for j in item :
            for k in item :
                # if not c[i]:
                c[i] = 1
                ar.append((i, 1))
                # if not c[i*10+j] :
                c[i*10+j] = 2
                ar.append((i * 10 + j, 2))
                # if not c[i*100+j*10+k] and i*100+j*10+k < 1000:
                c[i*100+j*10+k] = 3
                ar.append((i*100+j*10+k, 3))
    res = -1
    if c[w] != 1000:
        res = c[w]
    else :
        Q = []
        for i in ar :
            Q.append(i)
        while Q :
            a,b = Q.pop(0)
            for i in ar :
                e,d = i
                cnt = b+d+1
                if cnt >= m:
                    continue
                for j in range(o) :
                    k= 0
                    if oper[j] == 1 :
                        k = a+e
                    if oper[j] == 2 :
                        k = a-e
                    if oper[j] == 3 :
                        k = a*e
                    if oper[j] == 4 :
                        k = a//e
                    if 0 >  k or k > 999 or c[k] <= cnt :
                    	continue
                    Q.append((k,cnt))
                    c[k] = cnt
        if c[w] > 0 and c[w] != 1000 :
            res = c[w]+1
    print("#%d %d"%(tc+1,res))