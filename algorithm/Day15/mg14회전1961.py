for i in range(int(input())):
    n=int(input())
    k=[]
    for j in range(n):
        k.append(list(map(int,input().split())))
    print(f'#{i+1}')
    for j in range(n):
        for l in range(n):
            print(k[n-1-l][j],end='')
        print(end=' ')
        for l in range(n):
            print(k[n-1-j][n-1-l],end='')
        print(end=' ')
        for l in range(n):
            print(k[l][n-1-j],end='')
        print()