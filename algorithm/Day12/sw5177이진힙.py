for tc in range(int(input())) :
    n = int(input())
    tree = [0] * (n+1)
    Data = list(map(int,input().split()))
    r = 1
    for i in range(n) :
        tree[r] = Data[i]
        k = r
        while k > 1 :
            if tree[k//2] > tree[k] :
                tree[k],tree[k//2] = tree[k//2],tree[k]
                k //= 2
            else :
                break
        r+=1
    r-=1
    result = 0
    while r > 1 :
        r //= 2
        result += tree[r]
    print('#{} {}'.format((tc+1),result))