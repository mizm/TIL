for i in range(int(input())) :
    cnt = 0
    a,b = list(map(int,input().split()))
    l = list(map(int,input().split()))
    k = list(map(int,input().split()))
    if a > b:
        a,b = b,a
        l,k = k,l
    o=0
    for j in range(b-a+1) :
        p = 0
        for t in range(a) :
            p+=l[t]*k[t+j]
        if o<p:
            o = p
    print(f'#{i+1} {o}')                
