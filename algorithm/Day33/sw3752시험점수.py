for tc in range(int(input())) :
    n = int(input())
    data = list(map(int,input().split()))
    res = []
    t = sum(data)+1
    c = [0]*(sum(data)+1)
    c[0] = 1
    for j in range(n) :
        for i in range(t-1,-1,-1) :
            if c[i] :
                c[data[j]+i] = 1
    print("#%d %d"%(tc+1,sum(c)))