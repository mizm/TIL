for tc in range(int(input())):
    n,k,m =list(map(int,input().split()))
    charge=list(map(int,input().split()))
    result = 0
    now = 0
    many = len(charge)
    check = True
    while check :
        check = False
        if now + k >= n :
            break
        if now+k in charge :
            now += k
            result += 1
            check = True
            continue
        for t in range(k) :
            if now + t in charge :
                now += t
                result += 1
                check = True
                break
    if not check :
        result = 0
    print(result)
        
            