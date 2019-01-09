for a in range(int(input())) :
    n = int(input())
    l = list(map(int,input().split()))
    ma = -9999
    s = 0
    for i in l :
        s+=i
        if s > ma : 
            ma = s
        if s < 0 :
            s = 0
             
    print(f'#{a+1} {ma}')