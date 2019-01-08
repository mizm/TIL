for a in range(int(input())):
    p,q,r,s,w=list(map(int,input().split()))
    b=0
    if r >= w :
        b=q
    else :
        b=q+(w-r)*s
    if p*w < b :
        k=p*w
    else :
        k=b
    print(f'#{a+1} {k}')