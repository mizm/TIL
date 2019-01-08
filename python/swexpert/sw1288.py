for a in range(int(input())) :
    t=1
    n=int(input())
    k=n*t
    p=set()
    while True:
        for i in str(k):
            p.add(int(i))
        if len(p) == 10 : break
        t+=1
        k = n*t
    print(f'#{a+1} {k}')
    