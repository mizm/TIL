
for tc in range(int(input())):
    n,t = map(int,input().split())
    titem = list(map(int,input().split()))
    a = min(titem)
    b = max(titem)
    max_v = 10**9
    l = 0
    r = b-a
    # while l <= r :
    for kk in range(r+1) :
        m = kk
        p = 0
        item = titem[:]
        for i in range(n-1) :
            if item[i] > item[i+1] + m :
                p += item[i] - (item[i+1] + m)
                item[i] -= item[i] - (item[i+1] + m)
                continue
            if item[i+1] > item[i] + m :
                p += item[i+1] - (item[i] + m)
                item[i+1] -= item[i+1] - (item[i] + m)
        print(m,p,item)
        if p <= t :
            if max_v > m :
                max_v = m
            break
            r = m-1
        else :
            continue

        # else :
        #     l = m
        #     break
    print("#%d %d"%(tc+1,max_v))

