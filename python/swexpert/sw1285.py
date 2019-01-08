for a in range(int(input())):
    mi = 1000000
    nm = 0
    n=int(input())
    l=list(map(int,input().split()))
    for k in l :
        k=abs(k)
        if mi > k :
            nm = 1
            mi = k
        elif mi == k:
            nm+=1
    print(f'#{a+1} {nm} {mi}')
