for tc in range(int(input())) :
    n = int(input())
    item = []
    result = []
    data = list(map(int, input().split()))
    for i in range(n) :
        item.append(data[i*2:i*2+2])
    result.append(item.pop())
    while len(item) :
        re = len(result) - 1
        chk = result[re][1]
        selectchk = False
        for i in range(len(item)) :
            if chk == item[i][0] :
                result.append(item.pop(i))
                selectchk = True
                break
        if selectchk :
            continue
        chk = result[0][0]
        for i in range(len(item)) :
            if chk == item[i][1] :
                result.insert(0,item.pop(i))
                break
    print(f'#{tc+1}',end=' ')
    for i in result :
        print(i[0],i[1],sep=' ',end=' ')
    print()



