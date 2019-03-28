import collections
def bfs() :
    Q = collections.deque([n])
    item = [MAXVALUE]*1000001
    item[n] = 0
    while Q:
        t = Q.popleft()
        for i in range(4) :
            q = 0
            if i == 0 :
                q = t*2
            else :
                q = t+d[i]
            if 0 < q < 1000001 and item[q] == MAXVALUE:
                item[q] = item[t]+1
                if q == m :
                    return item[m]
                Q.append(q)


for tc in range(int(input())) :
    n,m = map(int,input().split())
    chk = 0
    d = [2,1,-1,-10]
    MAXVALUE = 987654321


    print("#%d %d"%(tc+1,bfs()))