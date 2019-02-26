for tc in range(int(input())) :
    n,m = list(map(int,input().split()))
    data = list(map(int,input().split()))
    Q = [-1]*n
    cnt = -1
    while Q :
        item = Q.pop(0)
        if item == -1 :
            if cnt < len(data)-1 :
                cnt += 1
                Q.append(cnt)
            continue
        data[item] //= 2
        if data[item] :
            Q.append(item)
        else :
            if cnt < len(data)-1 :
                cnt+=1
                Q.append(cnt)
    print(f'#{tc+1} {item+1}')