for tc in range(int(input())) :
    n, k = list(map(int, input().split()))
    result = 0
    for i in range(1<<12) :
        item = []
        for j in range(12) :
            if i & 1<<j :
                item.append(j+1)
        if sum(item) == k and len(item) == n :
            result+=1
    print(f'#{tc+1} {result}')
