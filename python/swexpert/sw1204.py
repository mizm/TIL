for a in range(int(input())):
    input()
    l=list(map(int,input().split()))
    p=0
    k=0
    for i in range(101):
        c = l.count(i)
        if p <= c:
            p=c
            k=i
    print(f'#{a+1} {k}')