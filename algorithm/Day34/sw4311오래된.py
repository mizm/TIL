for tc in range(int(input())) :
    n,o,m = list(map(int,input().split()))
    item = list(map(int,input().split()))
    item.sort()
    temp = list(map(int,input().split()))
    w = int(input())
    opcode = [-1,-2,-3,-4]
    oper = []
    for i in temp :
        oper.append(opcode[i-1])
    c = [0] * 1000
    ar = []
    for i in item :
        if i == 0 :
            c[i] = 1
            continue
        for j in item :
            for k in item :
                if not c[i]:
                    c[i] = 1
                    ar.append([i, 1])
                if not c[i*10+j] :
                    c[i*10+j] = 2
                    ar.append([i * 10 + j, 2])
                if not c[i*100+j*10+k] and i*100+j*10+k < 1000:
                    c[i*100+j*10+k] = 3
                    ar.append([i*100+j*10+k, 3])
    res = 987654321
    if c[w] :
        res = c[w]
    else :
        Q = []
        for i in ar :
            Q.append(i)
        while Q :
            a,b = Q.pop(0)
            # print(a,b)
            if a == w :
                if res > b :
                    res = b
                continue
            for i in ar :
                c,d = i
                if b+d+2 > m or b+d+2 >= res:
                    continue
                for j in range(o) :
                    if oper[j] == -1 :
                        k = a+c
                    if oper[j] == -2 :
                        k = a-c
                    if oper[j] == -3 :
                        k = a*c
                    if oper[j] == -4 :
                        if c == 0 :
                            continue
                        k = a//c
                    if 0<=k<=999 :
                        Q.append([k,b+d+2])
                        ar.append([k,b+d+2])
    print(res)