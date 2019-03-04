for tc in range(int(input())) :
    n,k = map(int, input().split())
    t = [0]*n
    for i in  list(map(int,input().split())) :
        t[i-1] = 1
    print('#{0}'.format(tc+1),end=' ')
    for i in range(n) :
        if not t[i] :
            print(i+1,end = ' ')
    print()
