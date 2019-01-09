D
    v = d = 0
    for j in range(int(input())):
        p = input()
        if int(p[0]):
            a,b = list(map(int,p.split()))
        else:
            a = 0
        if a == 1:
            v += b
        if a == 2:
            v -= b
            if v < 0:
                v = 0
        d += v
    print(f'#{i+1} {d}')