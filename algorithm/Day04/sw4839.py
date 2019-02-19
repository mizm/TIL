for tc in range(int(input())) :
    n, a, b = list(map(int, input().split()))
    startA = startB = 1
    endA = endB = n
    ca = cb = 0
    while True :
        if startA > endA :
            break
        if startB > endB :
            break
        midA = (startA+endA)//2
        midB = (startB + endB) // 2
        if midA == a :
            ca-=1
            startA = endA + 1
        elif midA < a :
            startA = midA
        else :
            endA = midA
        if midB == b:
            cb-=1
            startB = endB + 1
        elif midB < b:
            startB = midB
        else:
            endB = midB
        ca +=1
        cb +=1
    result = '0'
    if ca < cb :
        result = 'A'
    elif ca > cb :
        result = 'B'
    print(f'#{tc+1} {result}')