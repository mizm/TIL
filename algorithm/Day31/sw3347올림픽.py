for tc in range(int(input())) :
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    res = [0]*n
    for k in b :
        for i in range(n) :
            if k >= a[i] :
                res[i]+=1
                break
    print("#%d %d"%(tc+1,res.index(max(res))+1))