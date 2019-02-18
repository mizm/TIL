for tc in range(int(input())):
    k,n,m =list(map(int,input().split()))
    charge=list(map(int,input().split()))
    result = 0
    now = 0
    check = True
    while check :
        check = False
        if now + k >= n :
            check = True
            break
        for t in range(k,0,-1) :
            if now + t in charge :
                now += t
                result += 1
                check = True
                break
    if not check :
        result = 0
    print(f'#{tc+1} {result}')