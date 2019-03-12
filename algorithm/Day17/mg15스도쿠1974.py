def chk(l) :
    for i in range(1,10) :
        if not l.count(i) == 1:
            return 0
    return 1
for i in range(int(input())) :
    m = [] #가로
    r = [] #네모
    k = [] #세로
    cnt = 1
    for t in range(9):
        k.append([])
        r.append([])
    for j in range(9) :
        m.append(list(map(int,input().split())))
        for t in range(9) :
            k[t].append(m[j][t])
            r[t//3*3+j//3].append(m[j][t])
    for j in range(9) :
        if chk(k[j]) and chk(m[j]) and chk(r[j]) :
            continue
        else :
            cnt = 0
            break
    print('#%d %d'%((i+1),(cnt)))