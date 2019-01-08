for i in range(int(input())) :
    t = 0
    for j in range(int(input())):
        a,b=list(map(float,input().split()))
        t+=a*b
    print(f'#{i+1} {t}')
