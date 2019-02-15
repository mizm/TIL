for tc in range(int(input())):
    n,m =list(map(int,input().split()))
    v=list(map(int,input().split()))
    my_max = -1
    my_min = 10000*m
    for i in range(n-m+1) :
        item = 0
        for j in range(m) :
            item += v[i+j]
        if my_max < item :
            my_max = item
        if my_min > item :
            my_min = item
    print(f'#{tc+1} {my_max-my_min}')