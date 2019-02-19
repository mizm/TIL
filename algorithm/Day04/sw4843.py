for tc in range(int(input())) :
    n = int(input())
    data = list(map(int, input().split()))
    for i in range(n) :
        item = i
        for j in range(i+1,n) :
            if not i%2 and data[item] < data[j]:
                item = j
            elif i%2 and data[item] > data[j] :
                item = j
        data[i],data[item] = data[item],data[i]
    result = ' '.join(list(map(str,data[:10])))
    print(f'#{tc+1} {result}')