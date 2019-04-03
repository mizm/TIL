for tc in range(int(input())) :
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    l = min(a)
    r = max(a)
    while l <= r :
        m1 = (l+r)//2
        k = 0
        t = 0
        res = []
        for i in range(n) :
            if a[i] <= m1 :
                k+=1
                if k >= b[t] :
                    k -= b[t]
                    t+=1
                if t == m :
                    r = m1-1
                    break
            else :
                if k > 0 :
                    k = 0
        if t < m :
            l = m1+1
    print("#%d %d"%(tc+1,l))