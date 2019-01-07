for i in range(int(input())) :
    cnt = 0
    a,b = list(map(int,input().split()))
    l = list(map(int,input().split()))
    k = list(map(int,input().split()))
    if a > b:
        a,b = b,a
        l,k = k,l
    top = 0
    for j in range(b-a+1) :
        temp = 0
        for t in range(a) :
            temp += l[t]*k[t+j]
        if top < temp:
            top = temp
    print(f'#{i+1} {o}')                
